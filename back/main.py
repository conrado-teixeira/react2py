import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Pessoa():
    def __init__(self, url, name, company):
        self.url = url
        self.company = company
        self.name = name

    def to_json(self):
        return {
            "url" : self.url,
            "company" : self.company,
            "name" : self.name
        }

    pass



def buscar_vagas():
    pessoas = [
        Pessoa(url="http://www.google.com", company= "GuGu", name="Dev").to_json(),
        Pessoa(url="http://www.google.com", company= "Amazão", name="CTO").to_json(),
        Pessoa(url="http://www.google.com", company= "Feices", name="Stag").to_json()
    ]
    return pessoas

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/buscar_vagas':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "http://localhost:3000")  # Restrict to port 3000
            self.send_header("Access-Control-Allow-Methods", "GET")  # Allow GET
            self.end_headers()
            self.wfile.write(json.dumps(buscar_vagas()).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
