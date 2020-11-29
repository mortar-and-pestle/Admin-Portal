from run import app
import unittest
from admin import db
from admin.models import User
from flask_login import login_user, current_user

class FlaskTestCases(unittest.TestCase):

    #Setup for testing
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
        self.app = app.test_client()

    #Tests redirection to correct page when client is logged out.
    def test_root(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html/text')
        self.assertEqual(response.status_code, 200)
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/home',content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #Tests correct response to invalid login input
    def test_correct_redirection_after_successful_slash_short_username(self):
        tester=app.test_client(self)
        response=tester.post('/',data=dict(username='u'),follow_redirects=True)
        self.assertIn(b'Field must be between 2 and 25 characters long.',response.data)
    def test_correct_redirection_after_successful_login_short_username(self):
        tester=app.test_client(self)
        response=tester.post('/home',data=dict(username='u'),follow_redirects=True)
        self.assertIn(b'Field must be between 2 and 25 characters long.',response.data)
    def test_correct_redirection_after_successful_slash_short_password(self):
        tester=app.test_client(self)
        response=tester.post('/',data=dict(password='1'),follow_redirects=True)
        self.assertIn(b'Field must be between 6 and 30 characters long.',response.data)
    def test_correct_redirection_after_successful_login_short_password(self):
        tester=app.test_client(self)
        response=tester.post('/home',data=dict(password='1'),follow_redirects=True)
        self.assertIn(b'Field must be between 6 and 30 characters long.',response.data)
    def test_correct_redirection_after_successful_slash_long_username(self):
        tester=app.test_client(self)
        response=tester.post('/',data=dict(username='uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'),follow_redirects=True)
        self.assertIn(b'Field must be between 2 and 25 characters long.',response.data)
    def test_correct_redirection_after_successful_login_long_username(self):
        tester=app.test_client(self)
        response=tester.post('/home',data=dict(username='uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'),follow_redirects=True)
        self.assertIn(b'Field must be between 2 and 25 characters long.',response.data)
    def test_correct_redirection_after_successful_slash_long_password(self):
        tester=app.test_client(self)
        response=tester.post('/',data=dict(password='1111111111111111111111111111111111111111111111'),follow_redirects=True)
        self.assertIn(b'Field must be between 6 and 30 characters long.',response.data)
    def test_correct_redirection_after_successful_login_long_password(self):
        tester=app.test_client(self)
        response=tester.post('/home',data=dict(password='11111111111111111111111111111111111111111111111'),follow_redirects=True)
        self.assertIn(b'Field must be between 6 and 30 characters long.',response.data)

    #Test correct response to valid login input
    def test_valid_login(self):
        tester=app.test_client(self)
        response=tester.post('/home',data=dict(username="Bob",password='123456'), follow_redirects=True)
        self.assertIn(b'Log Out',response.data)

    #Test correct response to invalid login credentials
    def test_invalid_login(self):
        tester=app.test_client(self)
        response=tester.post('/home',data=dict(username="bob",password='123456'), follow_redirects=True)
        self.assertIn(b'Login failed. Check username and password',response.data)

    #Test if user doesn't have ADMIN type yet
    def test_admin_has_type(self):
        tester=app.test_client(self)
        response=tester.post('/home',data=dict(username="Eve",password='123456'), follow_redirects=True)
        self.assertIn(b'You do not have admin status! Please contact IT to be assigned an admin status.',response.data)

    #Test redirection if authetnicated user revists login page
    def test_authenticated_user_redirect_from_login(self):
        tester=app.test_client(self)
        response = tester.post('/home',data=dict(username="Bob",password='123456'), follow_redirects=True)
        response = tester.get('/home',content_type='html/text', follow_redirects=True)
        self.assertIn(b'Log Out', response.data)


    def test_check_links_ADMIN(self):
        with app.test_request_context():
            tester=app.test_client(self)
            tester.post('/home',data=dict(username="Chase",password='123456'), follow_redirects=True)
            login_user(User.query.first())
            response = tester.get('/links',content_type='html/text')
            userType = User.query.first().type

            if(userType == "ADMIN"):
                self.assertIn(b'Manage User Accounts',response.data)
                self.assertIn(b'Assign Roles',response.data)
                self.assertIn(b'Help Desk',response.data)

    def test_check_links_FINANCE_ADMIN(self):
        with app.test_request_context():
            tester=app.test_client(self)
            tester.post('/home',data=dict(username="Bob",password='123456'), follow_redirects=True)
            login_user(User.query.first())
            response = tester.get('/links',content_type='html/text')
            userType = User.query.first().type

            if(userType == "FINANCE_ADMIN"):
                self.assertIn(b'Finance Reports',response.data)
                self.assertIn(b'Accounts Payable',response.data)
                self.assertIn(b'Accounts Receivale',response.data)
                self.assertIn(b'Tax',response.data)


    def test_check_links_SALES_ADMIN(self):
        with app.test_request_context():
            tester=app.test_client(self)
            tester.post('/home',data=dict(username="Larry",password='123456'), follow_redirects=True)
            login_user(User.query.first())
            response = tester.get('/links',content_type='html/text')
            userType = User.query.first().type

            if(userType == "SALES_ADMIN"):
                self.assertIn(b'Sales Reports',response.data)
                self.assertIn(b'Sales Leads',response.data)
                self.assertIn(b'Sales Demo',response.data)

    def test_check_links_HR_ADMIN(self):
        with app.test_request_context():
            tester=app.test_client(self)
            tester.post('/home',data=dict(username="Jessica",password='123456'), follow_redirects=True)
            login_user(User.query.first())
            response = tester.get('/links',content_type='html/text')
            userType = User.query.first().type

            if(userType == "HR_ADMIN"):
                self.assertIn(b'New Hire On-boarding',response.data)
                self.assertIn(b'Benefits',response.data)
                self.assertIn(b'Payroll',response.data)
                self.assertIn(b'Off-boarding',response.data)
                self.assertIn(b'HR Reports',response.data)

    def test_check_links_TECH_ADMIN(self):
        with app.test_request_context():
            tester=app.test_client(self)
            tester.post('/home',data=dict(username="Mark",password='123456'), follow_redirects=True)
            login_user(User.query.first())
            response = tester.get('/links',content_type='html/text')
            userType = User.query.first().type

            if(userType == "TECH_ADMIN"):
                self.assertIn(b'Application Monitoring',response.data)
                self.assertIn(b'Tech Support',response.data)
                self.assertIn(b'App Development',response.data)
                self.assertIn(b'App Admin',response.data)
                self.assertIn(b'Release Management',response.data)

    def test_logout_redirect(self):
        with app.test_request_context():
            tester=app.test_client(self)
            tester.post('/home',data=dict(username="Bob",password='123456'), follow_redirects=True)
            login_user(User.query.first())
            response = tester.get('/logout',content_type='html/text', follow_redirects=True)
            self.assertIn(b"Login Here", response.data)


if __name__ == "__main__":
    unittest.main()
