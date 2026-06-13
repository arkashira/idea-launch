import pytest
from billing import BillingSystem, UsageData

def test_update_usage_data():
    billing_system = BillingSystem()
    billing_system.update_usage_data(10, 100)
    assert billing_system.usage_data.active_users == 10
    assert billing_system.usage_data.api_calls == 100
    assert billing_system.usage_data.estimated_monthly_cost == 30.0

def test_calculate_estimated_monthly_cost():
    billing_system = BillingSystem()
    estimated_cost = billing_system.calculate_estimated_monthly_cost(100)
    assert estimated_cost == 30.0

def test_get_dashboard_data():
    billing_system = BillingSystem()
    billing_system.update_usage_data(10, 100)
    dashboard_data = billing_system.get_dashboard_data()
    assert dashboard_data["active_users"] == 10
    assert dashboard_data["api_calls"] == 100
    assert dashboard_data["estimated_monthly_cost"] == 30.0

def test_check_warning_threshold():
    billing_system = BillingSystem()
    billing_system.update_usage_data(10, 5000)
    assert billing_system.check_warning_threshold() == True

def test_integrate_with_stripe():
    billing_system = BillingSystem()
    billing_system.integrate_with_stripe()
    assert billing_system.stripe_integration == True
