from templates import Template, TemplateCatalog, UIBuilder, BackendGenerator, create_template

def test_template_creation():
    template = create_template('MVP', 'landing_page.html', 'user_auth.py', 'data_model.json')
    assert template.name == 'MVP'
    assert template.landing_page == 'landing_page.html'
    assert template.user_auth == 'user_auth.py'
    assert template.data_model == 'data_model.json'

def test_template_catalog():
    catalog = TemplateCatalog()
    template = create_template('MVP', 'landing_page.html', 'user_auth.py', 'data_model.json')
    catalog.add_template(template)
    assert catalog.get_template('MVP') == template

def test_ui_builder():
    builder = UIBuilder()
    template = create_template('MVP', 'landing_page.html', 'user_auth.py', 'data_model.json')
    builder.auto_populate(template)
    assert builder.ui['landing_page'] == 'landing_page.html'
    assert builder.ui['user_auth'] == 'user_auth.py'
    assert builder.ui['data_model'] == 'data_model.json'

def test_backend_generator():
    generator = BackendGenerator()
    template = create_template('MVP', 'landing_page.html', 'user_auth.py', 'data_model.json')
    generator.auto_populate(template)
    assert generator.backend['landing_page'] == 'landing_page.html'
    assert generator.backend['user_auth'] == 'user_auth.py'
    assert generator.backend['data_model'] == 'data_model.json'
