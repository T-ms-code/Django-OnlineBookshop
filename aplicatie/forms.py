from django import forms
from datetime import date
import re

class CartiFilterForm(forms.Form):
    autor=forms.CharField(required=False, label="Autor")
    pret_min=forms.FloatField(required=True, label="Pret minim")
    pret_max=forms.FloatField(required=True, label="Pret maxim")
    pagini_min=forms.IntegerField(required=True, label="Numar minim de pagini")
    pagini_max=forms.IntegerField(required=True, label="Numar maxim de pagini")
    

def validate1(value):
    if value:
        if not value[0].isupper():
            raise forms.ValidationError("Textul trebuie să înceapa cu litera mare!")
        if not all(char.isalpha() or char.isspace() for char in value):
            raise forms.ValidationError("Textul poate conține doar litere si spatii!")

def validator2(value):
    if value<0: raise forms.ValidationError("Numarul minim de zile nu este pozitiv!")
    
class ContactForm(forms.Form):
    nume=forms.CharField(required=True, max_length=10,label='Nume:',validators=[validate1])
    prenume=forms.CharField(label='Prenume:', validators=[validate1])
    data_nastere=forms.DateField(label='Data nasterii:')
    email=forms.EmailField(required=True,label='E-mail:')
    confirm_email=forms.EmailField(required=True,label='Confirmare e-mail:')
    variante=[
        ('reclamatie', 'Reclamatie'),
        ('intrebare', 'Întrebare'),
        ('review', 'Review'),
        ('cerere', 'Cerere'),
        ('programare', 'Programare')
    ]
    tip_mesaj = forms.ChoiceField(choices=variante, label='Tip mesaj:')
    subiect=forms.CharField(required=True,label='Subiect:', validators=[validate1])
    min_zile_asteptare = forms.IntegerField(label='Minim zile asteptare:', validators=[validator2])
    mesaj=forms.CharField(widget=forms.Textarea,label='Mesaj:')
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError("Adresele de email nu coincid!")
    
    def clean_data_nastere(self):
        data_nastere=self.cleaned_data.get("data_nastere")
        data_curenta = date.today()
        varsta = data_curenta.year - data_nastere.year - (
            (data_curenta.month, data_curenta.day) < (data_nastere.month, data_nastere.day)
        )
        if varsta < 18:
            raise forms.ValidationError("Minor!")
        return data_nastere
    
    def clean_mesaj(self):
        mesaj = self.cleaned_data.get("mesaj", "")  
        L = re.findall(r'\w+', mesaj)  

        
        if len(L) < 5 or len(L) > 100:
            raise forms.ValidationError("Mesajul trebuie să conțină între 5 și 100 de cuvinte!")

        if "http://" in mesaj or "https://" in mesaj:
            raise forms.ValidationError("Mesajul nu trebuie să conțină URL-uri!")

        nume = self.cleaned_data.get("nume", "") 
        if nume and not mesaj.endswith(nume):  
            raise forms.ValidationError("Mesajul trebuie să se încheie cu numele!")

        return mesaj 


        
from .models import Autor

class AutorForm(forms.ModelForm):
    informatii_aditionale1 = forms.IntegerField(label='Varsta:',required=False, help_text='Ai grija ca varsta sa nu fie mai mica de 20ani si sa fie egala cu decat diferenta dintre data curenta si data de nastere!')
    variante = [('da','Da'),('nu','Nu')]
    informatii_aditionale2 = forms.ChoiceField(choices=variante, label="Decedat:",required=True)
    informatii_aditionale3 = forms.CharField(label='Onoratii:', required=True)
    
    class Meta:
        model = Autor
        fields = ['nume', 'prenume', 'data_nastere']
        labels = {
            'nume': 'Nume:',
            'prenume': 'Prenume:',
            'data_nastere': 'Data_nastere:'
        }
        error_messages = {
            'data_nastere': {
                'required': 'Este un câmp obligatoriu. Te rog să îl completezi!'
            },
            'nume': {
                'max_length': 'Ai depășit lungimea maximă!'
            },
            'prenume': {
                'max_length': 'Ai depășit lungimea maximă!'
            }
        }
        
    def clean_nume(self):
        nume = self.cleaned_data.get("nume") 
        if nume:
            if nume[0] == 'A':
                raise forms.ValidationError("Numele nu trebuie să înceapă cu litera A!")
        else:
            raise forms.ValidationError("Numele este obligatoriu!")
        return nume
        
    def clean_data_nastere(self):
        data_nastere = self.cleaned_data.get("data_nastere")
        if data_nastere and data_nastere.year < 1960:
            raise forms.ValidationError("Nu sunt acceptați autorii născuți înainte de 1960!")
        return data_nastere

    def clean_informatii_aditionale1(self):
        varsta = self.cleaned_data.get("informatii_aditionale1")
        if varsta: 
            if varsta < 20:
                raise forms.ValidationError("Vârsta este prea mică!")
        else:
            raise forms.ValidationError("Vârsta trebuie precizată!")
        return varsta
    
    def clean(self):
        if self.cleaned_data.get("nume") and self.cleaned_data.get("prenume"):
            if not (all(char.isalpha() for char in self.cleaned_data.get("nume"))  and 
                    all(char.isalpha() for char in self.cleaned_data.get("prenume"))):
                raise forms.ValidationError("Numele și prenumele trebuie să conțină doar litere!")
        data_nastere = self.cleaned_data.get("data_nastere")
        varsta = self.cleaned_data.get("informatii_aditionale1")
        decedat = self.cleaned_data.get("informatii_aditionale2")
        if  data_nastere and varsta and decedat :
            today = date.today()
            interval = today.year - data_nastere.year - ((today.month, today.day) < (data_nastere.month, data_nastere.day))
            if decedat == 'da':
                if interval<varsta: 
                    raise forms.ValidationError("Varsta necorespunzatoare!") 
            else:
                if interval!=varsta:
                    raise forms.ValidationError("Varsta necorespunzatoare!")
                
                
                
    
    
            
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Model personalizat

class CustomUserCreationForm(UserCreationForm):
    telefon = forms.CharField(required=True)
    tara = forms.CharField(required=True)
    localitate=forms.CharField(required=True)
    strada = forms.CharField(required=True)
    gen = forms.CharField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ("username","email", "telefon","tara","localitate","strada","gen", "password1", "password2")
    
    def clean_telefon(self):
        telefon = self.cleaned_data.get("telefon")
        if not telefon.isdigit():
            raise forms.ValidationError("Numarul de telefon trebuie sa contina doar cifre!")
        if len(telefon) != 10:
            raise forms.ValidationError("Numarul de telefon trebuie sa aiba 10 cifre!")
        return telefon

    def clean_tara(self):
        tara = self.cleaned_data.get("tara")
        if len(tara) < 3:
            raise forms.ValidationError("Numele tarii trebuie sa aiba cel putin 3 caractere!")
        if not tara.isalpha():
            raise forms.ValidationError("Numele tarii trebuie sa contina doar litere!")
        return tara

    def clean_gen(self):
        gen = self.cleaned_data.get("gen")
        if gen.lower() not in ["masculin", "feminin", "alt"]:
            raise forms.ValidationError("Genul trebuie sa fie 'masculin', 'feminin' sau 'alt'!")
        return gen
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.telefon = self.cleaned_data["telefon"]
        if commit:
            user.save()
        return user
    
                    

from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    ramane_logat = forms.BooleanField(
        required=False,
        initial=False,
        label='Rămâneți logat timp de o zi:'
    )

    def clean(self):        
        cleaned_data = super().clean()
        ramane_logat = self.cleaned_data.get('ramane_logat')
        return cleaned_data
    





TEMPLATE_CATEGORII = {
    'epic': 'email_promotie_epic.html',
    'liric': 'email_promotie_liric.html',
}
from .models import Promotii

class PromotieForm(forms.ModelForm):
    categorii = forms.MultipleChoiceField(
        choices=[(key, key.capitalize()) for key in TEMPLATE_CATEGORII.keys()],
        widget=forms.CheckboxSelectMultiple,
        initial=lambda: [key for key in TEMPLATE_CATEGORII.keys()],
        label="Categorii pentru promoție:"
    )

    class Meta:
        model = Promotii
        fields = ['nume', 'data_expirare', 'subiect', 'mesaj', 'reducere', 'categorii']
        widgets = {
            'data_expirare': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

        
            
        

        
        
        
        

        
        

    