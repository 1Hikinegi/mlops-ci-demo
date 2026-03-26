# MLOps CI Demo Project

## What this project shows:
- ML model training
- Prediction pipeline
- Automated testing
- GitHub Actions CI

## How to run locally:
pip install -r requirements.txt
python src/train.py
python main.py

## CI:
Every push triggers:
- Install dependencies
- Train model
- Run tests