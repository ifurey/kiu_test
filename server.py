import datetime
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from kiu import get_daily_report
from kiu.constants import POST_RUTES_MAPPING


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
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(get_daily_report(date)), "utf-8"))
    
    def do_POST(self):
        print(f"PATH  --  {self.path}")
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)
        if POST_RUTES_MAPPING[self.path](**data):
            self.send_response(HTTPStatus.CREATED)
        else:
            self.send_response(HTTPStatus.BAD_REQUEST)
        self.end_headers()

