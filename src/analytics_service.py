import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class UserEngagementMetrics:
    active_users: int
    session_duration: float
    conversion_funnel: float

class AnalyticsService:
    def __init__(self):
        self.metrics = {
            'active_users': 0,
            'session_duration': 0.0,
            'conversion_funnel': 0.0
        }

    def update_metrics(self, data):
        self.metrics['active_users'] += data['active_users']
        self.metrics['session_duration'] += data['session_duration']
        self.metrics['conversion_funnel'] += data['conversion_funnel']

    def get_metrics(self):
        return UserEngagementMetrics(
            active_users=self.metrics['active_users'],
            session_duration=self.metrics['session_duration'],
            conversion_funnel=self.metrics['conversion_funnel']
        )

    def pull_data(self):
        # Simulate pulling data from a built-in analytics service
        data = {
            'active_users': 100,
            'session_duration': 10.5,
            'conversion_funnel': 0.8
        }
        self.update_metrics(data)

class Dashboard:
    def __init__(self):
        self.analytics_service = AnalyticsService()

    def display_metrics(self):
        self.analytics_service.pull_data()
        metrics = self.analytics_service.get_metrics()
        return {
            'active_users': metrics.active_users,
            'session_duration': metrics.session_duration,
            'conversion_funnel': metrics.conversion_funnel
        }

if __name__ == "__main__":
    dashboard = Dashboard()
    metrics = dashboard.display_metrics()
    print(metrics)
