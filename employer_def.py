from employee_def import Employee
from job_def import Job

class Employer:
    def __init__(self, name, businessType):
        self.jobs = []
        self.employees = []
        self.businessType = businessType

    
    def listJob(self, job):
        self.jobs.append(job)

    def removeJob(self, jobName):
        for job in self.jobs:
            if job.name == jobName:
                self.jobs.remove(job)
            else:
                print("unable to find job")

    def hire(self, job, employee):
        
        # add the employee to the list of the employer's employees
        self.employees.append(employee)

        # add the job to the employee's list of jobs
        employee.addJob(job)

    def terminateEmployee(self, employee, job):
        self.employees.remove(employee)
        employee.removeJob(job)