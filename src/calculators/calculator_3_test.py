from typing import Dict, List
from pytest import raises
from src.calculators.calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3

class MockHandler:
    def variance(self, numbers: List[float]) -> float:
        return 100000

def test_calculate_with_variance_error():
    mockrequest = MockRequest({ "numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockHandlerError())

    with raises(Exception) as exinfo:
        calculator_3.calculate(mockrequest)

    assert str(exinfo.value) == "Process failure: Variance less than multiplication"

def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockHandler())

    response = calculator_3.calculate(mock_request)

    assert response == {'data': {'calculator': 3, 'value': 100000, 'success': True}}
