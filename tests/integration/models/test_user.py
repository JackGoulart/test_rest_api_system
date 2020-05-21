from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('jack', '1234')

            self.assertIsNone(user.find_by_username('jack'))
            self.assertIsNone(user.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(user.find_by_username('jack'))
            self.assertIsNotNone(user.find_by_id(1))