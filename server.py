# A simple HTTP server
# The default port is 9000.
# Usage: ``python3 server.py``

from http.server import HTTPServer, BaseHTTPRequestHandler
from json import dumps, loads

from models import model

PORT = 9000


class ModelHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        request_body = self.rfile.read(int(self.headers["Content-Length"]))
        request_body = request_body.decode()
        request_body = loads(request_body)

        prompt = request_body["prompt"]

        model_output = model(prompt)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(dumps(model_output).encode())


with HTTPServer(("", PORT), ModelHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
