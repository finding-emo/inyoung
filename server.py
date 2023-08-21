# A simple HTTP server
# The default port is 9000.
# Usage: ``python3 server.py``

from http.server import HTTPServer, BaseHTTPRequestHandler
from json import dumps, loads

from extract_keywords import extract_keywords
from extract_emotions import extract_emotions
from extract_gestures import extract_gestures
from generate_prompt import generate_prompt

PORT = 9000


class ModelHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        request_body = self.rfile.read(int(self.headers["Content-Length"]))
        request_body = request_body.decode()
        request_body = loads(request_body)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        if self.path == "/keywords":
            text = request_body["text"]

            model_output = extract_keywords(text)
            response_body = {"keywords": model_output}

            self.wfile.write(dumps(response_body).encode())

        elif self.path == "/prompt":
            text = request_body["text"]
            translatedKeywords = request_body["translatedKeywords"]
            survey = request_body["survey"]

            emotions = extract_emotions(text)
            gestures = extract_gestures(text)

            (prompts, negativePrompt) = generate_prompt(
                keywords=translatedKeywords,
                emotions=emotions,
                gestures=gestures,
                type=survey["iconType"],
                mood=survey["iconMood"],
                color=survey["iconColor"],
            )
            response_body = {
                "prompts": prompts,
                "negativePrompt": negativePrompt,
            }

            self.wfile.write(dumps(response_body).encode())

        else:
            raise Exception("Invalid path")


with HTTPServer(("", PORT), ModelHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
