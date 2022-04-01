import requests
import time


#Logo
print(
                33[36;1m;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
                ;       S P A M  S M S %      ;33[31;1m
                ;---------------------------;33[32;1m
                33[0;32m;       Author : H4cVil     ;
                ;---------------------------;33[32;1m
                ;       WA : 082393056023    ;
                33[36;1m;---------------------------;
                ;       github : H4ckVil     ;33[32;1m
                33[32;1m;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
print ('\n[×] Nomor Di Awali dengan 8++')

#run nomor
nomor = input('[×] Normor Target : ')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'Terkirim' in req:
    print ('[√] SpamSmS Berhasil [√] ')
else:
    print ('[!] SpamSmS Gagal [!] ')
