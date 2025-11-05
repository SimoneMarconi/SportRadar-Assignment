import os
import subprocess
import threading
import platform
import sys

# THIS IS THE SCRIPT TO RUN THE WHOLE APPLICATION

def startFrontend():
    frontendPath = os.getcwd() + "/frontend"
    print("Frontend Started")
    subprocess.run(
        ["npm", "run", "dev"], text=True, stdout=sys.stdout, cwd=frontendPath
    )

def startBackend():
    backendPath = os.getcwd() + "/backend"
    print("Backend Started")
    subprocess.run(
        ["flask", "--app", "app", "run"], stdout=sys.stdout, text=True, cwd=backendPath
    )

backThread = threading.Thread(target=startBackend)
frontThread = threading.Thread(target=startFrontend)

backThread.start()
frontThread.start()

backThread.join()
frontThread.join()

