import json
from dataclasses import dataclass
from datetime import datetime, timedelta
import argparse

@dataclass
class UsageData:
    active_users: int
    request_volume: int
    estimated_monthly_cost: float

class BillingSystem:
    def __init__(self):
        self.usage_data = UsageData(0, 0, 0.0)
        self.warning_threshold = 50.0

    def update_usage(self, active_users, request_volume):
        self.usage_data.active_users = active_users
        self.usage_data.request_volume = request_volume
        self.usage_data.estimated_monthly_cost = self.calculate_estimated_monthly_cost()

    def calculate_estimated_monthly_cost(self):
        # For simplicity, assume the cost is $0.01 per request
        return self.usage_data.request_volume * 0.01 * 30

    def get_usage_data(self):
        return self.usage_data

    def check_warning(self):
        return self.usage_data.estimated_monthly_cost >= self.warning_threshold

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--active-users', type=int, default=0)
        parser.add_argument('--request-volume', type=int, default=0)
        args = parser.parse_args()
        billing_system = BillingSystem()
        billing_system.update_usage(args.active_users, args.request_volume)
        print("Active Users:", billing_system.get_usage_data().active_users)
        print("Request Volume:", billing_system.get_usage_data().request_volume)
        print("Estimated Monthly Cost: $", billing_system.get_usage_data().estimated_monthly_cost)
        if billing_system.check_warning():
            print("Warning: Projected cost exceeds $50")

if __name__ == "__main__":
    billing_system = BillingSystem()
    billing_system.main()
