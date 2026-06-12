import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Template:
    name: str
    landing_page: str
    user_auth: str
    data_model: str

class TemplateCatalog:
    def __init__(self):
        self.templates = []

    def add_template(self, template: Template):
        self.templates.append(template)

    def get_templates(self) -> List[Template]:
        return self.templates

    def get_template(self, name: str) -> Template:
        for template in self.templates:
            if template.name == name:
                return template
        raise ValueError(f"Template {name} not found")

class UIBuilder:
    def __init__(self):
        self.ui = {}

    def populate(self, template: Template):
        self.ui = {
            "landing_page": template.landing_page,
            "user_auth": template.user_auth,
            "data_model": template.data_model
        }

    def get_ui(self) -> Dict:
        return self.ui

class BackendGenerator:
    def __init__(self):
        self.backend = {}

    def populate(self, template: Template):
        self.backend = {
            "landing_page": template.landing_page,
            "user_auth": template.user_auth,
            "data_model": template.data_model
        }

    def get_backend(self) -> Dict:
        return self.backend

def create_template_catalog() -> TemplateCatalog:
    catalog = TemplateCatalog()
    catalog.add_template(Template("MVP1", "landing_page1", "user_auth1", "data_model1"))
    catalog.add_template(Template("MVP2", "landing_page2", "user_auth2", "data_model2"))
    return catalog

def select_template(catalog: TemplateCatalog, name: str) -> Template:
    return catalog.get_template(name)

def auto_populate_ui_builder(ui_builder: UIBuilder, template: Template):
    ui_builder.populate(template)

def auto_populate_backend_generator(backend_generator: BackendGenerator, template: Template):
    backend_generator.populate(template)
