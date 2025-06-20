from address import Address
from mailing import Mailing

mail = Mailing(Address("111111", "Москва", "Арбат", "5", "1"),
               Address("100000", "НН", "Фрунзе", "1", "15"),
               1000,
               "123456789")

print(f"Отправление {mail.track} из {mail.from_address.index}, "
      f"{mail.from_address.city}, {mail.from_address.street}, "
      f"{mail.from_address.house} -{mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, {mail.to_address.house} "
      f"-{mail.to_address.apartment}. Стоимость {mail.cost} рублей.")
