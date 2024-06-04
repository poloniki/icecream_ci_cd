from icecream.predict import predict_sales


def test_return_type():
    assert isinstance(predict_sales(10, 20), int), "The return type is not the int"


def test_common_sense():
    assert predict_sales(10, 20) >= 0, "The sales can not be negative"
