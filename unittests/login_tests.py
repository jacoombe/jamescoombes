__author__ = 'james'
import unittest
from app import app, configuration

class loginTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def login(self, username, password):
        """Logs in using the supplied parameters
        @param username The username to be logged in with
        @param password The password to be used when logging in
        """
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        """Logs out the current user"""
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login(app.config['USERNAME'], app.config['PASSWORD'])
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', app.config['PASSWORD'])
        assert 'Invalid username' in rv.data
        rv = self.login(app.config['USERNAME'], 'defaultx')
        assert 'Invalid password' in rv.data

if __name__ == '__main__':
    unittest.main()