

def sayhello():
    print("hello")


class Capability(object):
    token=None
    def __init__(self):
        self.token="init token"
    

    def get_token(self):
        return self.token
    