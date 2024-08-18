from flask import Flask, render_template, jsonify
import server
import subprocess

app = Flask(__name__)

# جلب عنوان IP العام باستخدام curl
def get_public_ip():
    public_ip = subprocess.check_output(['curl', 'ifconfig.me']).decode('utf-8').strip()
    return public_ip

@app.route('/')
def index():
    return render_template('index.html', status=server.get_server_status(), ip_address=get_public_ip())

@app.route('/start')
def start():
    server.start_server()
    return jsonify({'status': 'تم تشغيل السيرفر'})

@app.route('/stop')
def stop():
    server.stop_server()
    return jsonify({'status': 'تم إيقاف السيرفر'})

@app.route('/restart')
def restart():
    server.restart_server()
    return jsonify({'status': 'تم إعادة تشغيل السيرفر'})

@app.route('/status')
def status():
    return jsonify({'status': server.get_server_status()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
