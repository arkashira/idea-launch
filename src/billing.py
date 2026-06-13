import json
from dataclasses import dataclass
from datetime import datetime, timedelta
import argparse

@dataclass
class UsageData:
    active_users: int
    api_calls: int
    estimated_monthly_cost: float

class BillingSystem:
    def __init__(self):
        self.usage_data = UsageData(0, 0, 0.0)
        self.warning_threshold = 50.0
        self.stripe_integration = False

    def update_usage_data(self, active_users, api_calls):
        self.usage_data.active_users = active_users
        self.usage_data.api_calls = api_calls
        self.usage_data.estimated_monthly_cost = self.calculate_estimated_monthly_cost(api_calls)

    def calculate_estimated_monthly_cost(self, api_calls):
        # Assume $0.01 per API call
        return api_calls * 0.01 * 30

    def get_dashboard_data(self):
        return {
            "active_users": self.usage_data.active_users,
            "api_calls": self.usage_data.api_calls,
            "estimated_monthly_cost": self.usage_data.estimated_monthly_cost
        }

    def check_warning_threshold(self):
        return self.usage_data.estimated_monthly_cost > self.warning_threshold

    def integrate_with_stripe(self):
        self.stripe_integration = True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--active-users", type=int, default=0)
    parser.add_argument("--api-calls", type=int, default=0)
    args = parser.parse_args()

    billing_system = BillingSystem()
    billing_system.update_usage_data(args.active_users, args.api_calls)
    dashboard_data = billing_system.get_dashboard_data()
    print(json.dumps(dashboard_data))

    if billing_system.check_warning_threshold():
        print("Warning: Projected cost exceeds $50")

if __name__ == "__main__":
    main()
