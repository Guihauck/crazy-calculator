from .calculator_4 import Calculator4
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

class MockHandler:
    def average(self, numbers: List[float]) -> float:
        return 4
    
def test_calculate_average():
    mock_request = MockRequest({"numbers": [14.5,4.0,6.0,4.5]})
    driver = NumpyHandler()
    calculator_4 = Calculator4(driver)
    formated_response = calculator_4.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'calculator': 4, 'value': 7.25, 'success': True}}
    