from fastapi.testclient import TestClient
from backend.main import app

def test_health():
    with TestClient(app) as client:
        r=client.get('/api/health'); assert r.status_code==200 and r.json()['status']=='healthy'
def test_dashboard():
    with TestClient(app) as client:
        r=client.get('/api/dashboard'); assert r.status_code==200 and 'total_applicants' in r.json()
def test_metrics():
    with TestClient(app) as client:
        r=client.get('/api/model-metrics'); assert r.status_code==200 and 'selected_model' in r.json()
