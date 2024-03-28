from datetime import date as date_cls

from database import DB


db_session = DB()


class BaseModel():
    """Base model class. Any new instance is directly added to the DB.
    """
    id: int

    def __init__(self, **kwargs) -> None:
        self.validators(**kwargs)
        for field, value in kwargs.items():
            setattr(self, field, value)
        db_session.add(self)

    def validators(self, **kwargs) -> None:
        """Method to implement model validators
        Should raise an exception if something is wrong."""
        pass


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
    date: date_cls = date_cls.today()


class Package(BaseModel):
    """Model for Package"""
    client: Client
    travel: Travel

    def validators(self, **kwargs) -> None:
        client = kwargs.get("client")
        travel = kwargs.get("travel")
        if not type(client) is Client or not db_session.exist(client):
            raise ValueError("Invalid client for package.")
        if not type(travel) is Travel or not db_session.exist(travel):
            raise ValueError("Invalid travel for package.")
