from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from pyDes import des, ECB
import json
import os

# Enkripsi atau Dekripsi menggunakan kunci
def des_encrypt(plaintext, key):
    k = des(key, ECB)
    encrypted_data = k.encrypt(plaintext, padmode=2)
    return encrypted_data.hex()

def des_decrypt(ciphertext, key):
    k = des(key, ECB)
    decrypted_data = k.decrypt(bytes.fromhex(ciphertext), padmode=2)
    return decrypted_data.decode()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Mengirimkan halaman HTML untuk input
        try:
            with open('index.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
        except IOError:
            self.send_error(404, "File not found.")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode())

        mode = data['mode'][0].strip().lower()
        text = data['text'][0].strip()
        key = data['key'][0].strip()

        # Validasi kunci
        if len(key) != 8:
            result = "Kunci harus 8 karakter."
        else:
            if mode == 'encrypt':
                result = des_encrypt(text, key)
            elif mode == 'decrypt':
                try:
                    result = des_decrypt(text, key)
                except Exception as e:
                    result = f"Kesalahan dalam dekripsi: {str(e)}"
            else:
                result = "Mode tidak valid. Gunakan 'encrypt' atau 'decrypt'."

        # Mengirimkan hasil kembali ke browser dalam format JSON
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"result": result}).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print("Server berjalan di http://localhost:8080")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
