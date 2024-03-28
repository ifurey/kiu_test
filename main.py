import datetime
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from database import DB
from kiu import get_daily_report
from utils import DATA_DATES, populate_db_with_dummy_data


hostName = "localhost"
serverPort = 8080


class KIUServer(BaseHTTPRequestHandler):
    def do_GET(self):
        qs = parse_qs(urlparse(self.path).query)
        try:
            date = datetime.date(
                int(qs.get('year')[0]),
                int(qs.get('month')[0]),
                int(qs.get('day')[0]),
            )
        except TypeError:
            date = datetime.date.today()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(get_daily_report(date)), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), KIUServer)
    db = DB()
    populate_db_with_dummy_data()
    print("Data base populated with dummy data, existing dates:")
    for d in DATA_DATES:
        print(f"\t* {d}")
    print('\n')
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")