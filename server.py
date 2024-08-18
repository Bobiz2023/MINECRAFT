import subprocess

server_status = "متوقف"

def start_server():
    global server_status
    subprocess.Popen(['screen', '-dmS', 'mcbedrock', './bedrock_server'], cwd='/bedrock')
    server_status = "نشط"

def stop_server():
    global server_status
    subprocess.run(['screen', '-S', 'mcbedrock', '-X', 'quit'])
    server_status = "متوقف"

def restart_server():
    stop_server()
    start_server()

def get_server_status():
    return server_status
