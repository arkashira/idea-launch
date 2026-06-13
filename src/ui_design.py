import json
from dataclasses import dataclass

@dataclass
class UIDesign:
    components: list

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(components=data['components'])

def generate_backend(ui_design):
    # Simplified example, real implementation would require more complex logic
    endpoints = []
    for component in ui_design.components:
        endpoint = {
            'method': 'GET',
            'path': f'/{component}',
            'handler': f'handle_{component}'
        }
        endpoints.append(endpoint)
    return endpoints

def generate_database_models(ui_design):
    # Simplified example, real implementation would require more complex logic
    models = []
    for component in ui_design.components:
        model = {
            'name': component,
            'fields': ['id', 'name']
        }
        models.append(model)
    return models
