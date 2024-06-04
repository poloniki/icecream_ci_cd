def predict_sales(temp: int, num_people: int) -> int:
    prediction = 10 + temp * 0.3 + num_people * 0.2
    return int(prediction)


if __name__ == "__main__":
    print(predict_sales(temp=10, num_people=20))
