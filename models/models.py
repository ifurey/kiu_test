from datetime import date

from database import DB


db_session = DB()


class BaseModel():
    """Base model class. Any new instance is directly added to the DB.
    """
    id: int

    def __init__(self, **kwargs) -> None:
        for field, value in kwargs.items():
            setattr(self, field, value)
        db_session.add(self)


class Client(BaseModel):
    """Model for clients"""
    name: str


class Airport(BaseModel):
    """Model for Airports"""
    name: str


class Travel(BaseModel):
    """Model for Travel"""
    origin: Airport
    destination: Airport
    date: date


class Package(BaseModel):
    """Model for Package"""
    client: Client
    travel: Travel

    def __init__(self, **kwargs) -> None:
        client = kwargs.get("client")
        if not type(client) is Client or getattr(client, 'id', None) is None:
            raise ValueError("Invalid client for package.")
        super().__init__(**kwargs)
