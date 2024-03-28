import datetime

from models import (
    Airport,
    Client,
    Package,
    Travel,
)
from database import DB


DATE1 = datetime.date(2024, 1, 8)
DATE2 = datetime.date(2024, 2, 15)
DATE3 = datetime.date(2024, 3, 17)

DATA_DATES = [
    DATE1,
    DATE2,
    DATE3,
]


def populate_db_with_dummy_data():
    db = DB()
    c1 = Client(name="One")
    c2 = Client(name="Two")
    c3 = Client(name="Three")

    a1 = Airport(name="North Airport")
    a2 = Airport(name="South Airport")


    t1 = Travel(origin=a1, destination=a2, date=DATE1)
    t2 = Travel(origin=a1, destination=a2, date=DATE1)
    t3 = Travel(origin=a1, destination=a2, date=DATE2)
    t4 = Travel(origin=a2, destination=a1, date=DATE3)

    # Date 1
    Package(client=c1, travel=t1)            
    Package(client=c1, travel=t1)
    Package(client=c1, travel=t2)
    Package(client=c2, travel=t1)
    Package(client=c2, travel=t2)
    Package(client=c2, travel=t2)
    Package(client=c3, travel=t1)
    Package(client=c3, travel=t1)
    Package(client=c3, travel=t2)
    Package(client=c1, travel=t1)
    Package(client=c1, travel=t2)
    Package(client=c1, travel=t1)

    # Date 2
    Package(client=c1, travel=t3)
    Package(client=c1, travel=t3)
    Package(client=c1, travel=t3)
    Package(client=c2, travel=t3)
    Package(client=c2, travel=t3)
    Package(client=c3, travel=t3)

    # Date 3
    Package(client=c2, travel=t4)
    Package(client=c2, travel=t4)
    Package(client=c1, travel=t4)