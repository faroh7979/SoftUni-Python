from unittest import TestCase, main


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


class TestIntegerList(TestCase):
    def setUp(self):
        self.my_int = IntegerList(1, 2, 3, 4)

    def test_get_data(self):
        self.assertEqual([1, 2, 3, 4], self.my_int.get_data())

    def test_add_with_no_int(self):

        with self.assertRaises(ValueError) as ve:
            self.my_int.add(2.4)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_with_int(self):
        self.my_int.add(9)
        self.assertEqual([1, 2, 3, 4, 9], self.my_int.get_data())

    def test_remove_index_with_index_error(self):

        with self.assertRaises(IndexError) as ie:
            self.my_int.remove_index(5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_deleted_and_return_it(self):
        self.assertEqual(3, self.my_int.remove_index(2))

    def test_get_index_error(self):

        with self.assertRaises(IndexError) as ie:
            self.my_int.get(6)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_correct_index(self):
        self.assertEqual(1, self.my_int.get(0))

    def test_insert_index_error(self):

        with self.assertRaises(IndexError) as ie:
            self.my_int.insert(10, "el")

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_value_error_expected(self):

        with self.assertRaises(ValueError) as ve:
            self.my_int.insert(0, 2.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_correct_input(self):
        self.my_int.insert(2, 12)
        self.assertEqual(12, self.my_int.get(2))

    def test_get_biggest(self):
        self.assertEqual(max(self.my_int.get_data()), self.my_int.get_biggest())

    def test_get_index(self):
        self.assertEqual(2, self.my_int.get_index(3))


if __name__ == '__main__':
    main()
