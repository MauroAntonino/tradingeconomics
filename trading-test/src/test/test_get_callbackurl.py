from unittest import TestCase, TestSuite
from unittest.mock import patch
import requests
from jsonschema import validate
import redis
import pickle
# from app.domain.entity.token import Provider

def validate_response(data):
    schema = { 
                'type' : 'object',
                'properties' : {
                    'url': {"type" : "string"},
                    'provider': {"type" : "string"},
                },
                "required": [ "url", "provider" ]
            }
    return validate(
                    instance=data,
                    schema=schema
                    )

class TestGetCallback(TestCase):
    def setUp(self) -> None:
        self.url = "http://0.0.0.0:8000/v1/get_url"
        self.connection = redis.Redis(host="localhost", port=6379, db=0, password="password")
        tkns = [{   
                        "redirect_url": "redirect_url", 
                        "provider_name": Provider.MELHOR_ENVIO,
                        "client_id": "XXXXX",
                        "client_secret": "XXXXX",
                        "access_token": "XXXXX",
                        "expiration_date": "XXXXX",
                        "generation_date": "XXXXX",
                        "refresh_token": "XXXXX"
                    }]
        store = {
            "id_code": "store_code",
            "tokens": tkns
        }
        self.connection.set("store_code", pickle.dumps(store))
        return
    
    def tearDown(self):
        self.connection.delete("store_code")
        return 

    def test_get_callbackurl(self):
        params = {
            "store_code": "store_code",
            "provider_name": "melhorenvio"
        }
        payload = {
        }
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'email'
        }
        response = requests.request("GET", self.url, headers=headers, data=payload, params=params)
        resp = response.json()
        validate_response(resp)
        self.assertEqual(100, 100)
    
    def test_get_callbackurl_2(self):
        params = {
            "store_code": "store_code",
            "provider_name": "melhorenvio"
        }
        payload = {
        }
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'email'
        }
        response = requests.request("GET", self.url, headers=headers, data=payload, params=params)
        resp = response.json()
        validate_response(resp)
        self.assertEqual(100, 100)
    
    def test_get_callbackurl_wrong_provider(self):
        params = {
            "store_code": "store_code",
            "provider_name": "melhorenvio_errado"
        }
        payload = {
        }
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'email'
        }
        response = requests.request("GET", self.url, headers=headers, data=payload, params=params)
        if response.status_code == 400:
            self.assertEqual(100, 100)
            return
        self.assertEqual(0, 100)

def suite():
    suite = TestSuite()
    suite.addTest(TestGetCallback('test_get_callbackurl_2'))
    suite.addTest(TestGetCallback('test_get_callbackurl'))
    suite.addTest(TestGetCallback('test_get_callbackurl_wrong_provider'))
    return suite