import requests
import time
class Client(object):

    def __init__(self, host, login, cooldown=4):
        print('========= KEYBOARD VS MOUSE (client, beta 1.0.0)')
        self.host = host
        self.login = login  
        self.session = requests.Session()
        self.cooldown = cooldown
        self.time = time.time()
        print('Connecting to server: %s ...'%host)
        response = self.session.get(self.host + '/login/client')
        self.token = response.text
        if self.token:
            print('Success! You are connected to the server.')
        self.add_token(self.login)

    def authorize(self):
        self.auth = self.session.post(self.host + '/login/client', 
                                      data=self.login) 
        print(self.auth.text)
        if self.auth.status_code != 200:
            exit(1)

    def submit(self, data):
        """
        Submit data to server every `self.cooldown` seconds.
        """
        if time.time() - self.time < self.cooldown:
            return 0
        self.time = time.time()
        self.add_token(data)
        try: 
            response = self.session.post(self.host + '/account/submit', data=data)
            print('')
            print(response.text)
            if self.auth.status_code != 200:
                exit(1)
            return 1
        except:
            print('Failed to submit stats to server! Connection lost?')
            return 0


    def add_token(self, data):
        data['_csrf'] = self.token
