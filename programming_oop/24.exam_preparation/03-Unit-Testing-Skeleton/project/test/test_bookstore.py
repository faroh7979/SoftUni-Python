from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self):
        self.book = Bookstore(10)

    def test_correct_initialisation(self):
        self.assertEqual(10, self.book.books_limit)
        self.assertEqual({}, self.book.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book._Bookstore__total_sold_books)

    def test_total_sold_books_property_should_return_the_exact_number(self):
        self.assertEqual(0, self.book.total_sold_books)

    def test_books_limit_property(self):
        self.assertEqual(10, self.book.books_limit)

    def test_book_limit_setter_zero_or_less_should_raise_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.book.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_book_limit_setter_greater_than_zero_should_set_it(self):
        self.book.books_limit = 2

        self.assertEqual(2, self.book.books_limit)

    def test___len__representation(self):
        self.book.availability_in_store_by_book_titles = {'Klopp': 2, 'Guardiola': 1}
        result = self.book.__len__()
        self.assertEqual(3, result)

    def test_receive_book_if_there_is_not_enough_space_expect_to_raise_exception(self):
        self.book.availability_in_store_by_book_titles = {'Klopp': 5, 'Guardiola': 3}

        with self.assertRaises(Exception) as ex:
            self.book.receive_book("Klopp", 3)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_if_there_is_book_not_in_bookstore_expect_to_add_it(self):
        self.book.availability_in_store_by_book_titles = {'Klopp': 2}
        self.book.receive_book('Guardiola', 1)

        self.assertEqual({'Klopp': 2, 'Guardiola': 1}, self.book.availability_in_store_by_book_titles)

    def test_receive_book_if_there_is_book_which_is_in_bookstore_expect_to_increase_it(self):
        self.book.availability_in_store_by_book_titles = {'Klopp': 2, 'Guardiola': 1}
        result = self.book.receive_book('Guardiola', 5)

        self.assertEqual({'Klopp': 2, 'Guardiola': 6}, self.book.availability_in_store_by_book_titles)
        self.assertEqual(result, "6 copies of Guardiola are available in the bookstore.")

    def test_sell_book_if_the_book_is_not_available(self):
        self.book.availability_in_store_by_book_titles = {'Klopp': 2}

        with self.assertRaises(Exception) as ex:
            self.book.sell_book('Guardiola', 2)

        self.assertEqual("Book Guardiola doesn't exist!", str(ex.exception))

    def test_sell_book_if_the_book_is_available_but_there_is_not_enough_copies(self):
        self.book.availability_in_store_by_book_titles = {'Klopp': 5, 'Guardiola': 3}

        with self.assertRaises(Exception) as ex:
            self.book.sell_book('Guardiola', 4)

        self.assertEqual("Guardiola has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book_if_sold_is_successful(self):
        self.book.availability_in_store_by_book_titles = {'Klopp': 5, 'Guardiola': 3}
        result = self.book.sell_book('Guardiola', 3)

        self.assertEqual({'Klopp': 5, 'Guardiola': 0}, self.book.availability_in_store_by_book_titles)
        self.assertEqual(3, self.book.total_sold_books)
        self.assertEqual("Sold 3 copies of Guardiola", result)

    def test___str__representation(self):
        self.book.availability_in_store_by_book_titles = {'Klopp': 5, 'Guardiola': 3, 'Mourinho': 1}
        self.book._Bookstore__total_sold_books = 3
        expected_result = f"Total sold books: 3\nCurrent availability: 9\n - Klopp: 5 copies\n - Guardiola: 3 copies\n - Mourinho: 1 copies"

        self.assertEqual(expected_result, str(self.book))


if __name__ == "__main__":
    main()
