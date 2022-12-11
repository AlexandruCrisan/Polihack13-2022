from model.user import User


class Refugee(User):
    def __init__(self, username: str, password: str, name: str, email: str, phone_number: str, nationality: str, location: dict, skills: list, address: str, donations: dict):
        super().__init__(username, password, name, phone_number)
        self.__nationality = nationality
        self.__location = location
        self.__skills = skills
        self.__email = email
        self.__address = address
        self.__donations = donations
    
    def get_nationality(self):
      return self.__nationality
    
    def get_location(self):
      return self.__location

    def get_donations(self):
      return self.__donations

    def get_skills(self):
      return self.__skills

    def get_email(self):
      return self.__email

    def get_address(self):
      return self.__address
