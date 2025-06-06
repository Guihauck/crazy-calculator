from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, drive_handler: DriverHandlerInterface) -> None:
        self.__drive_handler = drive_handler

    def calculate(self, request:FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        formated_result = self.__format_response(calculated_number)
        return formated_result

    def __validate_body(self, body:Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("poorly formed body")
        
        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__drive_handler.standard_deviation(first_process_result)
        return 1/result
    
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "calculator": 2,
                "result": round(calculated_number, 2)
            }
        }