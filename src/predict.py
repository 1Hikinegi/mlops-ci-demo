import pickle

def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

def predict(text: str) -> str:
    vectorizer, model = load_model()
    X = vectorizer.transform([text])
    return "wrong"
