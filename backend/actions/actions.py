import os
import yaml
import logging
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType

# Set up logging
logger = logging.getLogger(__name__)

# Load providers config
PROVIDERS_CONFIG = os.path.join(os.path.dirname(__file__), '../rasa_project/config/providers.yaml')

def load_providers():
    with open(PROVIDERS_CONFIG, 'r') as f:
        return yaml.safe_load(f)['providers']

class ActionFallbackProvider(Action):
    """Fallback to next available AI provider if one fails."""
    def name(self) -> Text:
        return "action_fallback_provider"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[EventType]:
        providers = load_providers()
        # Example: just cycle to next enabled provider
        current = tracker.get_slot('provider')
        enabled = [p for p in providers if p['enabled']]
        if not enabled:
            dispatcher.utter_message(text="No AI providers are currently enabled.")
            return []
        if current:
            idx = next((i for i, p in enumerate(enabled) if p['name'] == current), -1)
            next_idx = (idx + 1) % len(enabled)
            next_provider = enabled[next_idx]['name']
        else:
            next_provider = enabled[0]['name']
        dispatcher.utter_message(text=f"Switching to provider: {next_provider}")
        return []

class ActionCheckProviders(Action):
    """Check status of all AI providers."""
    def name(self) -> Text:
        return "action_check_providers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[EventType]:
        providers = load_providers()
        statuses = []
        for p in providers:
            status = "enabled" if p['enabled'] else "disabled"
            # Optionally, ping endpoint for real status
            try:
                resp = requests.get(p['endpoint'], timeout=2)
                if resp.status_code == 200:
                    status += ", online"
                else:
                    status += ", offline"
            except Exception as e:
                status += ", error"
            statuses.append(f"{p['name']}: {status}")
        dispatcher.utter_message(text="\n".join(statuses))
        return [] 