import unittest
'''
A testcase is created by subclassing unittest.
TestCase. The three individual tests are defined 
with methods whose names start with the letters 
test. This naming convention informs the test runner
about which methods represent tests.

Passing the -v option to your test script
 will instruct unittest.main() to enable 
 a higher level of verbosity
 
python second.py -v
'''
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()