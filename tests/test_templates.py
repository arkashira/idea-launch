import pytest
from src.templates import Template, TemplateCatalog, UIBuilder, BackendGenerator

def test_template_creation():
    template = Template("MVP", "Minimal Viable Product", "index.html", True, {"name": "str", "age": "int"})
    assert template.name == "MVP"
    assert template.description == "Minimal Viable Product"
    assert template.landing_page == "index.html"
    assert template.user_auth == True
    assert template.data_model == {"name": "str", "age": "int"}

def test_template_catalog():
    catalog = TemplateCatalog()
    template = Template("MVP", "Minimal Viable Product", "index.html", True, {"name": "str", "age": "int"})
    catalog.add_template(template)
    assert len(catalog.get_templates()) == 1
    assert catalog.get_template("MVP").name == "MVP"

def test_ui_builder():
    builder = UIBuilder()
    template = Template("MVP", "Minimal Viable Product", "index.html", True, {"name": "str", "age": "int"})
    builder.select_template(template)
    assert builder.auto_populate() == {
        "landing_page": "index.html",
        "user_auth": True,
        "data_model": {"name": "str", "age": "int"}
    }

def test_backend_generator():
    generator = BackendGenerator()
    template = Template("MVP", "Minimal Viable Product", "index.html", True, {"name": "str", "age": "int"})
    generator.select_template(template)
    assert generator.auto_populate() == {
        "landing_page": "index.html",
        "user_auth": True,
        "data_model": {"name": "str", "age": "int"}
    }

def test_template_catalog_edge_case():
    catalog = TemplateCatalog()
    assert catalog.get_template("Non-existent") is None
