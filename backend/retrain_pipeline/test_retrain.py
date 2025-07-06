import pytest
import retrain
from unittest.mock import patch, MagicMock

def test_prepare_data():
    rows = [(1, "hello", "hi"), (2, "bye", "goodbye")]
    texts, labels = retrain.prepare_data(rows)
    assert texts == ["hello", "bye"]
    assert labels == [0, 0]

@patch("retrain.get_new_chats")
@patch("retrain.mark_chats_retrained")
@patch("retrain.DistilBertTokenizer.from_pretrained")
@patch("retrain.DistilBertForSequenceClassification.from_pretrained")
@patch("retrain.Trainer")
def test_main_loop(mock_trainer, mock_model, mock_tokenizer, mock_mark, mock_get):
    # Setup
    mock_get.return_value = [(1, "hi", "hello")] * 100
    mock_trainer.return_value.train.return_value = None
    mock_trainer.return_value.save_model = MagicMock()
    with patch("time.sleep", return_value=None):
        with patch("builtins.print"):
            with pytest.raises(StopIteration):
                # Stop after one loop
                next(iter([retrain.main()])) 