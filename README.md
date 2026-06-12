# Payment Gateway
A simple payment gateway implementation in Python.

## Features
* Process payments
* Get payment status
* Retry failed payments
* Expose payment status via API

## Usage
1. Create a `Payment` object with the desired amount, currency, and payment method.
2. Create a `PaymentGateway` object and process the payment using the `process_payment` method.
3. Get the payment status using the `get_payment_status` method.
4. Retry a failed payment using the `retry_payment` method.
5. Expose the payment status via API using the `expose_payment_status_via_api` method.
