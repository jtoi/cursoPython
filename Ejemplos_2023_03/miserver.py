import http.server
from logging import Handler
import socketserver

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as h:
    print("serving at port", PORT)
    http.server.serve_forever()