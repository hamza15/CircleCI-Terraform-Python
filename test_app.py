import app
import unittest

class AppTest(unittest.TestCase)

    def config(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_greeting_message(self):
        greeting = 'Hello World from BenchSci!'
        self.assertEqual(app.greet(), greeting)

if __name__ == '__main__':
    unittest.main()
