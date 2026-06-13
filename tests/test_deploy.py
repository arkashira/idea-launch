import pytest
from deploy import deploy_to_github, trigger_render_build, trigger_heroku_build, get_public_url

def test_deploy_to_github():
    repo_url = "https://github.com/example/repo"
    code = "example code"
    assert deploy_to_github(repo_url, code) == True

def test_trigger_render_build():
    render_url = "https://render.com/example"
    assert trigger_render_build(render_url) == True

def test_trigger_heroku_build():
    heroku_url = "https://heroku.com/example"
    assert trigger_heroku_build(heroku_url) == True

def test_get_public_url():
    assert get_public_url() == "https://example.com"

def test_main():
    # Simulate command-line arguments
    import sys
    sys.argv = ["deploy.py", "--repo_url", "https://github.com/example/repo", "--render_url", "https://render.com/example", "--heroku_url", "https://heroku.com/example", "--code", "example code"]
    from deploy import main
    public_url = main()
    assert public_url == "https://example.com"
