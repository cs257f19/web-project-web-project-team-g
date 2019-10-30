import unittest


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        ds = Datasource()
        booklist = getBookRecID(1,2)
        self.assertEqual(len(booklist), 3)

    def test_few_fans(self):
        ds = Datasource()
        booklist = getBookRecID(10001,30000)
        self.assertEqual(len(booklist), 3)

    def test_no_common_books(self):
        ds = Datasource()
        booklist = getBookRecID(10001, 30000)
        self.assertEqual(len(booklist), 3)

if __name__ == '__main__':
    unittest.main()
