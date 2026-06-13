from billing import BillingSystem, UsageData

def test_update_usage():
    billing_system = BillingSystem()
    billing_system.update_usage(10, 100)
    assert billing_system.get_usage_data().active_users == 10
    assert billing_system.get_usage_data().request_volume == 100
    assert billing_system.get_usage_data().estimated_monthly_cost == 30.0

def test_calculate_estimated_monthly_cost():
    billing_system = BillingSystem()
    billing_system.update_usage(0, 1000)
    assert billing_system.get_usage_data().estimated_monthly_cost == 300.0

def test_get_usage_data():
    billing_system = BillingSystem()
    billing_system.update_usage(10, 100)
    usage_data = billing_system.get_usage_data()
    assert isinstance(usage_data, UsageData)
    assert usage_data.active_users == 10
    assert usage_data.request_volume == 100
    assert usage_data.estimated_monthly_cost == 30.0

def test_check_warning():
    billing_system = BillingSystem()
    billing_system.update_usage(0, 5001)
    assert billing_system.check_warning() == True

def test_check_no_warning():
    billing_system = BillingSystem()
    billing_system.update_usage(0, 5000)
    assert billing_system.check_warning() == True
