from tests.base_test import BaseTest
from models.store import StoreModel
from models.item import ItemModel
'''
    In order of database interaction 
    it needs to use app_context() functionality
'''

class TestStore(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('UpIt')
        self.assertListEqual(store.items.all(), [],
                             "The store's items length was not 0 even though no items were add.")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('Tupfly')

            self.assertIsNone(StoreModel.find_by_name('Tupfly'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('Tupfly'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('Tupfly'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Uptofly')
            item = ItemModel('pear of wings', 150, 1)

            store.save_to_db()
            item.save_to_db()
            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'pear of wings')

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('Uptofly')
            item = ItemModel('pear of wings', 150.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                "name": "Uptofly",
                "items": [{"name": "pear of wings", "price": 150.99}]
            }

            self.assertDictEqual(store.json(), expected, "my own msg if I want to")
