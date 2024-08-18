from flask import Flask, render_template, jsonify
from flask_basicauth import BasicAuth
import server
import subprocess

app = Flask(__name__)

# إعدادات المصادقة
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
basic_auth = BasicAuth(app)

# جلب عنوان IP العام باستخدام curl
def get_public_ip():
    public_ip = subprocess.check_output(['curl', 'ifconfig.me']).decode('utf-8').strip()
    return public_ip

@app.route('/')
@basic_auth.required
def index():
    return render_template('index.html', status=server.get_server_status(), ip_address=get_public_ip())

@app.route('/start')
@basic_auth.required
def start():
    server.start_server()
    return jsonify({'status': 'تم تشغيل السيرفر'})

@app.route('/stop')
@basic_auth.required
def stop():
    server.stop_server()
    return jsonify({'status': 'تم إيقاف السيرفر'})

@app.route('/restart')
@basic_auth.required
def restart():
    server.restart_server()
    return jsonify({'status': 'تم إعادة تشغيل السيرفر'})

@app.route('/status')
@basic_auth.required
def status():
    return jsonify({'status': server.get_server_status()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
