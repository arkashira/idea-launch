import pytest
from src.templates import Template, TemplateCatalog, UIBuilder, BackendGenerator, create_template_catalog, select_template, auto_populate_ui_builder, auto_populate_backend_generator

def test_create_template_catalog():
    catalog = create_template_catalog()
    assert len(catalog.get_templates()) == 2

def test_select_template():
    catalog = create_template_catalog()
    template = select_template(catalog, "MVP1")
    assert template.name == "MVP1"

def test_auto_populate_ui_builder():
    ui_builder = UIBuilder()
    catalog = create_template_catalog()
    template = select_template(catalog, "MVP1")
    auto_populate_ui_builder(ui_builder, template)
    assert ui_builder.get_ui() == {
        "landing_page": "landing_page1",
        "user_auth": "user_auth1",
        "data_model": "data_model1"
    }

def test_auto_populate_backend_generator():
    backend_generator = BackendGenerator()
    catalog = create_template_catalog()
    template = select_template(catalog, "MVP1")
    auto_populate_backend_generator(backend_generator, template)
    assert backend_generator.get_backend() == {
        "landing_page": "landing_page1",
        "user_auth": "user_auth1",
        "data_model": "data_model1"
    }

def test_get_template_not_found():
    catalog = create_template_catalog()
    with pytest.raises(ValueError):
        select_template(catalog, "MVP3")
