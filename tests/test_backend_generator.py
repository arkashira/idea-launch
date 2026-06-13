import pytest
from backend_generator import generate_nodejs_express_backend, generate_database_models_code
from ui_design import UIDesign

def test_generate_nodejs_express_backend():
    ui_design = UIDesign(components=['component1', 'component2'])
    backend_code = generate_nodejs_express_backend(ui_design)
    assert 'app.get("/component1", handle_component1);' in backend_code
    assert 'app.get("/component2", handle_component2);' in backend_code

def test_generate_database_models_code():
    ui_design = UIDesign(components=['component1', 'component2'])
    models_code = generate_database_models_code(ui_design)
    assert 'const component1 = {' in models_code
    assert 'const component2 = {' in models_code
