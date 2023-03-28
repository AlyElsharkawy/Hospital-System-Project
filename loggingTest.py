import logging
import time
timeInstance = time.localtime()
current_time = time.strftime("%d-%m-%Y", timeInstance)
logging.basicConfig(filename=f" {current_time} Patient Flow.txt", filemode="w", level=logging.INFO, format= "%(message)s")
def appendLog(inputMessage):
    logging.info(inputMessage)
for i in range(50):
    appendLog(f"Hello x {i}")