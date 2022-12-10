class Job():
  def __init__(self, id:str, title: str, description: str, min_salary: str, username: str, city: str):
    self.__id = id
    self.__title = title
    self.__description = description
    self.__min_salary = min_salary
    self.__username = username
    self.__city = city
  
  def get_title(self):
    return self.__title

  def get_description(self):
    return self.__description

  def get_min_salary(self):
    return self.__min_salary

  def get_username(self):
    return self.__username

  def get_id(self):
    return self.__id

  def get_city(self):
    return self.__city
    