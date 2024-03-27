import unittest

from database import InMemDB
from models import BaseModel


class MockModel(BaseModel):
    pass

class TestInMemDB(unittest.TestCase):

    def _populate_db(self, amount: int = 2):
        """Creates a DB an populate it with "amount" mock objects
        """
        db = InMemDB()
        for n in range(amount):
            db.add(MockModel())
        return db

    def test_add(self):
        db = InMemDB()
        mocked_item = MockModel()
        db.add(mocked_item)

        self.assertEqual(db.data, {MockModel: [mocked_item]})
        self.assertEqual(mocked_item.id, 0)

    def test_add_invalid_model(self):
        db = InMemDB()
        with self.assertRaises(ValueError):
            db.add(1)

    def test_select_all(self):
        db = self._populate_db()
        mocked_items = list(db.select(MockModel))
        self.assertEqual(mocked_items, db.data[MockModel])

    def test_select_unexisting_table(self):
        db = self._populate_db()
        ut = list(db.select(object))
        self.assertEqual(ut, [])

    def test_select_filtered(self):
        db = self._populate_db(amount=4)
        mocked_items = list(db.select(MockModel, filter_logic=lambda x: x.id > 1))
        self.assertEqual(mocked_items, db.data[MockModel][2:])
 