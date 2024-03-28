import datetime

from database import DB
from models import Airport, Client, Package, Travel


DEFAULT_PACKET_CHARGE = 10


db = DB()


def get_daily_report(date: datetime.date) -> dict:
    packages = db.select(Package, filter_logic=lambda x: x.travel.date == date)
    report = {
        "date": str(date),
        "total_packages": 0,
        "total_collected": 0,
        "packages": [],
    }
    for pack in packages:
        report["total_packages"] += 1
        report["total_collected"] += getattr(pack, "price", DEFAULT_PACKET_CHARGE)
        report["packages"].append({
            "id": pack.id,
            "client_name": getattr(pack.client, "name", ""),
            "travel": pack.travel.id
        })

    return report


def post_client(**kwargs) -> bool:
    Client(name=kwargs.get("name", ""))
    return True


def post_airport(**kwargs) -> bool:
    Airport(name=kwargs.get("name", ""))
    return True


def post_travel(**kwargs) -> bool:
    try:
        origin = list(db.select(Airport, filter_logic=lambda x: x.name == kwargs.get("origin")))[0]
    except IndexError:
        return False

    try:
        destination = list(db.select(Airport, filter_logic=lambda x: x.name == kwargs.get("destination")))
    except IndexError:
        return False

    try:
        date = datetime.datetime.strptime(kwargs.get("date"), "%Y-%m-%d").date()
    except TypeError:
        return False

    Travel(
        origin=origin,
        destination=destination,
        date=date,
    )
    return True


def post_package(**kwargs) -> bool:
    try:
        travel = list(db.select(Airport, filter_logic=lambda x: x.id == kwargs.get("travel")))[0]
    except IndexError:
        return False

    try:
        client = list(db.select(Airport, filter_logic=lambda x: x.name == kwargs.get("client")))
    except IndexError:
        return False
    
    Package(client=client, travel=travel)
    return True
