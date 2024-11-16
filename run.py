import os
import sys
import time
import multiprocessing
import subprocess

def run_server():
    os.chdir("server")
    os.system("python app.py")

def run_client():
    os.chdir("client")
    os.system("python app.py")   

def run_server():
    os.chdir("API")  # Cambia al directorio 'server' donde está 'app.py'
    result = subprocess.run(["python", "app.py"])

    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    print("[INFO] Starting Server")
    server = multiprocessing.Process(target=run_server)
    client = multiprocessing.Process(target=run_client)
    print("[INFO] Starting Server and Client")
    server.start()
    print("[INFO] Waiting for Server to start")
    time.sleep(1.5)
    print("[INFO] Starting Client")
    client.start()
    try:
        server.join()
        client.join()
    except KeyboardInterrupt:
        print("[INFO] Keyboard Interrupted. Terminating Server and Client")
        server.terminate()
        client.terminate()
        sys.exit(1)