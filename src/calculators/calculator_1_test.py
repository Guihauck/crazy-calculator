from .calculator_1 import Calculator1
from typing import Dict
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculator():
    mock_request = MockRequest(body={ "number": 1 })
    calculator_1 = Calculator1()
    response = calculator_1.calculate(mock_request)

    # Response format
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]

    # Assertiveness of the response
    assert response["data"]["calculator"] == 1
    assert response["data"]["result"] == 14.25

def test_calculate_with_body_error():
    mock_request = MockRequest(body={ "something": 1 })
    calculator_1 = Calculator1()

    with raises(Exception) as excepinfo:
        calculator_1.calculate(mock_request)
    assert str(excepinfo.value) == "body mal formatado!"
   