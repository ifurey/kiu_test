from typing import Callable
from collections.abc import Iterable

from models import BaseModel

class InMemDB():
    def __init__(self) -> None:
        self.data = {}

    def add(self, item: BaseModel) -> None:
        """Adds a single item to a table based on the item class.

        Args:
            item: Item to add
        """
        model = type(item)
        try:
            item.id = len(self.data.get(model, []))
        except AttributeError as e:
            raise ValueError(f"Invalid Model type: {model}")
        self.data[model] = self.data.get(model, [])
        self.data[model].append(item)

    def select(self, table: type, filter_logic: Callable = lambda x: True) -> Iterable:
        """
        Select items from a specific table

        Args:
            table: Model class that defines the db table.
            filter_logic: Function to filter the result. Default is True.
        Returns:
            Iterable with filtered entries in the table.
        """
        return filter(filter_logic, self.data.get(table, []))
