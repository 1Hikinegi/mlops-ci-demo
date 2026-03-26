from src.predict import predict

def test_prediction():
    result = predict("payment failed")
    assert result in ["payment", "refund", "bug", "auth"]