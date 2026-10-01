import os
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
STATIC_ROOT = PROJECT_ROOT / "static"


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path in ("/", "/index.html"):
            self.serve_static("index.html", "text/html; charset=utf-8")
            return
        self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def serve_static(self, filename: str, content_type: str) -> None:
        path = (STATIC_ROOT / filename).resolve()
        if path.parent != STATIC_ROOT or not path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND, "Static file not found")
            return

        body = path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:
        print(f"{self.address_string()} - {format % args}")


def main() -> None:
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    print(f"WAV analyser listening on http://{host}:{port}")
    ThreadingHTTPServer((host, port), RequestHandler).serve_forever()


if __name__ == "__main__":
    main()
