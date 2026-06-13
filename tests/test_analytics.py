from analytics import UserEngagement, AnalyticsDashboard, WebSocket
import pytest

def test_user_engagement():
    user_engagement = UserEngagement(active_users=10, session_duration=30, conversion_funnels=[0.5, 0.7])
    assert user_engagement.active_users == 10
    assert user_engagement.session_duration == 30
    assert user_engagement.conversion_funnels == [0.5, 0.7]

def test_analytics_dashboard():
    dashboard = AnalyticsDashboard()
    user_engagement = UserEngagement(active_users=10, session_duration=30, conversion_funnels=[0.5, 0.7])
    dashboard.update_data(user_engagement)
    data = dashboard.get_data()
    assert data["active_users"] == 10
    assert data["session_duration"] == 30
    assert data["conversion_funnels"] == [0.5, 0.7]

def test_websocket():
    websocket = WebSocket()
    user_engagement = UserEngagement(active_users=10, session_duration=30, conversion_funnels=[0.5, 0.7])
    websocket.send_data(user_engagement)
    data = websocket.get_data()
    assert data["active_users"] == 10
    assert data["session_duration"] == 30
    assert data["conversion_funnels"] == [0.5, 0.7]

def test_export_to_csv():
    websocket = WebSocket()
    user_engagement = UserEngagement(active_users=10, session_duration=30, conversion_funnels=[0.5, 0.7])
    websocket.send_data(user_engagement)
    csv_data = websocket.export_to_csv()
    assert csv_data.startswith("active_users,session_duration,conversion_funnels,last_updated")
    assert str(user_engagement.active_users) in csv_data
    assert str(user_engagement.session_duration) in csv_data
    assert str(user_engagement.conversion_funnels) in csv_data

def test_edge_case_empty_data():
    dashboard = AnalyticsDashboard()
    data = dashboard.get_data()
    assert data == {}

def test_edge_case_none_user_engagement():
    websocket = WebSocket()
    websocket.send_data(None)
    data = websocket.get_data()
    assert data == {}
