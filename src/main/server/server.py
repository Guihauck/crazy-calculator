from flask import Flask
from src.main.routes.calculators import calc_route_bp

app = Flask(__name__) #App objeto de servidor de Flask

app.register_blueprint(calc_route_bp)