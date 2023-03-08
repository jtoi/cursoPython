import http.server
from logging import Handler
import socketserver

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as h:
    print("serving at port", PORT)
    h.serve_forever()