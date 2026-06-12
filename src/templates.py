import json
from dataclasses import dataclass

@dataclass
class Template:
    name: str
    landing_page: str
    user_auth: str
    data_model: str

class TemplateCatalog:
    def __init__(self):
        self.templates = []

    def add_template(self, template):
        self.templates.append(template)

    def get_template(self, name):
        for template in self.templates:
            if template.name == name:
                return template
        return None

    def to_json(self):
        return json.dumps([template.__dict__ for template in self.templates])

class UIBuilder:
    def __init__(self):
        self.ui = {}

    def auto_populate(self, template):
        self.ui['landing_page'] = template.landing_page
        self.ui['user_auth'] = template.user_auth
        self.ui['data_model'] = template.data_model

class BackendGenerator:
    def __init__(self):
        self.backend = {}

    def auto_populate(self, template):
        self.backend['landing_page'] = template.landing_page
        self.backend['user_auth'] = template.user_auth
        self.backend['data_model'] = template.data_model

def create_template(name, landing_page, user_auth, data_model):
    return Template(name, landing_page, user_auth, data_model)
