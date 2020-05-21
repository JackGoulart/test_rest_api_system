from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest


class TestStore(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('UpIt')
        self.assertEqual(store.name,
                         'UpIt',
                         'The name of store {} does not equal the constructor argument.'.format(store.name))
        # So I added these two tests further dow to try it on
        self.assertIsNotNone(store)
        self.assertIsInstance(store, StoreModel, f'The obj does not longer is instance of the {StoreModel}')