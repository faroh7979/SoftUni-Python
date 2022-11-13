from customer import Customer
from dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        try:
            customer = next(filter(lambda c: c.id == customer_id, self.customers))
            dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        except StopIteration:
            return 'Oops'

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"

            return "DVD is already rented"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        try:
            customer = next(filter(lambda c: c.id == customer_id, self.customers))
            dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        except StopIteration:
            return 'Oops'

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        list_for_returning = []

        for customer in self.customers:
            list_for_returning.append(f'{str(customer)}')

        for dvd in self.dvds:
            list_for_returning.append(f'{str(dvd)}')

        return "\n".join(list_for_returning)



import unittest


class TestsMovieWorld(unittest.TestCase):
    def test_customer_init(self):
        c = Customer("Pesho", 22, 1)
        self.assertEqual(c.name, "Pesho")
        self.assertEqual(c.age, 22)
        self.assertEqual(c.id, 1)

    def test_customer_repr(self):
        c = Customer("Pesho", 22, 1)
        self.assertEqual(repr(c), "1: Pesho of age 22 has 0 rented DVD's ()")

    def test_dvd_init(self):
        dvd = DVD("B", 1, 2020, "January", 10)
        self.assertEqual(dvd.name, "B")
        self.assertEqual(dvd.id, 1)
        self.assertEqual(dvd.creation_month, "January")
        self.assertEqual(dvd.creation_year, 2020)
        self.assertEqual(dvd.age_restriction, 10)
        self.assertEqual(dvd.is_rented, False)

    def test_dvd_class_method(self):
        dvd = DVD.from_date(1, "A", "16.10.1997", 18)
        self.assertEqual(dvd.name, "A")
        self.assertEqual(dvd.id, 1)
        self.assertEqual(dvd.creation_month, "October")
        self.assertEqual(dvd.creation_year, 1997)
        self.assertEqual(dvd.age_restriction, 18)
        self.assertEqual(dvd.is_rented, False)

    def test_dvd_repr(self):
        dvd = DVD.from_date(1, "A", "16.10.1997", 18)
        self.assertEqual(repr(dvd), "1: A (October 1997) has age restriction 18. Status: not rented")

    def test_movie_init(self):
        movie = MovieWorld("Test")
        self.assertEqual(movie.name, "Test")
        self.assertEqual(movie.customers, [])
        self.assertEqual(movie.dvds, [])

    def tests_movie_world_dvd_capacity(self):
        self.assertEqual(MovieWorld.dvd_capacity(), 15)

    def tests_movie_world_customer_capacity(self):
        self.assertEqual(MovieWorld.customer_capacity(), 10)

    def test_movie_world_add_customer_success(self):
        movie_world = MovieWorld("Test")
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        self.assertEqual(movie_world.customers, [c])

    def test_movie_world_add_customer_overflow(self):
        movie_world = MovieWorld("Test")
        for _ in range(11):
            movie_world.add_customer(Customer("Pesho", 20, 4))
        self.assertEqual(len(movie_world.customers), 10)

    def test_movie_world_add_dvd_success(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        movie_world.add_dvd(d)
        self.assertEqual(movie_world.dvds, [d])

    def test_movie_world_add_dvd_overflow(self):
        movie_world = MovieWorld("Test")
        for _ in range(16):
            movie_world.add_dvd(DVD("A", 1, 1254, "February", 10))
        self.assertEqual(len(movie_world.dvds), 15)

    def test_movie_world_rent_dvd_already_rented(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        c2 = Customer("Gosho", 26, 2)
        movie_world.add_customer(c)
        movie_world.add_customer(c2)
        movie_world.add_dvd(d)
        movie_world.rent_dvd(4, 1)
        result = movie_world.rent_dvd(2, 1)
        self.assertEqual(result, "DVD is already rented")

    def test_movie_world_rent_dvd_already_rented_by_user(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        movie_world.rent_dvd(4, 1)
        result = movie_world.rent_dvd(4, 1)
        self.assertEqual(result, "Pesho has already rented A")

    def test_movie_world_rent_dvd_no_permision(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 18)
        c = Customer("Pesho", 16, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        result = movie_world.rent_dvd(4, 1)
        self.assertEqual(result, "Pesho should be at least 18 to rent this movie")

    def test_movie_world_rent_dvd_success(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        result = movie_world.rent_dvd(4, 1)
        self.assertEqual(result, "Pesho has successfully rented A")
        self.assertEqual(d.is_rented, True)
        self.assertEqual(c.rented_dvds[0], d)

    def test_movie_world_return_dvd_success(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        movie_world.rent_dvd(4, 1)
        result = movie_world.return_dvd(4, 1)
        self.assertEqual(result, "Pesho has successfully returned A")
        self.assertEqual(c.rented_dvds, [])
        self.assertEqual(d.is_rented, False)

    def test_movie_world_return_dvd_unsuccessful(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        result = movie_world.return_dvd(4, 1)
        self.assertEqual(result, "Pesho does not have that DVD")

    def test_movie_world_repr(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        movie_world.rent_dvd(4, 1)
        actual = repr(movie_world).strip('\n')
        expected = "4: Pesho of age 20 has 1 rented DVD's (A)\n1: A (February 1254) has age restriction 10. Status: rented"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
