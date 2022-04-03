from cgi import print_arguments


class CellPhone:
    def __init__(self, model):
        self.model = model
        self.phone_number = 5555555555
        self.contacts = {}
        self.messages = []
        self.vibrate = True
    def recive_text(self):
        self.text = input(f'send a text to {self.phone_number}')
        print(self.text)
        self.messages.append(self.text)
    def toggle_vibrate(self):
        if self.vibrate == True:
            self.vibrate = False
            print('Silent Mode Off')
        else:
            self.vibrate = True
            print('Silent Mode On')
    def send_message(self):
        self.sent_message = self.contacts[input('Enter Contact')] = input('Send a message')
        print(self.sent_message)        