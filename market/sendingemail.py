from rest_framework.views import *
from .send_mail import envoi_email
from datetime  import datetime
    
    
def envoyer_email(email:str,lien:str):
    subjet = "sous-scription"
    template = 'envoimail.html'
    context = {
                 'date': datetime.today(),
                    'email': email,
                    'lien':lien
                }
    receivers = [email]

    has_send = envoi_email(
                    sujet=subjet,
                    desti=receivers,
                    template=template,
                    context=context
                    )
    if has_send:
        return True 
    else:
        return False