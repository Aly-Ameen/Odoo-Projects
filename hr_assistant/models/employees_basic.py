
from odoo import fields, models

class EmployeesData(models.Model):
     _name = 'employees.data'
     _description = 'Collecting all the basic data for the employees'
     _log_access = False

     full_name = fields.Char('Full Name')

     national_id = fields.Integer('National ID')

     date_of_birth = fields.Date('Date of Birth')

     martial_status = fields.Selection(
          [('single','Single'), ('married','Married'),
          ('divorced','Divorced'), ('widowed','Widowed')]
     )

     insurance_number = fields.Integer('Insurance Number')

     phone_number = fields.Integer('Insurance Number')

     employee_id = fields.Integer('Employee ID')

     job_title = fields.Char('Job Title')

     department = fields.Selection(
     selection= [('executive management','Executive Management'), ('legal affairs','Legal Affairs'),
                 ('accounting','Accounting'), ('human resources','Human Resources'),
                 ('procurement','Procurement'), ('sales','Sales'),
                 ('planning','Planning'), ('logistics','Logistics'),
                 ('warehouse','Warehouse'), ('customer relationships','Customer Relationships'),
                 ('maintenance','Maintenance'), ('security and services','Security & Services')],
     required=True)

     hiring_date = fields.Date('Hiring Date')

     net_salary = fields.Float('Net Salary')


