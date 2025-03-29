import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proiect.settings')
django.setup()

import schedule

import logging
from django.core.mail import send_mail
from datetime import timedelta
from django.utils.timezone import now
from .models import CustomUser


logger = logging.getLogger('django')



def stergere_useri_noconfirmati():
    L = CustomUser.objects.filter(email_confirmat=False)
    L.delete()
    logger.info("Userii neconfirmati au fost stersi.")

def trimite_newsletter():
    users = CustomUser.objects.filter(email_confirmat=True, date_joined__lte=now() - timedelta(minutes=30))
    if users.exists():
        for user in users:
            send_mail(
                subject="Newsletterul de la magazinul online de carti X",
                message=f"{user.username} nu pierde ocazia sa citesti o carte!",
                from_email='djangoproiect@gmail.com',
                recipient_list=[user.email],
                fail_silently=False,
            )
            logger.info(f"Newsletter trimis catre {user.username} ({user.email}).")
    else:
        logger.info("Niciun utilizator eligibil pentru newsletter.")


def mesaj_de_rutina_zilnic():
    logger.info("Site-ul a avut activitate azi.")
    
def mesaj_de_rutina_spatamanal():
    logger.debug("Site-ul functioneaza corect.")

