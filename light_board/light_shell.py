from flask import Flask, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route("/test")
def hello():
    return "Hello World!"

@app.route("/light_board/<text>", methods=['GET'])
def exec(text):
    light_shell(text)
    return ""

def light_shell(text):
    command = f"sudo ./rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-no-hardware-pulse --led-rows=16 --led-cols=32 -s 4 -f ./rpi-rgb-led-matrix/fonts/helvR12.bdf -C 102,179,22 {text}"
    print('A')
    # completed = subprocess.run(command, shell=True) # commandがコマンド、argumentが引数。必要なだけ並べる。

# light_shell('Hello World')
app.run()
