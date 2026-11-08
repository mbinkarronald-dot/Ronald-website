import os 
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = """
        <html>
        <body style="font-family:Arial; text-align:center; margin-top:50px;">
            <h1>THE AMBASSADOR</h1>
            <h2>Server Running from Ronald.py - No Data Needed!</h2>
            <form method="POST">
                <input name="name" placeholder="name" style="padding:10px; margin:5px;"<br></br>
                <input name="matricule" placeholder="Matricule" style="padding:10px; margin:5px;"><br></br>
                <input name="password" type="password" placeholder="Password" style="padding:10px; margin:5px;"><br></br>
                <button style="padding:10px 20px; background:green; color:white;">Login</button>
            </form>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

    def do_POST(self):
        self.do_GET()

# Start server
print("Starting server on http://0.0.0.0:8000")
print("Open that link in your browser")
HTTPServer(("0.0.0.0", 8000), MyHandler).serve_forever()