import joblib

with open('dataset.pkl', 'rb') as file:
    df = joblib.load(file)
print(type(df))