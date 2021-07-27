import http.server

import socketserver


PORT = 1234

Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", PORT), Handler) as Httpd:
    print("serving at port", PORT)
    
    Httpd.serve_forever()