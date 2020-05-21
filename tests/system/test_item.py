from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel
from tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel('jackson', '1234').save_to_db()
                auth_request = client.post('/auth',
                                           data=json.dumps({'username': 'jackson', 'password': '1234'}),
                                           headers={"Content-Type": "application/json"})

                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = f'JWT {auth_token}'



    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/item/test')
                self.assertEqual(response.status_code, 401)

    def test_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/item/test', headers={'Authorization':self.access_token})
                self.assertEqual(response.status_code, 404)

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('kabanas').save_to_db()
                ItemModel('mouse', 12.31, 1).save_to_db()
                response = client.get('/item/mouse', headers={'Authorization': self.access_token})
                self.assertEqual(200, response.status_code)

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('kabanas').save_to_db()
                ItemModel('mouse', 12.31, 1).save_to_db()
                response = client.delete('/item/mouse')
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({"message":"Item deleted"},
                                     json.loads(response.data))
    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('kabanas').save_to_db()
                response = client.post('/item/mouse', data={'price':22.10,'store_id':1}, headers= {'Authorization' : self.access_token})
                self.assertEqual(response.status_code, 201)

    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('kabanas').save_to_db()
                ItemModel('mouse',22.10,1).save_to_db()
                response = client.post('/item/mouse', data={'price': 22.10, 'store_id': 1}, headers={'Authorization':self.access_token})
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': "An item with name 'mouse' already exists."},
                                     json.loads(response.data))

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('kabanas').save_to_db()
                response = client.put('/item/mouse',
                                      data=json.dumps({
                                                       'price':22.10,
                                                       'store_id':1}),
                                      headers={"Content-Type": "application/json",
                                               'Authorization':self.access_token})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('mouse').price, 22.10)
                self.assertDictEqual({'name':'mouse', 'price':22.10},
                                     json.loads(response.data))

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('kabanas').save_to_db()
                ItemModel('mouse',18.00, 1).save_to_db()
                self.assertEqual(ItemModel.find_by_name('mouse').price, 18.00)
                response = client.put('/item/mouse',
                                      data=json.dumps({
                                                       'price':22.10,
                                                       'store_id':1}),
                                      headers={"Content-Type": "application/json",
                                               'Authorization':self.access_token})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('mouse').price, 22.10)
                self.assertDictEqual({'name':'mouse', 'price':22.10},
                                     json.loads(response.data))

    def test_list_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('ka').save_to_db()
                ItemModel('mouse', 22.22, 1).save_to_db()
                ItemModel('charger', 200.22, 1).save_to_db()
                response = client.get('/items')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'items': [{'name':'mouse', 'price':22.22},
                                                {'name':'charger', 'price':200.22}]},
                                                 json.loads(response.data))


