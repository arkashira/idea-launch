import json
import argparse
from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentStatus:
    status: str
    retry_count: int

class StripeIntegration:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.payment_status = {}

    def charge_user(self, user_id: str, amount: float) -> bool:
        # Simulate Stripe API call
        print(f"Charging user {user_id} ${amount}")
        return True

    def store_payment_status(self, user_id: str, status: str) -> None:
        self.payment_status[user_id] = PaymentStatus(status, 0)

    def expose_payment_status_via_api(self, user_id: str) -> Optional[PaymentStatus]:
        return self.payment_status.get(user_id)

    def retry_failed_payment(self, user_id: str) -> None:
        if user_id in self.payment_status:
            payment_status = self.payment_status[user_id]
            payment_status.retry_count += 1
            self.payment_status[user_id] = payment_status
            print(f"Retrying payment for user {user_id}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", required=True)
    parser.add_argument("--user-id", required=True)
    parser.add_argument("--amount", type=float, required=True)
    args = parser.parse_args()

    stripe_integration = StripeIntegration(args.api_key)
    if stripe_integration.charge_user(args.user_id, args.amount):
        stripe_integration.store_payment_status(args.user_id, "success")
    else:
        stripe_integration.store_payment_status(args.user_id, "failed")
        stripe_integration.retry_failed_payment(args.user_id)

    payment_status = stripe_integration.expose_payment_status_via_api(args.user_id)
    if payment_status:
        print(f"Payment status for user {args.user_id}: {payment_status.status}")

if __name__ == "__main__":
    main()
