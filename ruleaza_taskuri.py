import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proiect.settings')
django.setup()

import schedule
import time


import sys
from aplicatie import tasks



def run_scheduler():
    schedule.every(2).minutes.do(tasks.stergere_useri_noconfirmati)
    schedule.every().sunday.at("12:20").do(tasks.trimite_newsletter)
    schedule.every(5).minutes.do(tasks.mesaj_de_rutina_zilnic)
    schedule.every().sunday.at("12:21").do(tasks.mesaj_de_rutina_spatamanal)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    try:
        run_scheduler()
    except KeyboardInterrupt:
        print("Scheduler oprit manual.")
        sys.exit()
