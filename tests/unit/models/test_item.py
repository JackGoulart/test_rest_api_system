from unittest import TestCase
from models.item import ItemModel
from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest
# The way to run this test via cli is the followed command.
# $ python -m unittest discover test/


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        store = StoreModel('It4you')
        item = ItemModel('Mouse', 5,1)
        # first arg value, second arg value expected and third arg is custom message just in case of error.
        self.assertEqual(item.name, 'Mouse',
                         "The name of the item after creation  does not equal  the constructor argument.")
        self.assertEqual(item.price, 5,
                         "The value of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)


    def test_item_json(self):
        item = ItemModel('Mouse', 5, 1)

        expected = {
            'name': 'Mouse',
            'price': 5
        }

        self.assertEqual(item.json(), expected,
                         "The JSON export of the item is incorrect. Received {}, expected {}".format(item.json(), expected))