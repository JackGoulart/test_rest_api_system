from models.store import StoreModel
from models.item import ItemModel
from tests.base_test import BaseTest
import json


class TestStore(BaseTest):

    def test_create_store(self):
        with self.app() as cliente:
            with self.app_context():
                response = cliente.post('/store/Capivaras')
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('Capivaras'))
                self.assertDictEqual({"name": "Capivaras", "items": []}, json.loads(response.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/Capivaras')
                response = client.post('/store/Capivaras')
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': "A store with name 'Capivaras' already exists."},
                                     json.loads(response.data))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
               store = StoreModel('Capivaras')
               store.save_to_db()
               response = client.delete('/store/Capivaras')
               self.assertEqual(response.status_code, 200)
               self.assertDictEqual({'message':'Store deleted'}, json.loads(response.data))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/store/Capivaras')
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('Capivaras'))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/capivaras')
                response = client.get('/store/jujs')
                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'}, json.loads(response.data))

    def test_sotre_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/capivaras')
                item = ItemModel('mouse', 10.40, 1)
                item.save_to_db()
                response = client.get('/store/capivaras')
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({"name": "capivaras",
                                                  "items": [{"name": "mouse", "price": 10.40}]},
                                     json.loads(response.data))

    def test_store_list(self):
        with self.app() as client:
            client.post('/store/capivaras')
            client.post('/store/lunas')
            response = client.get('/stores')
            self.assertDictEqual({'stores': [{"name": "capivaras", "items": []},
                                             {"name": "lunas", "items": []}]},
                                 json.loads(response.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/capivaras')
                item_1 = ItemModel('mouse', 10.40, 1)
                item_1.save_to_db()
                client.post('/store/lunas')
                item_2 = ItemModel('fishsticker', 100.50, 2)
                item_2.save_to_db()
                response = client.get('/stores')

                self.assertDictEqual({'stores': [{"name": "capivaras",
                                                  "items": [{"name": "mouse", "price": 10.40}]},
                                                 {"name": "lunas",
                                                  "items": [{"name": "fishsticker", "price": 100.50}]}]},
                                     json.loads(response.data))
