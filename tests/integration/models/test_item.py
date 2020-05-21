from models.store import StoreModel
from tests.base_test import BaseTest
from models.item import ItemModel
# Jack to take care with the names of functions test
# Take for instance assertIsNone and assertIsNotNone
# Remember for each method there is a opposite as well


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db()
            item = ItemModel('mouse', 5, 1)

            self.assertIsNone(ItemModel.find_by_name('t'),
                              f'Found an item with name {item.name}, but expected not.')

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('mouse'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('mouse'))

    def test_store_relationship(self): # test relationship between item and store
        with self.app_context():
            store = StoreModel('Ikea')
            item = ItemModel('mouse', 5, 1)
            store.save_to_db()
            item.save_to_db()
            self.assertEqual(item.store.name, 'Ikea')