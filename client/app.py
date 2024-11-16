import http.server
import socketserver

PORT = 7000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"[INFO] Running on http://localhost:{PORT}")
    httpd.serve_forever()
