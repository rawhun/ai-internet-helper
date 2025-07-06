import pytest
from unittest.mock import patch, MagicMock
from actions import ActionFallbackProvider, ActionCheckProviders

class DummyDispatcher:
    def __init__(self):
        self.messages = []
    def utter_message(self, text=None):
        self.messages.append(text)

class DummyTracker:
    def __init__(self, provider=None):
        self.slots = {"provider": provider}
    def get_slot(self, key):
        return self.slots.get(key)

@patch("actions.load_providers")
def test_fallback_provider(mock_load):
    mock_load.return_value = [
        {"name": "openai", "enabled": True},
        {"name": "huggingface", "enabled": True}
    ]
    dispatcher = DummyDispatcher()
    tracker = DummyTracker(provider="openai")
    action = ActionFallbackProvider()
    action.run(dispatcher, tracker, {})
    assert any("Switching to provider" in m for m in dispatcher.messages)

@patch("actions.load_providers")
@patch("actions.requests.get")
def test_check_providers(mock_get, mock_load):
    mock_load.return_value = [
        {"name": "openai", "enabled": True, "endpoint": "http://test"}
    ]
    mock_get.return_value.status_code = 200
    dispatcher = DummyDispatcher()
    tracker = DummyTracker()
    action = ActionCheckProviders()
    action.run(dispatcher, tracker, {})
    assert any("openai" in m for m in dispatcher.messages) 