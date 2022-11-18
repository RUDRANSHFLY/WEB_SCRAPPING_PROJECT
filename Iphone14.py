from bs4 import BeautifulSoup
import requests
from xlwt import Workbook

wb1 = Workbook()

IPHONE14 = wb1.add_sheet('IPHONE-14')
  







print("IPHONE 14 PRICES IN FLIPKART \n \n ")

iphone14 = requests.get("https://www.flipkart.com/apple-iphone-14-blue-128-gb/p/itmdb77f40da6b6d?pid=MOBGHWFHSV7GUFWA&lid=LSTMOBGHWFHSV7GUFWA3AV8J8&marketplace=FLIPKART&q=iphone14&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=8a55779f-4e80-4ae0-8c39-9fc99741c91d.MOBGHWFHSV7GUFWA.SEARCH&ppt=pp&ppn=pp&ssid=ljfduwqyao0000001667193732899&qH=694e31eb1200eb29")
so2 = BeautifulSoup(iphone14.content,"lxml")
ides2 = so2.find("span",class_="B_NuCI").text
ipp2 = so2.find('div',class_="_30jeq3 _16Jk6d").text
print(ides2+" :- "+ipp2)

IPHONE14.write(0, 0, ides2)
IPHONE14.write(0, 1, ipp2)

iphone142 = requests.get("https://www.flipkart.com/apple-iphone-14-purple-256-gb/p/itmb2bf402090fae?pid=MOBGHWFHQHE7ZPSB&lid=LSTMOBGHWFHQHE7ZPSBUUK6V6&marketplace=FLIPKART&q=iphone14&store=tyy%2F4io&srno=s_1_6&otracker=search&otracker1=search&fm=organic&iid=8a55779f-4e80-4ae0-8c39-9fc99741c91d.MOBGHWFHQHE7ZPSB.SEARCH&ppt=pp&ppn=pp&ssid=ljfduwqyao0000001667193732899&qH=694e31eb1200eb29")
so142 = BeautifulSoup(iphone142.content,"lxml")
ides142 = so142.find("span",class_="B_NuCI").text
ipp142 = so142.find('div',class_="_30jeq3 _16Jk6d").text
print(ides142+" :- "+ipp142)

IPHONE14.write(1, 0, ides142)
IPHONE14.write(1, 1, ipp142)

iphone145 = requests.get("https://www.flipkart.com/apple-iphone-14-purple-512-gb/p/itm97a1b385891d0?pid=MOBGHWFHG9HQHTU7&lid=LSTMOBGHWFHG9HQHTU7OVRY05&marketplace=FLIPKART&q=iphone14&store=tyy%2F4io&srno=s_1_11&otracker=search&otracker1=search&fm=organic&iid=8a55779f-4e80-4ae0-8c39-9fc99741c91d.MOBGHWFHG9HQHTU7.SEARCH&ppt=pp&ppn=pp&ssid=ljfduwqyao0000001667193732899&qH=694e31eb1200eb29")
so145 = BeautifulSoup(iphone145.content,"lxml")
ides145 = so145.find("span",class_="B_NuCI").text
ipp145 = so145.find('div',class_="_30jeq3 _16Jk6d").text
print(ides145+" :- "+ipp145)

IPHONE14.write(2, 0, ides145)
IPHONE14.write(2, 1, ipp145)

print("\n IPHONE 14 PRO VARIENT PRICES \n")

iphonepro = requests.get("https://www.flipkart.com/apple-iphone-14-pro-gold-128-gb/p/itme5895e593585d?pid=MOBGHWFHXPC3NFFY&lid=LSTMOBGHWFHXPC3NFFYGGZRVC&marketplace=FLIPKART&q=iphone14+pro&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=c74fed47-c352-4be9-8fa5-22c54d9637e6.MOBGHWFHXPC3NFFY.SEARCH&ppt=pp&ppn=pp&ssid=mmoi2iufvk0000001667194502424&qH=a4a061b26ad7f0b5")
sopro = BeautifulSoup(iphonepro.content,"lxml")
pro = sopro.find("span",class_="B_NuCI").text
propi= sopro.find('div',class_="_30jeq3 _16Jk6d").text
print(pro+" :- "+propi)

IPHONE14.write(3, 0, pro)
IPHONE14.write(3, 1, propi)

iphonepro2 = requests.get("https://www.flipkart.com/apple-iphone-14-pro-deep-purple-256-gb/p/itmfbeb0684432d7?pid=MOBGHWFHR4ZYUPH5&lid=LSTMOBGHWFHR4ZYUPH5GLZZWZ&marketplace=FLIPKART&q=iphone14+pro&store=tyy%2F4io&srno=s_1_4&otracker=search&otracker1=search&fm=organic&iid=c74fed47-c352-4be9-8fa5-22c54d9637e6.MOBGHWFHR4ZYUPH5.SEARCH&ppt=pp&ppn=pp&ssid=mmoi2iufvk0000001667194502424&qH=a4a061b26ad7f0b5")
sopro2 = BeautifulSoup(iphonepro2.content,"lxml")
pro2 = sopro2.find("span",class_="B_NuCI").text
propi2= sopro2.find('div',class_="_30jeq3 _16Jk6d").text
print(pro2+" :- "+propi2)

IPHONE14.write(4, 0, pro2)
IPHONE14.write(4, 1, propi2)

iphonepro5 = requests.get("https://www.flipkart.com/apple-iphone-14-pro-space-black-512-gb/p/itm67843bf67dbae?pid=MOBGHWFHH9JVZK6Z&lid=LSTMOBGHWFHH9JVZK6ZJ4HT4L&marketplace=FLIPKART&q=iphone14+pro&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=organic&iid=c74fed47-c352-4be9-8fa5-22c54d9637e6.MOBGHWFHH9JVZK6Z.SEARCH&ppt=pp&ppn=pp&ssid=mmoi2iufvk0000001667194502424&qH=a4a061b26ad7f0b5")
sopro5 = BeautifulSoup(iphonepro5.content,"lxml")
pro5 = sopro5.find("span",class_="B_NuCI").text
propi5= sopro5.find('div',class_="_30jeq3 _16Jk6d").text
print(pro5+" :- "+propi5)

IPHONE14.write(5, 0, pro5)
IPHONE14.write(5, 1, propi5)

iphonepro1 = requests.get("https://www.flipkart.com/apple-iphone-14-pro-silver-1-tb/p/itm87b6f4daf8cd0?pid=MOBGHWFHSY5K7VGA&lid=LSTMOBGHWFHSY5K7VGAGVAREI&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&st=storage")
sopro1 = BeautifulSoup(iphonepro1.content,"lxml")
pro1 = sopro1.find("span",class_="B_NuCI").text
propi1= sopro1.find('div',class_="_30jeq3 _16Jk6d").text
print(pro1+" :- "+propi1)

IPHONE14.write(6, 0, pro1)
IPHONE14.write(6, 1, propi1)


print("\n\nIPHONE 14 PRO MAX VARIENT \n ")

iphonemax = requests.get("https://www.flipkart.com/apple-iphone-14-pro-max-deep-purple-128-gb/p/itm5256789ae40c7?pid=MOBGHWFHCWHXRZZJ&lid=LSTMOBGHWFHCWHXRZZJNGJFTD&marketplace=FLIPKART&q=iphone+14+pro+max&store=tyy%2F4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&fm=organic&iid=b4dade8c-7f3d-426c-9200-75fba3d727ef.MOBGHWFHCWHXRZZJ.SEARCH&ppt=pp&ppn=pp&ssid=aeic5y4hts0000001667195174324&qH=37e37d60a349d989")
somax = BeautifulSoup(iphonemax.content,"lxml")
max = somax.find("span",class_="B_NuCI").text
maxmi= somax.find('div',class_="_30jeq3 _16Jk6d").text
print(max+" :- "+maxmi)

IPHONE14.write(7, 0, max)
IPHONE14.write(7, 1, maxmi)

iphonemax2 = requests.get("https://www.flipkart.com/apple-iphone-14-pro-max-gold-256-gb/p/itmd21bfa03be8c2?pid=MOBGHWFHZVHJM4HZ&lid=LSTMOBGHWFHZVHJM4HZLWF9MT&marketplace=FLIPKART&q=iphone+14+pro+max&store=tyy%2F4io&srno=s_1_9&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&fm=organic&iid=b4dade8c-7f3d-426c-9200-75fba3d727ef.MOBGHWFHZVHJM4HZ.SEARCH&ppt=pp&ppn=pp&ssid=aeic5y4hts0000001667195174324&qH=37e37d60a349d989")
somax2 = BeautifulSoup(iphonemax2.content,"lxml")
max2 = somax2.find("span",class_="B_NuCI").text
maxmi2= somax2.find('div',class_="_30jeq3 _16Jk6d").text
print(max2+" :- "+maxmi2)

IPHONE14.write(8, 0, max2)
IPHONE14.write(8, 1, maxmi2)

iphonemax5 = requests.get("https://www.flipkart.com/apple-iphone-14-pro-max-deep-purple-512-gb/p/itmf7d9a6db35ddd?pid=MOBGHWFHK5GZRHS3&lid=LSTMOBGHWFHK5GZRHS3XOKI1D&marketplace=FLIPKART&q=iphone+14+pro+max&store=tyy%2F4io&srno=s_1_11&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&fm=organic&iid=b4dade8c-7f3d-426c-9200-75fba3d727ef.MOBGHWFHK5GZRHS3.SEARCH&ppt=pp&ppn=pp&ssid=aeic5y4hts0000001667195174324&qH=37e37d60a349d989")
somax5 = BeautifulSoup(iphonemax5.content,"lxml")
max5 = somax5.find("span",class_="B_NuCI").text
maxmi5= somax5.find('div',class_="_30jeq3 _16Jk6d").text
print(max5+" :- "+maxmi5)

IPHONE14.write(9, 0, max5)
IPHONE14.write(9, 1, maxmi5)

iphonemax1 = requests.get("https://www.flipkart.com/apple-iphone-14-pro-max-silver-1-tb/p/itm674918cf10f1d?pid=MOBGHWFHHURZWVKE&lid=LSTMOBGHWFHHURZWVKEAO46IE&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&st=storage")
somax1= BeautifulSoup(iphonemax1.content,"lxml")
max1 = somax1.find("span",class_="B_NuCI").text
maxmi1= somax1.find('div',class_="_30jeq3 _16Jk6d").text
print(max1+" :- "+maxmi1)

IPHONE14.write(10, 0, max1)
IPHONE14.write(10, 1, maxmi1)


wb1.save('Iphone14.xls')