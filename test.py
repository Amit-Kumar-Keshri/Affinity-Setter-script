import psutil
import psutil as p
# importing os module
import os
import time

def process_id(process_name):
    pid = None

    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            time.sleep(30)
            print("Pid:", pid)
            return pid

pid_got = process_id('audiodg')


p = psutil.Process(pid_got)
p.cpu_affinity([0])

