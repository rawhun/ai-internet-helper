import os
import logging
import time
import yaml
from sqlalchemy import create_engine, text
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer, TrainingArguments
import torch

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("retrain_pipeline")

# Config
DATABASE_URL = os.getenv("DATABASE_URL")
N_CHATS = int(os.getenv("RETRAIN_TRIGGER", 100))  # Retrain after N new chats
MODEL_PATH = os.getenv("MODEL_PATH", "./model")

# Connect to DB
engine = create_engine(DATABASE_URL)

def get_new_chats():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT id, user_message, bot_response FROM chat_logs
            WHERE retrained = false
            ORDER BY id ASC
            LIMIT :n
        """), {"n": N_CHATS})
        return result.fetchall()

def mark_chats_retrained(ids):
    with engine.connect() as conn:
        conn.execute(text("""
            UPDATE chat_logs SET retrained = true WHERE id = ANY(:ids)
        """), {"ids": ids})
        conn.commit()

def prepare_data(rows):
    # Simple binary classification: user_message -> bot_response intent
    texts = [r[1] for r in rows]
    labels = [0 for _ in rows]  # Placeholder: replace with real label extraction
    return texts, labels

def main():
    while True:
        logger.info("Checking for new chats...")
        rows = get_new_chats()
        if len(rows) < N_CHATS:
            logger.info(f"Not enough new chats ({len(rows)}/{N_CHATS}), sleeping...")
            time.sleep(60)
            continue
        logger.info(f"Retraining on {len(rows)} new chats...")
        texts, labels = prepare_data(rows)
        tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
        model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')
        # Tokenize
        encodings = tokenizer(texts, truncation=True, padding=True, return_tensors='pt')
        dataset = torch.utils.data.TensorDataset(encodings['input_ids'], torch.tensor(labels))
        # Training
        training_args = TrainingArguments(
            output_dir=MODEL_PATH,
            num_train_epochs=1,
            per_device_train_batch_size=8,
            logging_steps=10,
            save_steps=10,
            save_total_limit=1,
            remove_unused_columns=False,
        )
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=dataset,
        )
        trainer.train()
        model.save_pretrained(MODEL_PATH)
        logger.info(f"Model saved to {MODEL_PATH}")
        mark_chats_retrained([r[0] for r in rows])
        logger.info("Marked chats as retrained.")
        time.sleep(60)

if __name__ == "__main__":
    main() 