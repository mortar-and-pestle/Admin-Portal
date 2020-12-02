Presentation Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How to Run app
1. Clone https://github.com/mortar-and-pestle/Admin-Portal
2. Install all required libraries located in the requirements.txt
3. Navigate to Admin-Portal Directory and run:
  python3 run.py
4. Navigate to http://localhost:5000/.
5. Here are the logins for each type of Admin:
  ADMIN
    Username: Chase
    Password:123456
  FINANCE_ADMIN
    Username: Bob
    Password: 123456
  SALES_ADMIN
    Username: Larry
    Password: 123456
  HR_ADMIN
    Username: Jessica
    Password: 123456
  TECH_ADMIN
    Username: Mark
    Password: 123456
  *Not given Admin designation
    Username: Eve
    Password: 123456

6. You will redirected to a page displaying that admin's relevant links.
7. Unit tests and coverage can be checked by running:
  coverage run test.py
  coverage report -m admin/*py
