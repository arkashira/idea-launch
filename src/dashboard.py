import json
from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class DemoButton:
    url: str
    label: str = "Live Demo"

    def to_dict(self):
        return {"url": self.url, "label": self.label}

    @classmethod
    def from_dict(cls, data):
        return cls(url=data["url"], label=data["label"])

def get_demo_button(deployment_url):
    return DemoButton(url=deployment_url)

def get_styled_button(button):
    # For simplicity, assume styling is just adding a CSS class
    return f'<a href="{button.url}" target="_blank" class="btn btn-primary">{button.label}</a>'

def refresh_demo_url(button, new_deployment_url):
    return DemoButton(url=new_deployment_url, label=button.label)
