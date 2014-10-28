from blog import app
import unittest

class FlaskTestCase(unittest.TestCase):
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	def test_login_correct(self):
		tester = app.test_client(self)
		response = tester.post('/login', data=dict(email="styccs@gmail.com", password="admin"), follow_redirects=True)		
		self.assertIn(b'You were just logged in',response.data)

	def test_login_incorrect(self):
		tester = app.test_client(self)
		response = tester.post('/login', data=dict(email="styccs@gmail.com", password="adm0n"))		
		self.assertIn(b'Invalid password',response.data)

	def test_logout(self):
		tester = app.test_client(self)
		tester.post('/login', data=dict(email="admin@one.com",password="admin"),follow_redirects=True)
		response = tester.get('/logout', follow_redirects=True)
		self.assertIn(b'You were just logged out', response.data)

if __name__ == '__main__':
	unittest.main()