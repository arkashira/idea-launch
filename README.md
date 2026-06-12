# Stripe Integration
This project provides a basic implementation of Stripe integration for payment processing.

## Features
* One-click checkout and subscription plans
* Payment status stored in the backend and exposed via API
* Failed payments trigger a retry workflow

## Usage
1. Install the project using `poetry install`
2. Run the project using `python src/stripe_integration.py --api-key <api_key> --user-id <user_id> --amount <amount>`
3. Test the project using `pytest tests/test_stripe_integration.py`
