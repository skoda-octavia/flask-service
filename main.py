import functools
import socket
import subprocess
from flask import Flask, render_template


app = Flask(__name__)

@functools.lru_cache(maxsize=1)
def get_ip():
    output = subprocess.check_output(["ip", "-o", "route", "get", "1.1.1.1"],
                                     universal_newlines=True)
    return output.strip().split(" ")[-1]

@app.route('/')
def home():
    return render_template('index.html', hostname=socket.gethostname(), ip=get_ip()), 200, {'Content-Type': 'text/html'}

@app.route('/health')
def health_check():
    return "OK\n"

@app.route('/echo/<int:number>')
def echo_number(number):
    fake_num = 0
    for _ in range(number):
        fake_num += 1
        fake_num -= 1
    return f"Ok!\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
