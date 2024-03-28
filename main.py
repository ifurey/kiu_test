from http.server import HTTPServer

from database import DB
from server import KIUServer
from utils import DATA_DATES, populate_db_with_dummy_data


hostName = "localhost"
serverPort = 8080


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