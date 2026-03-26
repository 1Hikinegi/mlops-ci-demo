from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

data = [
    ("payment failed", "payment"),
    ("refund not received", "refund"),
    ("app crashing", "bug"),
    ("cannot login", "auth"),
]

texts, labels = zip(*data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Model trained and saved!")