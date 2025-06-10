from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validade_body(body)
        average = self.__calculate_average(input_data)
        formated_response = self.__format_response(average)
        
        return formated_response

    def __validade_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpBadRequestError("poorly formed body")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_average(self, numbers: List[float]) -> float:
        average = self.__driver_handler.average(numbers)
        return average
    
    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "calculator": 4,
                "value": float(round(average,2)),
                "success": True
            }
        }