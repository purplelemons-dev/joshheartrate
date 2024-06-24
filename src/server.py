from http.server import BaseHTTPRequestHandler, HTTPServer
from utils import ext_to_mime


class Handler(BaseHTTPRequestHandler):

    def _200(self, content: str):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(content.encode())

    def do_GET(self):
        path = self.path
        if not path.startswith("/api"):
            if path == "/":
                path = "/index.html"
            with open(f"public{path}") as f:
                self.send_response(200)
                self.send_header("Content-type", ext_to_mime(path.split(".")[-1]))
                self.end_headers()
                if path.split(".")[-1] in ["html", "css", "js", "txt"]:
                    self.wfile.write(f.read().encode())
                else:
                    self.wfile.write(f.read())
        
        # api call here


def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ("127.0.0.1", 10024)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
