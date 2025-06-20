from smartphone import Smartphone

catalog = [Smartphone("Samsung", "S20", "+79999999999"),
           Smartphone("iPhone", "12", "+79666666666"),
           Smartphone("Nokia", "7", "+79222222222"),
           Smartphone("Panasonic", "None", "+79000000000"),
           Smartphone("Xiaomi", "Redmi", "+79111111111"),]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
