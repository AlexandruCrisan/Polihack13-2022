from model.user import User


class Refugee(User):
    def __init__(self, username: str, password: str, name: str, phone_number: str, nationality: str, location, skills: list):
        super().__init__(username, password, name, phone_number)
        self.__nationality = nationality
        self.__location = location
        self.__skills = skills
    
    def get_nationality(self):
      return self.__nationality
    
    def get_location(self):
      return self.__location

    def get_skills(self):
      return self.__skills
