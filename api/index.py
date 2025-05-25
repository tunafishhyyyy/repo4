# api/index.py
import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        import os

        # Parse query parameters
        query = parse_qs(urlparse(self.path).query)
        names = query.get('name', [])

        # Load marks data
        with open(os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')) as f:
            data = json.load(f)

        # Get marks for requested names
        marks = [data.get(name, None) for name in names]

        # Set CORS headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Respond with marks
        response = json.dumps({"marks": marks})
        self.wfile.write(response.encode())
