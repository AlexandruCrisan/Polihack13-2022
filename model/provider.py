from model.user import User


class Provider(User):
    def __init__(self, id: str, name: str, phone_number: str, email: str):
        super().__init__(id, name, phone_number)
        self.__email = email
    
    def get_email(self):
      return self.__email