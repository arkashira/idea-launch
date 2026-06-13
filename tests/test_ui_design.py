import pytest
from ui_design import UIDesign

def test_ui_design_to_json():
    ui_design = UIDesign(components=['component1', 'component2'])
    json_str = ui_design.to_json()
    assert json_str == '{"components": ["component1", "component2"]}'

def test_ui_design_from_json():
    json_str = '{"components": ["component1", "component2"]}'
    ui_design = UIDesign.from_json(json_str)
    assert ui_design.components == ['component1', 'component2']
