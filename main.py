from src.predict import predict

if __name__ == "__main__":
    text = input("Enter your issue: ")
    result = predict(text)
    print(f"Predicted category: {result}")