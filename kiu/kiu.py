from datetime import date

from database import DB
from models import Package, Travel
from .constants import DEFAULT_PACKET_CHARGE


db = DB()


def get_daily_report(date: date) -> dict:
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