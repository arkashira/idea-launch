import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict

class PaymentStatus(Enum):
    SUCCESS = 1
    FAILED = 2

@dataclass
class Payment:
    amount: float
    currency: str
    payment_method: str

class PaymentGateway:
    def __init__(self):
        self.payments = {}

    def process_payment(self, payment: Payment) -> PaymentStatus:
        # Simulate payment processing
        if payment.amount > 0:
            self.payments[payment.payment_method] = payment
            return PaymentStatus.SUCCESS
        else:
            return PaymentStatus.FAILED

    def get_payment_status(self, payment_method: str) -> PaymentStatus:
        if payment_method in self.payments:
            return PaymentStatus.SUCCESS
        else:
            return PaymentStatus.FAILED

    def retry_payment(self, payment_method: str) -> PaymentStatus:
        if payment_method in self.payments:
            return self.process_payment(self.payments[payment_method])
        else:
            return PaymentStatus.FAILED

    def expose_payment_status_via_api(self, payment_method: str) -> Dict:
        payment_status = self.get_payment_status(payment_method)
        return {"payment_method": payment_method, "payment_status": payment_status.name}
