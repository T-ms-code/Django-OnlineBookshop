from django.shortcuts import render, redirect

from .models import Carte, Autor
from datetime import date
from django.core.mail import send_mail


import logging
logger = logging.getLogger('django')


def obtine_permisiuni_meniu(request):
    return {
        'is_administrator_produse': request.user.groups.filter(name="Administratori_produse").exists(),
    }

def trimite_email():
    send_mail(
        subject='Salutare!',
        message='Salut. Ce mai faci?',
        html_message='<h1>Salut</h1><p>Ce mai faci?</p>',
        from_email='djangoproiect@gmail.com',
        recipient_list=['djangoproiect@gmail.com'],
        fail_silently=False,
)


# Create your views here.
from django.http import HttpResponse
def index(request):
    # trimite_email()
    return HttpResponse("Primul raspuns")






def carte_filtrare_titlu(request):
    carti = Carte.objects.all()
    return render (request, 'pagina.html',{
    "Carti":carti.filter(titlu__lt='Moromeții')}
    )
    
def carte_filtrare_autor(request):
    carti = Carte.objects.all()
    autor = request.GET.get('autor')
    if autor:
        return render (request, 'pagina.html',{
    "Carti":carti.filter(autor__nume__exact=autor)}
    )
    else:return render (request, 'pagina.html',{
		"Carti":carti.filter(autor__nume__exact='Preda')}
		)

def carte_filtrare_nr_pagini(request):
    return render (request, 'pagina.html',{
		"Carti":Carte.objects.filter(nr_pagini__gt='300')}
		)
    
def carte_filtrare_pret(request):
    return render (request, 'pagina.html',{
		"Carti":Carte.objects.filter(pret__gte=40.00).order_by('pret')}
		)

# i=-3
    
# def paginare(request):
#     global i
#     i=i+3
#     carti=Carte.objects.all()
#     if i>len(carti): i=0
#     return  render (request, 'pagina.html',{
#	 	"Carti":carti[i:i+3]}) 



# def paginator1(request, c,i):
#     return render (request, 'pagina.html',{
# 		"Carti":c[i:i+3]}) 
    
# def paginare(request):
#     carti=Carte.objects.all()
#     l=len(carti)
#     contor=0
#     for i in range (0, l-3, 3):
#         paginator1(request,carti,i)
#         contor=contor+3
#     return render (request, 'pagina.html',{
# 		"Carti":carti[contor:contor+3]}) 



# from django.core.paginator import Paginator
# def paginare(request):
#     carti1 = Carte.objects.all()  
#     carti = Paginator(carti1, 3)  ###paginatorul
    
#     numarul_paginii = request.GET.get('pagina')  
#     pagina_efectiva = carti.get_page(numarul_paginii)  

#     return render(request, 'pagina.html', {
#         'Carti': pagina_efectiva
#     })
    
def paginare(request):
    carti = Carte.objects.all() 
    l=len(carti)
    n= int(request.GET.get('pagina'))
    if n>=1 and n<=l/3+1:  
        carti_pe_pagina=carti[(n-1)*3:n*3]
        return  render (request, 'pagina.html',{
		"Carti":carti_pe_pagina}) 
    else:  return HttpResponse("Nu exista aceasta pagina!")
    

from .forms import CartiFilterForm 

def carti_filter_form(request):
    if request.method=='POST':
        carti=Carte.objects.all()
        form=CartiFilterForm(request.POST)
        
        if form.is_valid():
            autor = form.cleaned_data.get('autor')
            pagini_min = form.cleaned_data.get('pagini_min')
            pagini_max = form.cleaned_data.get('pagini_max')
            pret_min = form.cleaned_data.get('pret_min')
            pret_max = form.cleaned_data.get('pret_max')

            if autor:
                carti = carti.filter(autor__nume__contains=autor)
            if pagini_min:
                carti = carti.filter(nr_pagini__gte=pagini_min)
            if pagini_max:
                carti = carti.filter(nr_pagini__lte=pagini_max)
            if pret_min:
                carti = carti.filter(pret__gte=pret_min)
            if pret_max:
                carti = carti.filter(pret__lte=pret_max)
    
    else: 
        form=CartiFilterForm() 
        carti=Carte.objects.all()
    return  render (request, 'filtrarecarti.html',{'Form':form, "Carti":carti}) 


import json
import time
from .forms import ContactForm

def captare_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_data = {key: value for key, value in form.cleaned_data.items() if key != 'confirm_email'}
# nu am nevoie de .save(commit=False), nu e un model existent
            data_curenta = date.today()
            contact_data['data_nastere'] = str(data_curenta.year - contact_data['data_nastere'].year) + ' ani si ' + str(data_curenta.month - contact_data['data_nastere'].month) + ' luni'
            contact_data['mesaj'] = ' '.join(contact_data['mesaj'].split())

            timestamp = int(time.time())
            nume_fisier = f"mesaj_{timestamp}.json"
            cale_fisier = '\\'.join(['aplicatie\mesaje',nume_fisier])
            cale_fisier = cale_fisier[:17]+cale_fisier[18:]
            with open(cale_fisier, 'w') as f:
                json.dump(contact_data, f)  
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})




from .forms import AutorForm
from django.http import HttpResponse, HttpResponseForbidden

def adauga_autor(request):
    permisiuni = [
        'aplicatie.view_autor',
        'aplicatie.change_autor',
        'aplicatie.delete_autor',
        'aplicatie.add_autor',
    ]
    if not all(request.user.has_perm(perm) for perm in permisiuni):
        return HttpResponseForbidden(render(request, '403.html', {
            'titlu': "Eroare-adaugare-autori",
            'mesaj': "Nu ai voie sa adaugi autori...hmm, pari suspect!",
            'user': request.user,
        }))
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save(commit=False)
            
            varsta = form.cleaned_data['informatii_aditionale1']
            decedat = form.cleaned_data['informatii_aditionale2']
            
            if decedat == 'da':
                autor.data_deces = autor.data_nastere.replace(year=autor.data_nastere.year + varsta)
                autor.descriere = f'Autorul a murit la varsta de {varsta} ani.'
            else:
                autor.descriere = f'Autorul are varsta de {varsta} ani.'

            autor.nationalitate = 'Romana'
            autor.premii = form.cleaned_data['informatii_aditionale3'][:100]
            autor.save()
            form = AutorForm()
    else:
        form = AutorForm()
    return render(request, 'adauga_autor.html', {'form': form})



from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def trimite_mail(email, user_name, confirm_url):
    
    context = {'name': user_name,'confirm_url':confirm_url}  
    html_content = render_to_string('email_template.html', context)


    email = EmailMessage(
        subject='Salutare!',
        body=html_content,
        from_email='djangoproiect@gmail.com',
        to=[email],
    )
    email.content_subtype = 'html'
    email.send(fail_silently=False) 



from .forms import CustomUserCreationForm


import random
import string

def genereaza_sir():
    lungime = random.randint(1, 5) 
    return ''.join(random.choices(string.ascii_letters, k=lungime))

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['username']!='admin':
                    user.cod=form.cleaned_data['username'][0]+form.cleaned_data['email'][:2]+genereaza_sir()
            
                    user.is_active = False ###PANA NU CONFIRMA MAIL-ul, NU POATE FACE NIMIC PE SITE/INCLUSIV LOGAREA!
                    user.save()
                    confirm_url = request.build_absolute_uri(f"/aplicatie/confirma_email/{user.cod}/")
                    trimite_mail(form.cleaned_data['email'], form.cleaned_data['username'], confirm_url)
                    return redirect('login')
            else: 
                    email=form.cleaned_data['email']
                    subiect = "Cineva incearca sa ne preia site-ul"
                    message1 = f"Cineva cu Email-iul: {email} forteaza inregistrarea ca admin!"
                    message2 = f"""
                                    <h1 style="color: red;">{subiect}</h1>
                                    <p>: Email: {email}</p>
                                """
                    mail_admins(subiect, message1, html_message=message2, fail_silently=False)
                    logger.critical("Cineva vrea sa autentifice ca admin, fara sa fie!")
                    messages.error(request, 'Nu sunteti admin!')#message-error
                    messages.warning(request, 'Veti fi raportat!')#message-warning
    else:
        form = CustomUserCreationForm()
    logger.debug("Debug pe inregistrare.")
    messages.debug(request, 'Se face si debug.')#message-debug
    messages.info(request, 'S-a incarcat formularul!')#message-info
    return render(request, 'inregistrare.html', {'form': form})





from datetime import datetime, timedelta
from django.core.mail import mail_admins
from django.utils.timezone import now

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    return ip

from django.contrib.auth import logout
from django.contrib.auth import login
from .forms import CustomAuthenticationForm



failed_logins = {}###asta nu face nimic si nici nu trebuie, caci pe mine ma intereseaza failed_login-ul din functie, adica doar atunci cand se "sta" pe pagina de logare, adica cand nu se reseteaza pagina/server-ul
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST, request=request)
        if form.is_valid():
            user = form.get_user()
        
            if user.blocat:
                messages.error(request, "Contul tau a fost blocat! Nu te poti autentifica!")
                return redirect('login')
            
            login(request, user)
            if not form.cleaned_data.get('ramane_logat'):
                request.session.set_expiry(60)#NU EXISTA O SESIUNE DOAR CU 0!!!
            else :
                request.session.set_expiry(24*60*60) 
            #Pentru a verifica durata sesiunii
            session_expiry = request.session.get_expiry_age()  
            messages.success(request, f'Sesiunea va expira în {session_expiry} secunde.')#message-succes

            return redirect('home')
        else:
            username = request.POST.get('username')
            adresa_ip = get_ip(request)
            timpul_curent = now()
            if username not in failed_logins:
                failed_logins[username] = []
            
            failed_logins[username].append((adresa_ip,timpul_curent))
            failed_logins[username] = [
                    (ip, time) for ip, time in failed_logins[username]
                    if (timpul_curent - time) < timedelta(minutes=2)]
            if len(failed_logins[username]) >= 3:
                    subiect = "Logari suspecte"
                    message1 = f"Username: {username}, IP: {adresa_ip} forteaza logarea!"
                    message2 = f"""
                        <h1 style="color: red;">{subiect}</h1>
                        <p>Username: {username}</p>
                        <p>IP: {adresa_ip}</p>
                    """
                    logger.critical("Se forteaza logarea!")
                    messages.error(request, 'Ati fortat logare!')#message-error
                    messages.warning(request, 'Veti fi raportat!')#message-warning
                    mail_admins(subiect, message1, html_message=message2, fail_silently=False)
    else:
        form = CustomAuthenticationForm()
    logger.debug("Debug pe logare.")
    messages.debug(request, 'Se face si debug.')#message-debug
    messages.info(request, 'S-a incarcat formularul!')#message-info
    return render(request, 'login.html', {'form': form})

    
    
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user = request.user 
    return render(request, 'home.html', {'user': user})



from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def schimba_parola(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save() 
            update_session_auth_hash(request, form.user)
            logger.info("Parola a fost actualizata!")
            messages.success(request, 'Parola a fost actualizata!') #message-succes
            return redirect('home')
        else: messages.error(request, 'Exista erori!')#message-error
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'schimba_parola.html', {'form': form})


#Nu e necesara @login_required, nu se intoarce eroare!!
def logout2(request):
    logger.info("Te-ai delogat cu succes!")
    messages.success(request, "Te-ai delogat cu succes!")#message-succes
    try:
        permission = Permission.objects.get(codename='vizualizeaza_oferta')
        request.user.user_permissions.remove(permission)
    except Permission.DoesNotExist:
        logger.warning("Permisiunea 'vizualizeaza_oferta' nu există.")
    
    logout(request)
    return redirect('login')



from .models import CustomUser
from django.core.exceptions import MultipleObjectsReturned
####AICI E LOCUL UNDE AM DEFINIT ALT EMAIL PENTRU ADMINI:----------------------------------------------------------
def confirma_email(request, cod):
    try:
        user = CustomUser.objects.get(cod=cod)
        
        if not user.email_confirmat:
            user.email_confirmat = True
            user.is_active = True
            user.save()
            logger.info(f"Email confirmat pentru utilizatorul {user.username}.")
            return render(request, 'email_confirmat.html', {'user': user})
        else:
            logger.warning(f"Email deja confirmat pentru utilizatorul {user.username}.")
            messages.warning(request, f"Email deja confirmat pentru utilizatorul {user.username}.")#message-warning

    except CustomUser.DoesNotExist:
        subiect = "Utilizator disparut inainte de confirmarea email-lui"
        message1 = f"Utlizatorul cu CODUL: {cod} a disparut!"
        message2 = f"""
                        <h1 style="color: red;">{subiect}</h1>
                        <p>COD_UTILIZATOR: {cod}</p>
                        <p style="background-color: red; color: white;">EROAREA: Utilizatorul nu există sau codul este invalid.</p>
                    """
        mail_admins(subiect, message1, html_message=message2, fail_silently=False)
        logger.error(f"Cod invalid sau utilizator inexistent pentru codul: {cod}")
        messages.error(request, f"Cod invalid sau utilizator inexistent pentru codul: {cod}")#message-error
        
    except MultipleObjectsReturned:
        logger.error(f"Mai multi utilizatori gasiti cu acelasi cod: {cod}")
        messages.error(request, f"Mai multi utilizatori gasiti cu acelasi cod: {cod}")#message-error
    
    return render(request, 'pagina_eroare.html')


from .models import Vizualizari

def adauga_vizualizare(request):
    id_utilizator=request.GET.get('id_utilizator')
    id_produs=request.GET.get('id_produs')
    if id_utilizator and id_produs:
        utilizator=CustomUser.objects.filter(id__exact=id_utilizator)
        produs=Carte.objects.filter(id__exact=id_produs)
        if not utilizator.exists():
            logger.warning("Utilizatorul cu id-ul furnizat nu exista!")
            return HttpResponse("Eroare: Utilizatorul cu id-ul furnizat nu exista!")
        if not produs.exists():
            logger.warning("Produsul cu id-ul furnizat nu exista!")
            return HttpResponse("Eroare: Produsul cu id-ul furnizat nu exista!")
        Vizualizari.objects.create(utilizator=utilizator[0], produs=produs[0])
        logger.debug(f"Vizualizare adaugata pentru utilizatorul={utilizator[0].username} si produsul={produs[0].titlu} la data curenta.")
        vizualizari = Vizualizari.objects.filter(utilizator__exact=utilizator[0]).order_by('-data_vizualizare')
        if vizualizari.count() > 5:
            for vizualizare in vizualizari[5:]:
                vizualizare.delete()
                logger.info(f"Vizualizarile vechi au fost stearse pentru utilizatorul {utilizator[0].username} si au ramas doar primele 5")
        logger.info("Vizualizare adaugata cu succes!")
        return HttpResponse("Vizualizare adaugata cu succes!")
    else: return HttpResponse("Eroare la adaugare!")



TEMPLATE_CATEGORII = {
    'epic': 'email_promotie_epic.html',
    'liric': 'email_promotie_liric.html',
}
from .forms import PromotieForm
from .models import Vizualizari
from .models import Carte
from django.core.mail import send_mass_mail


def adauga_promotie(request):
    if request.method == 'POST':
        form = PromotieForm(request.POST)
        if form.is_valid():
            categorii_selectate = form.cleaned_data['categorii']
            k = 3
            datatuple = []
            for categorie in categorii_selectate:
                promotie = form.save(commit=False)  
                utilizatori={}#AICI scot id-urile clientilor/userilor care ar beneficia de promotie pentru aceasta categorie
                for vizualizare in Vizualizari.objects.all():
                    if vizualizare.utilizator.id not in utilizatori:
                        carte = Carte.objects.get(id=vizualizare.produs.id)
                        if carte.categorie==categorie:
                            utilizatori[vizualizare.utilizator.id]=1
                    else:
                        carte = Carte.objects.get(id=vizualizare.produs.id)
                        if carte.categorie==categorie:
                            utilizatori[vizualizare.utilizator.id]+=1 
                lista_mailuri_useri=[]
                for utilizator in [x for x in utilizatori if utilizatori[x]>=k]:
                    user = CustomUser.objects.get(id=utilizator)
                    lista_mailuri_useri.append(user.email)
                if lista_mailuri_useri!=[]:
                    template = TEMPLATE_CATEGORII.get(categorie)
                    mesaj = render_to_string(template, {###NU e capabil send_mass_mail() sa trimita HTML 
                            'nume': promotie.nume,
                            'data_expirare': promotie.data_expirare,
                            'mesaj':promotie.mesaj,
                            'reducere':promotie.reducere,
                    })
                    datatuple.append((
                            promotie.subiect,
                            mesaj,
                            'djangoproiect@gmail.com',
                            lista_mailuri_useri,
                    ))
            promotie.save()
            send_mass_mail(datatuple, fail_silently=False)
            logger.info("Promotie adaugata cu succes!")
            return HttpResponse("Promotie adaugata cu succes!")
    else:
        form = PromotieForm()
    return render(request, 'promotie.html', {'form': form})
            
    

###################
def pagina_acces_oferte(request):
    permisiuni2 = obtine_permisiuni_meniu(request)
    permisiuni2['user']=request.user
    return render(request, 'pagina_acces_oferte.html', permisiuni2)
    # return render(request, 'pagina_acces_oferte.html', {'user': request.user,})
##################

from django.contrib.auth.models import Permission
def da_permisiune(request):
    if request.user.is_authenticated:
        permission = Permission.objects.get(codename='vizualizeaza_oferta')
        request.user.user_permissions.add(permission)
        return redirect('oferta')
    return HttpResponseForbidden("Nu esti logat!")
    
    
    
    
def oferta(request):
    if request.user.is_authenticated and request.user.has_perm('aplicatie.vizualizeaza_oferta'):
            return HttpResponse("Ofertele sunt valabile pentru toate cartile mai mari de 400 de pagini si mai vechi de 80 de ani!")
    return render(request, '403.html', {
        "titlu": "Eroare afisare oferta",
        "mesaj": "Nu ai voie sa vizualizezi oferta.",
    })
    


from django.shortcuts import get_object_or_404

def  detalii_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    return render(request, 'detalii_autor.html', {'autor': autor})

def  detalii_carte(request, id):
    carte = get_object_or_404(Carte, id=id)
    return render(request, 'detalii_carte.html', {'carte': carte})

def detalii_user(request, id):
    utilizator = get_object_or_404(CustomUser, id=id)
    return render(request, 'detalii_user.html', {'utilizator': utilizator})


from django.core.serializers.json import DjangoJSONEncoder
def cos_virtual(request):
    produse = Carte.objects.all()
    return render(request, 'cos_virtual.html', {'produse_json': produse})



from django.http import JsonResponse

@login_required
def cumpara_cos(request):
    if request.method != "POST":
        return JsonResponse({"error": "Metoda nepermiss! Folositi POST!"}, status=405)

    data = json.loads(request.body)#RESTABILIREA FORMATULUI INTIAL
    cos_virtual = data.get("cos", [])
    if cos_virtual==[]:
        return JsonResponse({"error": "Cosul este gol."}, status=400)

    utilizator = request.user
    
    
    total_pret=0
    total_cantitate=0
    carti_comandate = []

    print(cos_virtual)
    for item in cos_virtual:
        id = item.get('id')
        titlu = item.get('titlu')
        cantitate = item.get('cantitate')
        pret = item.get('pret')
        stoc = item.get('stoc')

        carte = Carte.objects.get(id=int(id))
        cantitate = int(cantitate)
        carte.nr_stoc -= cantitate### MODIFIC CHIAR IN BAZA DE DATE!!!si dau reload la pgina, ca sa se incarce cu noile date formularul
        carte.save()
        carti_comandate.append((id, titlu, pret, cantitate))
        total_pret += pret * cantitate
        total_cantitate +=  cantitate

    factura_path = genereaza_factura(utilizator, carti_comandate, total_cantitate, total_pret)

    subject = "Factura comenzii tale"
    body = f"Salut {utilizator.username},\n\nAici este factura pentru comanda ta."
    email = EmailMessage(subject, body, 'djangoproiect@gmail.com', [utilizator.email])
    email.attach_file(factura_path)
    email.send()

    return JsonResponse({"status": "success", "message": "Comanda a fost plasata cu succes!"})



import os
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def genereaza_factura(utilizator, comenzi, total_cantitate, total_pret):
    print(utilizator.username)
    facturi_folder = os.path.join(settings.BASE_DIR, "temporar-facturi")
    if not os.path.exists(facturi_folder):
        os.makedirs(facturi_folder)
    facturi_utilizator = os.path.join(facturi_folder, utilizator.username)
    if not os.path.exists(facturi_utilizator):
        os.makedirs(facturi_utilizator)
    timestamp = int(time.time())
    factura_path = os.path.join(facturi_utilizator, f"factura-{timestamp}.pdf")
    c = canvas.Canvas(factura_path, pagesize=letter)
    c.drawString(20, 750, f"Factura pentru {utilizator.username}.")
    c.drawString(20, 700, f"Email: {utilizator.email}")
    c.drawString(20, 650, f"Data comenzii: {now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(20, 600, f"Contact administrator: djangoproiect@gmail.com")
    y = 500
    for comanda in comenzi:
        lk = f"http://localhost:8000/aplicatie/detalii_carte/{comanda[0]}"
        c.drawString(2, y, f"Produs: {comanda[1]}, Cantitate: {comanda[3]}, Pret: {comanda[2]} RON/bucata, Link-produs: {lk}")
        y -= 20
    c.drawString(20, y - 20, f"Total produse: {total_cantitate}, Pret final: {total_pret} RON")
    c.save()
    return factura_path



###S-au mai stilizat paginile: .../cos_virtual/... si .../home/...







def meniu(request):
    permisiuni2 = obtine_permisiuni_meniu(request)
    return render(request, 'meniu.html', permisiuni2)