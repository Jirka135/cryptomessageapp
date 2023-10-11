import hashlib
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import create_salt
from flask import Flask, render_template, request, redirect, url_for
from webpage import webpage

#sul = create_salt.generate_salt()
#print(sul)

app = Flask(__name__)

app.register_blueprint(webpage,url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)