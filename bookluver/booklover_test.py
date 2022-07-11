import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    test_object = BookLover('Han Solo', 'hsolo@millenniumfalcon.com', 'scifi')
    test_object.add_book('War of the Worlds', 4)
    
    def test_1_add_book(self):
        # Add a book and test if it is in book_list
        self.test_object.add_book('Diary of a Wimpy Kid', 2)
        print(self.test_object.book_list)
        
        expected = ['Diary of a Wimpy Kid', 2]
        self.assertEqual(self.test_object.book_list[1], expected)
    
    def test_2_add_book(self):
        # Add the same book twice. Test if it's in book_list only once
        self.test_object.add_book('The Hunger Games', 3)
        self.test_object.add_book('The Hunger Games', 3)
        print(self.test_object.book_list)
        
        expected = 3
        self.assertEqual(self.test_object.num_books_read, expected)
        # ************* review this
    
    def test_3_has_read(self):
        # Pass a book in the list and test if the answer is True 
        self.assertTrue(self.test_object.has_read('War of the Worlds'), 'Yep, this book was read!')
    
    def test_4_has_read(self):
        # Pass a book NOT in the list and use 'assert False' to test the answer is True 
        self.assertFalse(self.test_object.has_read('Barbie Girl'), 'Yep, this book was NOT read.')
    
    def test_5_num_books_read(self):
        # Add some books to the list, and test num_books matches expected
        self.test_object.add_book('Fourth book', 4)
        self.test_object.add_book('Fifth book', 3)
        self.test_object.add_book('Sixth book', 2)
        self.test_object.add_book('Seventh book', 1)
        self.test_object.add_book('Eigth book', 0)

        print('Number of Books Read:', 8)
        print(self.test_object.book_list)
        
        expected = 8 #len(self.test_object.book_list)
        self.assertEqual(self.test_object.num_books_read, expected)
    
    
    def test_6_fav_books(self):
        # Add some books with ratings to the list, making sure some of them have rating > 3.
        # Your test should check that the returned books have rating > 3.
        self.test_object.add_book('The best book', 5)
        self.test_object.add_book('The worst book', 0)
        self.test_object.add_book('Fine book', 2)
        self.test_object.add_book('A good book', 4)
        self.test_object.add_book('My favorite book', 5)
        
        # Test
        expected = self.test_object.book_list[self.test_object.book_list['book_rating'] > 3]
        self.assertEqual(self.test_object.fav_books, expected)

        print(self.test_object.fav_books)
        
       # **might need to change to the length (match # of rows)
        
    
if __name__ == '__main__':
    unittest.main(verbosity=3)