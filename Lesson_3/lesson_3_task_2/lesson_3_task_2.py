from smartphone import Smartphone

catalog = []
phone1 = Smartphone('Xiaomi', 'Mi 10', '+79555555555')
phone2 = Smartphone('Samsung', 'Galaxy', '+79666666666')
phone3 = Smartphone('Apple', 'IPhon 12', '+79777777777')
phone4 = Smartphone('Google', 'Pixel', '+79888888888')
phone5 = Smartphone('Vivo', 'X100', '+79999999999')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)


for phone in catalog:
    print(f'{phone.brand} - {phone.model}, {phone.phone_number}')