from .calculator_2 import Calculator2
from typing import Dict

class MockRequest:
    def __init__(self, body: dict):
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [12.08,60.80]})
    calculator_2 = Calculator2()
    calculator_2.calculate(mock_request)