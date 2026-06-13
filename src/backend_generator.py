import json
from ui_design import generate_backend, generate_database_models

def generate_nodejs_express_backend(ui_design):
    backend_code = ''
    backend_code += 'const express = require("express");\n'
    backend_code += 'const app = express();\n'
    endpoints = generate_backend(ui_design)
    for endpoint in endpoints:
        backend_code += f'app.{endpoint["method"].lower()}("{endpoint["path"]}", {endpoint["handler"]});\n'
    return backend_code

def generate_database_models_code(ui_design):
    models_code = ''
    models = generate_database_models(ui_design)
    for model in models:
        models_code += f'const {model["name"]} = {{\n'
        models_code += '  id: { type: Number, required: true },\n'
        models_code += '  name: { type: String, required: true }\n'
        models_code += '};\n'
    return models_code
