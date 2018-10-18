import unittest

from discworld_books  import app

class ProjectTests(unittest.TestCase):

##########################
####setup and teardown####
##########################

#executed prior to each test
	def setUp(self):
		app.config['TESTING'] = True
		app.config['DEBUG'] = False
		self.app = app.test_client()

		self.assertEquals(app.debug, False)

#executed after each test

	def tearDown(self):
		pass

######################
####helper methods####
######################

#############
####tests####
#############

	def test_main_page(self):
		response = self.app.get('/', follow_redirects = True)
		self.assertIn(b'Welcome to the Discworld Books App!', response.data)
		self.assertIn(b'Chronologically', response.data)
		self.assertIn(b'The City Watch', response.data)
		self.assertIn(b'The Witches', response.data)
		self.assertIn(b'Death', response.data)
		self.assertIn(b'Moist Von Lipwig', response.data)
		self.assertIn(b'Rincewind/The Wizards', response.data)
		self.assertIn(b'For Younger Readers', response.data)


if __name__ == "__main__":
	unittest.main()

 
