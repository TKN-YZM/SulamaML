import requests
from bs4 import BeautifulSoup


def Hava(intadata,sehir):
    url="https://havadurumu15gunluk.xyz/havadurumu/630/{}-hava-durumu-15-gunluk.html".format(sehir)

    response=requests.get(url)

    #print(response)

    if response.status_code==200:
        #print("İŞLEM BAŞARILI")
        soup=BeautifulSoup(response.text,"html.parser")
        #print(soup)

        tumVeriler=soup.find_all("tr")[intadata].text
        tumVeriler=tumVeriler.replace("Saatlik","").strip()

        print(tumVeriler)
        gunluk_hava=""
        gunduz_sicaklik=tumVeriler[-6:-4]
        gece_sicaklik=tumVeriler[-3:-1]


        tumVeriler=tumVeriler[6:-6].strip()

        gunun_ismi=tumVeriler[:3]


        gunKisaltma=["Sal","Çar","Per","Cum","Cmt","Paz","Pzt"]

        for x in gunKisaltma:
            if x in tumVeriler:
                gunluk_hava=tumVeriler.replace(x,"")


        gununIsimleri={"Paz":"Pazartesi","Pzt":"Pazartesi","Sal":"Salı","Çar":"Çarşamba","Per":"Perşembe","Cum":"Cuma","Cmt":"Cumartesi"}
        gunun_ismi=gununIsimleri[gunun_ismi]


        return [gunduz_sicaklik,gece_sicaklik,gunluk_hava]

    else:
        return ""

print(Hava(2,"Konya"))