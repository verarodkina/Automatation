from smartphone import Smartphone

catalog = []
phone_1 = Smartphone ("Apple" , "iPhone 15" , "+79511282802")
phone_2 = Smartphone ("POCO" , "X5 Pro" , "+79130525203")
phone_3 = Smartphone ("Vivo" , "X100s Pro" , "+79611695802")
phone_4 = Smartphone ("Samsung" , "A01" , "+79050754723")
phone_5 = Smartphone ("realme" , "13 Pro" , "+79080880525")

catalog.append (phone_1)
catalog.append (phone_2)
catalog.append (phone_3)
catalog.append (phone_4)
catalog.append (phone_5)

for phone in catalog :
    print (f"{phone.mark} - {phone.model}. {phone.number}")