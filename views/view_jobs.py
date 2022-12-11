from flask import Blueprint, request

from adapter.job_adapter import JobAdapter
from database_ops.db_jobs import DB_JOBS
from model.job import Job

urlJobs = Blueprint('views', __name__)

jobs_table = DB_JOBS()

@urlJobs.route('/jobs/<string:job_id>', methods=['POST'])
def addJob(job_id: str):
  job_json = request.json

  job_obj = Job(job_id, job_json["title"], job_json["description"], job_json["min_salary"], job_json["username"], job_json["city"])
  return jobs_table.add_job(JobAdapter.toJSON(job_obj))

@urlJobs.route('/jobs/<string:job_id>', methods=['GET'])
def getJob(job_id: str):
  return jobs_table.get_job(job_id)

@urlJobs.route('/jobs/<string:home_id>', methods=['DELETE'])
def deleteJob(home_id: str):
  return jobs_table.delete_job(home_id)

  """
  {
    "title": "jobTitle",
    "description": "jobDescription",
    "city": "jobCity",
    "min_salary": 12000,
    "username": "username"
  }
  """


