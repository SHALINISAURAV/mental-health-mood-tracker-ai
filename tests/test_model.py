from models.inference import predict_emotion


def test_prediction():

    text = "I feel very stressed today."

    predictions = predict_emotion(text)

    assert len(predictions) > 0