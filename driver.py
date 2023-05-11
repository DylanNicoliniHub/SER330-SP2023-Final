
from person_def import Person
from employee_def import Employee
from employer_def import Employer
from job_def import Job

# Declare a person
person = Person(last_Name="last", first_Name="first", date_of_Birth="5/1/2023", type_of_Person="Test")
print("First Name:" + person.firstName + " " + " Last Name: " + person.lastName)

# Declare an Employee
employee = Employee(lastName="employee_lastName", firstName="employee_firstName", dateOfBirth="5/9/2023", employeeId=12345, salary=100)

# Declare an Employer
employer = Employer("Test Company", "BusinessType")

# Declare a Job
job = Job(name="Test Job", description="description")

# Post the job with the employer
employer.listJob(job)

# Hire the employee
employer.hire(job, employee)

# Remove the job posting
employer.removeJob("Test Job")

# Give the employee a raise
employee.increaseSalary(100000)

# decrease employee salary
employee.decreaseSalary(100)

# Terminiate the employee
employer.terminateEmployee(employee, job)

print("Finished")