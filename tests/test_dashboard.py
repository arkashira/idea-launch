from src.dashboard import DemoButton, get_demo_button, get_styled_button, refresh_demo_url
import pytest

def test_demo_button():
    url = "https://example.com/demo"
    button = DemoButton(url)
    assert button.url == url
    assert button.label == "Live Demo"

def test_get_demo_button():
    deployment_url = "https://example.com/deployment"
    button = get_demo_button(deployment_url)
    assert button.url == deployment_url

def test_get_styled_button():
    button = DemoButton("https://example.com/demo")
    styled_button = get_styled_button(button)
    assert styled_button.startswith('<a href="https://example.com/demo"')

def test_refresh_demo_url():
    button = DemoButton("https://example.com/old-deployment")
    new_deployment_url = "https://example.com/new-deployment"
    refreshed_button = refresh_demo_url(button, new_deployment_url)
    assert refreshed_button.url == new_deployment_url
