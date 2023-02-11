import time
import schedule
import os
from win10toast import ToastNotifier
import re

def job():
    try:
        Download_path = r"C:\Users\prade\Downloads"
        files = os.listdir(Download_path)
        contents = [file for file in files if re.search(r'\.(png|jpg|jpeg|html|pdf)$', file, re.IGNORECASE)]

        for content in contents:
            os.remove(os.path.join(Download_path, content))
            toaster = ToastNotifier()
            toaster.show_toast("Alert",
                               f"{content} has been deleted successfully",
                               duration=10,
                               icon_path="trash2.ico")

        time.sleep(1)

    except Exception as error:
        pass


schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
