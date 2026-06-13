import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class UserEngagement:
    active_users: int
    session_duration: int
    conversion_funnels: List[float]

class AnalyticsDashboard:
    def __init__(self):
        self.data = {}

    def update_data(self, user_engagement: UserEngagement):
        if user_engagement is not None:
            self.data = {
                "active_users": user_engagement.active_users,
                "session_duration": user_engagement.session_duration,
                "conversion_funnels": user_engagement.conversion_funnels,
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            self.data = {}

    def get_data(self):
        return self.data

    def export_to_csv(self):
        if self.data:
            csv_data = "active_users,session_duration,conversion_funnels,last_updated\n"
            csv_data += f"{self.data['active_users']},{self.data['session_duration']},{self.data['conversion_funnels']},{self.data['last_updated']}"
            return csv_data
        else:
            return ""

class WebSocket:
    def __init__(self):
        self.dashboard = AnalyticsDashboard()

    def send_data(self, user_engagement: UserEngagement):
        self.dashboard.update_data(user_engagement)

    def get_data(self):
        return self.dashboard.get_data()

    def export_to_csv(self):
        return self.dashboard.export_to_csv()
