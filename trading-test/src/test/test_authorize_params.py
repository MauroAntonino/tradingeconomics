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
                    'url': {"type" : "string"}
                },
                "required": [ "url" ]
            }
    return validate(
                    instance=data,
                    schema=schema
                    )

class TestAuthorize(TestCase):
    def setUp(self) -> None:
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'email'
        }
        self.url = "http://0.0.0.0:8000/v1/authorize_params"
        self.connection = redis.Redis(host="localhost", port=6379, db=0, password="password")
        tkns = [{   
                        "redirect_url": "http://0.0.0.0:8000/redirect/92932d7c-8d07-4c46-a3e3-3894ac8f0544/", 
                        "provider_name": Provider.MELHOR_ENVIO,
                        "client_id": "3010",
                        "client_secret": "bBmPUh8DaqWk1VBnNiQRkv0WzL2pEmBXCkZI4BM5",
                        "access_token": "XXXXX",
                        "expiration_date": "XXXXX",
                        "generation_date": "XXXXX",
                        "refresh_token": "def50200cdde97e8834aa980bee80f7d1767f81bbff831ce904ce418c855e0b92e547d353c4d0d13780c40d11a93e47eb18f7e31b08963b7040c712bc41fba2cc0e7d17ae8a283cfaf4c1f52afe9e74b98efd448709a21190d2273fa55e8801d4a6cc0aa389716535358b4f245c38e8d7b44c1f4afdcf3fc207ecce66cf4bbad9908666116ac6e662cb4c3aab1644100c2dc77fcba8ac8a223780b594ccf196856d3eeccfd7f1b9e2ef6ad1f1909c29c66570cff28c3cb3507b63cffbe8a923aecbd38c600e9869c8d249c66585c256b4598f61329e0e062a6ffd1366c17a5678d07e84b5b9fb795d81891b6bf2b1d1cbd6d3deee6be500f0532cd1f3862e934dc5ce13929818a7cdabad49356254c7dc198b45bcb8d2f79577296b3c6583743244348a1c42e497b2192c3da6573bbbc8598d358c9949e95b5d94b98976fe146758e80c8c1dc1bf441dfc08e48f11f4d25a82d8ac847dc88da694d685a4d17b815ab5af2455a6d76fc6a16f0260e8f144b692f269c7dea7e84e0f7821a8d2fc029414995623490c05168c7d0ae45948c39c9cec5097a1ef23a58600f21ea30b001b85d56b97b9bb0bc9ff2938628a4718dd772bb1e53cee05d929005b442c032a82d8486e9e14cb3051613f944f7c12aa397f20764c7ecf4c6f85ffd87d19e735a2921d683b46ab8f4374beb3dab5031d0fc9d598bfbc794e12e2c324dc2b802b80fe57af0d070499322ec2cea31a05b1ceb76fb39ac34852071356c3480b41a5fceec5f8d2950a1decb9d39c18905f696d669b1548bf1eb16cdfa33e7e3a62dcf05fc0914b7c845e596c3a9bf72d2081034b0e4fa707d354508db1e35bc0dc95745b91661be812408e1b52527e6ae72778487f8605668b891d1b30784400fd987521ebbd683144bd38d894b0fe349e1993792cc8487141f2f9225e52a2f5114fe4df05d0d0e1fa0d624164623f18d82aa5960bde4861eba89594ee0a9b97b5f6ad4b175e2bcaa905c05722f9658fa4508539385ce00c38b2ab9ff3362f398c34f363e5f2d4dbf30f28613d10eca276daf199700d0030cf1e04430c0c8419d1e793aa54cb5e03bbe4d79583a989ec218fafdea08a97ab6e30aaace870810b45b10bfc4a240ffc3be33"
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
    
    def test_authorize(self):
        payload = {
            "store_code": "store_code", 
            "client_id": "3010 ", 
            "client_secret":  "bBmPUh8DaqWk1VBnNiQRkv0WzL2pEmBXCkZI4BM5",
            "provider_name": "melhorenvio"
        }
        params = {
        }
        response = requests.request("POST", self.url, headers=self.headers, json=payload, params=params)
        resp = response.json()
        validate_response(resp)
        self.assertEqual(100, 100)
    
    def test_wrong_store_authorize(self):
        payload = {
            "store_code": "store_code_wrong", 
            "client_id": "3010 ", 
            "client_secret":  "bBmPUh8DaqWk1VBnNiQRkv0WzL2pEmBXCkZI4BM5",
            "provider_name": "melhorenvio"
        }
        params = {
        }
        response = requests.request("POST", self.url, headers=self.headers, json=payload, params=params)
        if response.status_code == 400:
            self.assertEqual(100, 100)
            return
        self.assertEqual(0, 100)
    
    def test_wrong_provider(self):
        payload = {
            "store_code": "store_code", 
            "client_id": "3010 ", 
            "client_secret":  "bBmPUh8DaqWk1VBnNiQRkv0WzL2pEmBXCkZI4BM5",
            "provider_name": "melhorenvio_wrong"
        }
        params = {
        }
        response = requests.request("POST", self.url, headers=self.headers, json=payload, params=params)
        if response.status_code == 400:
            self.assertEqual(100, 100)
            return
        self.assertEqual(0, 100)


def suite():
    suite = TestSuite()
    suite.addTest(TestAuthorize('test_authorize'))
    suite.addTest(TestAuthorize('test_wrong_store_authorize'))
    suite.addTest(TestAuthorize('test_wrong_provider'))
    return suite