from stripe_integration import StripeIntegration, PaymentStatus

def test_charge_user():
    stripe_integration = StripeIntegration("api_key")
    assert stripe_integration.charge_user("user_id", 10.99)

def test_store_payment_status():
    stripe_integration = StripeIntegration("api_key")
    stripe_integration.store_payment_status("user_id", "success")
    assert stripe_integration.expose_payment_status_via_api("user_id").status == "success"

def test_expose_payment_status_via_api():
    stripe_integration = StripeIntegration("api_key")
    stripe_integration.store_payment_status("user_id", "success")
    payment_status = stripe_integration.expose_payment_status_via_api("user_id")
    assert payment_status.status == "success"
    assert payment_status.retry_count == 0

def test_retry_failed_payment():
    stripe_integration = StripeIntegration("api_key")
    stripe_integration.store_payment_status("user_id", "failed")
    stripe_integration.retry_failed_payment("user_id")
    payment_status = stripe_integration.expose_payment_status_via_api("user_id")
    assert payment_status.retry_count == 1
