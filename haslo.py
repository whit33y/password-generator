import random
import string
import math

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits
all_chars = lowercase + uppercase + punctuation + digits

def generator_hasla(ilosc_znakow):
    if(ilosc_znakow % 4 == 0):
        znaki = ilosc_znakow / 4
        losowe_cyfry = random.sample(digits, int(znaki))
        losowe_male = random.sample(lowercase, int(znaki))
        losowe_duze = random.sample(uppercase, int(znaki))
        losowe_znaki = random.sample(punctuation, int(znaki))
        cala_lista_losowych = losowe_cyfry + losowe_male  + losowe_duze + losowe_znaki
        losowanie_losowych = random.sample(cala_lista_losowych, ilosc_znakow)
        haslo = ''.join(losowanie_losowych)
        return(haslo)
    else:
        mod_znaki = ilosc_znakow % 4
        znaki = math.floor(ilosc_znakow/4)
        losowe_cyfry = random.sample(digits, int(znaki))
        losowe_male = random.sample(lowercase, int(znaki))
        losowe_duze = random.sample(uppercase, int(znaki))
        losowe_znaki = random.sample(punctuation, int(znaki))  
        dopelnianie = random.sample(all_chars, int(mod_znaki))
        cala_lista_losowych = losowe_cyfry + losowe_male  + losowe_duze + losowe_znaki + dopelnianie
        losowanie_losowych = random.sample(cala_lista_losowych, ilosc_znakow)
        haslo = ''.join(losowanie_losowych)
        return(haslo)

haslo = generator_hasla(20)
print(haslo)