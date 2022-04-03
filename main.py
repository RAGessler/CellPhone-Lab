from cellphone import CellPhone

my_phone = CellPhone('Iphone 12')
my_phone.contacts['Mark'] = ''
print(my_phone.contacts)
my_phone.recive_text()
my_phone.recive_text()
print(my_phone.messages)
my_phone.send_message()
my_phone.toggle_vibrate()
print(f'Vibrate only is set to {my_phone.vibrate}')
print(my_phone.contacts)
