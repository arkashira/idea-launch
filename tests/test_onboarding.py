import pytest
from onboarding import Onboarding, WalkthroughStep

@pytest.fixture
def i18n_file():
    return 'tests/i18n.json'

def test_get_walkthrough(i18n_file):
    onboarding = Onboarding(i18n_file)
    walkthrough = onboarding.get_walkthrough()
    assert len(walkthrough) == 3
    assert walkthrough[0].description == "Idea Capture"
    assert walkthrough[1].description == "Spec Review"
    assert walkthrough[2].description == "Launch"

def test_get_tooltip(i18n_file):
    onboarding = Onboarding(i18n_file)
    tooltip = onboarding.get_tooltip(0)
    assert tooltip == "Example idea capture tooltip"

def test_get_tooltip_out_of_range(i18n_file):
    onboarding = Onboarding(i18n_file)
    tooltip = onboarding.get_tooltip(3)
    assert tooltip is None

def test_skip_walkthrough(i18n_file):
    onboarding = Onboarding(i18n_file)
    result = onboarding.skip_walkthrough()
    assert result == "Walkthrough skipped"

def test_replay_walkthrough(i18n_file):
    onboarding = Onboarding(i18n_file)
    result = onboarding.replay_walkthrough()
    assert result == "Walkthrough replayed"
