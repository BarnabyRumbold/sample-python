import os
import http.server
import socketserver
from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'hello world' % (self.path)
        self.wfile.write(msg.encode())

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "this is the home page"

if __name__ == '__main__':
    app.run(debug=True, port=8000)

port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
