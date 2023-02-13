from app import Calculator
import app


def test_myapp():
    data = Calculator(10, 20)
    data = data.multi()
    var_a = app.a.multi()
    assert data is 200
    assert type(data) is int
    assert var_a is 200
    assert type(var_a) is int
