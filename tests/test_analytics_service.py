import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analytics_service import AnalyticsService, UserEngagementMetrics, Dashboard
import pytest

def test_update_metrics():
    analytics_service = AnalyticsService()
    data = {
        'active_users': 100,
        'session_duration': 10.5,
        'conversion_funnel': 0.8
    }
    analytics_service.update_metrics(data)
    assert analytics_service.metrics['active_users'] == 100
    assert analytics_service.metrics['session_duration'] == 10.5
    assert analytics_service.metrics['conversion_funnel'] == 0.8

def test_get_metrics():
    analytics_service = AnalyticsService()
    data = {
        'active_users': 100,
        'session_duration': 10.5,
        'conversion_funnel': 0.8
    }
    analytics_service.update_metrics(data)
    metrics = analytics_service.get_metrics()
    assert metrics.active_users == 100
    assert metrics.session_duration == 10.5
    assert metrics.conversion_funnel == 0.8

def test_pull_data():
    analytics_service = AnalyticsService()
    analytics_service.pull_data()
    assert analytics_service.metrics['active_users'] == 100
    assert analytics_service.metrics['session_duration'] == 10.5
    assert analytics_service.metrics['conversion_funnel'] == 0.8

def test_display_metrics():
    dashboard = Dashboard()
    metrics = dashboard.display_metrics()
    assert metrics['active_users'] == 100
    assert metrics['session_duration'] == 10.5
    assert metrics['conversion_funnel'] == 0.8
