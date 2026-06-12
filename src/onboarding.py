import json
from dataclasses import dataclass

@dataclass
class WalkthroughStep:
    description: str
    tooltip: str

class Onboarding:
    def __init__(self, i18n_file):
        with open(i18n_file, 'r') as f:
            self.i18n_data = json.load(f)
        self.steps = [
            WalkthroughStep(self.i18n_data['idea_capture']['description'], self.i18n_data['idea_capture']['tooltip']),
            WalkthroughStep(self.i18n_data['spec_review']['description'], self.i18n_data['spec_review']['tooltip']),
            WalkthroughStep(self.i18n_data['launch']['description'], self.i18n_data['launch']['tooltip']),
        ]

    def get_walkthrough(self):
        return self.steps

    def get_tooltip(self, step_index):
        if step_index < len(self.steps):
            return self.steps[step_index].tooltip
        return None

    def skip_walkthrough(self):
        return "Walkthrough skipped"

    def replay_walkthrough(self):
        return "Walkthrough replayed"
