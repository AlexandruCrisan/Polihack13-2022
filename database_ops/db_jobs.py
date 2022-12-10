import database_ops.setup as setup
from database_ops.db_users import DB_USERS


class DB_JOBS():
  def __init__(self):
    self.__jobTable = setup.startSetup("test-jobs")
    self.__dbUsers = DB_USERS()

  def get_job(self, id):
        response = self.__jobTable.get_item(
            Key={
                'id': id
            }
        )
        try:
            return response["Item"]
        except KeyError:
            return {"ErrorMessage": "Home Does not Exist"}

  def add_job(self, jobObjJSON):
        self.__jobTable.put_item(
            Item=jobObjJSON
        )

        # Add them into the provider's account
        userJSON = self.__dbUsers.get_user(jobObjJSON["username"])
        jobs = userJSON["jobs"]

        jobs.append(jobObjJSON["id"])
        return self.__dbUsers.updateJobs(jobObjJSON["username"], list(set(jobs)))


  def delete_home(self, id: str):
        response = self.__jobTable.delete_item(
        Key = {
            'id': id
        }
        )
        return response
    
  def get_all_jobs(self):
        response = self.__jobTable.scan(AttributesToGet=['id', 'title', 'description', 'username', 'min_salary', 'city'])
        return response["Items"]