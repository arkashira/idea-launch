from payment_gateway import Payment, PaymentGateway, PaymentStatus

def test_process_payment_success():
    payment_gateway = PaymentGateway()
    payment = Payment(10.0, "USD", "credit_card")
    assert payment_gateway.process_payment(payment) == PaymentStatus.SUCCESS

def test_process_payment_failure():
    payment_gateway = PaymentGateway()
    payment = Payment(0.0, "USD", "credit_card")
    assert payment_gateway.process_payment(payment) == PaymentStatus.FAILED

def test_get_payment_status_success():
    payment_gateway = PaymentGateway()
    payment = Payment(10.0, "USD", "credit_card")
    payment_gateway.process_payment(payment)
    assert payment_gateway.get_payment_status("credit_card") == PaymentStatus.SUCCESS

def test_get_payment_status_failure():
    payment_gateway = PaymentGateway()
    assert payment_gateway.get_payment_status("credit_card") == PaymentStatus.FAILED

def test_retry_payment_success():
    payment_gateway = PaymentGateway()
    payment = Payment(10.0, "USD", "credit_card")
    payment_gateway.process_payment(payment)
    assert payment_gateway.retry_payment("credit_card") == PaymentStatus.SUCCESS

def test_retry_payment_failure():
    payment_gateway = PaymentGateway()
    assert payment_gateway.retry_payment("credit_card") == PaymentStatus.FAILED

def test_expose_payment_status_via_api():
    payment_gateway = PaymentGateway()
    payment = Payment(10.0, "USD", "credit_card")
    payment_gateway.process_payment(payment)
    expected_response = {"payment_method": "credit_card", "payment_status": "SUCCESS"}
    assert payment_gateway.expose_payment_status_via_api("credit_card") == expected_response
