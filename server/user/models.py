from database.models import Model


def encrypt(password):
    return password


class User(Model):
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = None

    def as_dict(self):
        fields = ['email', 'first_name', 'last_name', 'password']
        output = dict()
        for f in fields:
            output[f] = getattr(self, f)
        return output

    def set_password(self, password):
        self.password = encrypt(password)

    def delete(self):
        return

    @staticmethod
    def authenticate(email, password):
        return User

    @staticmethod
    def find(**kwargs):
        return [User]

    @staticmethod
    def get(**kwargs):
        return User

    @staticmethod
    def create(**kwargs):
        return User

