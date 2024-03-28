import unittest
import datetime

import models
from database import DB
from kiu import get_daily_report


class TestDailyReport(unittest.TestCase):

    def _populate_db(self) -> tuple:
        """Populates the database with some clients, airports, travel and packages
        
        Return:
            Tuple with a date and a list of packages for that date
        """
        db = DB()
        c1 = models.Client(name="Batman")
        c2 = models.Client(name="Robin")

        a1 = models.Airport(name="Gotham City Airport")
        a2 = models.Airport(name="Metropolis City Airport")

        date1 = datetime.date(2024, 2, 15)
        date2 = datetime.date(2024, 3, 17)

        t1 = models.Travel(origin=a1, destination=a2, date=date1)
        t2 = models.Travel(origin=a1, destination=a2, date=date1)
        t3 = models.Travel(origin=a1, destination=a2, date=date2)

        date1_packages = [
            models.Package(client=c1, travel=t1),            
            models.Package(client=c1, travel=t2),
            models.Package(client=c2, travel=t1),
            models.Package(client=c2, travel=t2),
        ]

        models.Package(client=c1, travel=t3)
        models.Package(client=c2, travel=t3)
        models.Package(client=c1, travel=t3)

        return date1, date1_packages
    
    def test_daily_report(self):
        date, expected_packages = self._populate_db()

        expected_report = {
            "date": str(date),
            "total_packages": len(expected_packages),
            "total_collected": len(expected_packages) * 10,
            "packages": [{
                    "id": pack.id,
                    "client_name": pack.client.name,
                    "travel": pack.travel.id
                } for pack in expected_packages]
        }

        daily_report = get_daily_report(date)

        self.assertDictEqual(daily_report, expected_report)
