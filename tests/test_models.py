import unittest
import datetime

from database import DB
from models import (
    BaseModel,
    Client,
    Package,
    Travel,
)


class TestModels(unittest.TestCase):

    def test_base_model_fields_creation(self):
        fields = {
            "name": "Batman",
            "car": "Batmobile"
        }
        item = BaseModel(**fields)

        for f, v in fields.items():
            self.assertEqual(getattr(item, f), v) 

    def test_package_with_valid_fields(self):
        client = Client(name= "Joker")
        travel = Travel(date=datetime.date.today())
        package = Package(client=client, travel=travel)

        self.assertIsInstance(package, Package)
        self.assertIs(package.client, client)

    def test_package_with_no_client(self):
        with self.assertRaises(ValueError):
            package = Package()

    def test_package_with_invalid_client(self):
        with self.assertRaises(ValueError):
            package = Package(client="Robin")

    def test_package_with_no_travel(self):
        with self.assertRaises(ValueError):
            package = Package(client=Client())

    def test_model_is_added_to_db(self):
        db = DB()
        item_name = "I am Batman"
        new_item = BaseModel(name=item_name)

        item = list(db.select(BaseModel, filter_logic=lambda x: x.name == item_name))[0]

        self.assertIs(new_item, item)
