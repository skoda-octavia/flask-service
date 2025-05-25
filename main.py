from flask import Flask
import os

app = Flask(__name__)

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