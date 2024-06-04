from fastapi import FastAPI
from icecream.predict import predict_sales

app = FastAPI()


@app.get("/")
def root():
    return {"greeting": "Hellow world!!!!!"}


@app.get("/predict")
def predict_api(temp: int, num_people: int):
    prediction = predict_sales(int(temp), int(num_people))

    return {"prediction": prediction}
