from notebook import notebookapp
import os
import time

os.system("jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --allow-root &")

time.sleep(5)
servers = list(notebookapp.list_running_servers())
print("servers", servers)