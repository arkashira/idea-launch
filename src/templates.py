import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Template:
    name: str
    description: str
    landing_page: str
    user_auth: bool
    data_model: Dict[str, str]

class TemplateCatalog:
    def __init__(self):
        self.templates = []

    def add_template(self, template: Template):
        self.templates.append(template)

    def get_templates(self):
        return self.templates

    def get_template(self, name: str):
        for template in self.templates:
            if template.name == name:
                return template
        return None

class UIBuilder:
    def __init__(self):
        self.template = None

    def select_template(self, template: Template):
        self.template = template

    def auto_populate(self):
        if self.template:
            return {
                "landing_page": self.template.landing_page,
                "user_auth": self.template.user_auth,
                "data_model": self.template.data_model
            }
        return None

class BackendGenerator:
    def __init__(self):
        self.template = None

    def select_template(self, template: Template):
        self.template = template

    def auto_populate(self):
        if self.template:
            return {
                "landing_page": self.template.landing_page,
                "user_auth": self.template.user_auth,
                "data_model": self.template.data_model
            }
        return None
