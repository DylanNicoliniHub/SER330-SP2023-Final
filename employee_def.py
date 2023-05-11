from person_def import Person
from job_def import Job


# Definition for an employee
# Constructor accepts last name and first name as string
# dateOfBith is Date/Time
# employee id is an integer
class Employee:
    
    def __init__(self, lastName, firstName, dateOfBirth, employeeId, salary):
        Person.__init__(self, lastName, firstName, dateOfBirth, "employee")
        self.salary = salary
        self.employeeId = employeeId
        self._jobs = []

    
    @property
    def jobs(self):
        return self._jobs

    def addJob(self, job):
        self._jobs.append(job)
    
    def removeJob(self, job):
        self._jobs.remove(job)
    
    def increaseSalary(self, targetSalary):
        # the target salary cannot be 0 
        # the target salary must be greater than the current salary
        if targetSalary != 0 and targetSalary > self.salary:
            self.salary = targetSalary

    def decreaseSalary(self, targetSalary):
        # the target salary cannot be 0 
        # the target salary must be less than the current salary
        if targetSalary != 0 and targetSalary < self.salary:
            self.salary = targetSalary

