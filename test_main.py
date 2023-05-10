from fastapi.testclient import TestClient

from main import app
from datetime import date
import requests
client = TestClient(app)


def test_get_today_uf():
    """Test get uf value for today date"""
    response = client.get(f"/uf/{date.today()}")
    assert response.status_code == 200
    assert response.json()['value'] > 0


def test_get_2012_uf():
    """test get the value of the uf for a date less than 2013"""
    response = client.get(f"/uf/{date(2012,12,1)}")
   
    assert response.status_code == 422
    assert "detail" in response.json() 

def test_get_uf_without_date():
    
    response = client.get("/uf/")
   
    assert response.status_code == 404
    assert "detail" in response.json() 


def test_get_today_uf_sii_error(mocker):
    """test to get the uf value when request to sii.cl fails"""
    mocker.patch("db.db_uf.get_uf", return_value=None)
    mocked_response = requests.Response()
    mocked_response.status_code = 404
    mocker.patch.object(requests,'get').return_value = mocked_response 
    response = client.get(f"/uf/{date.today()}")
    assert response.status_code == 404
    assert 'found' in  response.json().get("detail")


def test_get_today_uf_changed_html(mocker):
    """test to get the value of the uf when the html structure of the response has changed"""
    mocker.patch("db.db_uf.get_uf", return_value=None)
    mocked_response = requests.Response()
    mocked_response.status_code = 200
    mocked_response._content = '<div id="mes_all"></div>'.encode('utf-8')
    mocker.patch.object(requests,'get').return_value = mocked_response 
    response = client.get(f"/uf/{date.today()}")
    assert response.status_code == 500
    assert'extract' in  response.json().get("detail")

def test_get_future_uf_value(mocker):
    """test to get the value of the uf for a date 2 months from now"""
    mocker.patch("db.db_uf.get_uf", return_value=None)
    uf_date = date.today()
    uf_date = uf_date.replace(day=uf_date.day+2,month=uf_date.month + 1)
    response = client.get(f"/uf/{uf_date}")
    assert response.status_code == 404
   