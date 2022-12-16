from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shop = ShoppingCart('Liverpool', 1000)
        self.other_shop = ShoppingCart('Shity', 20)

    def test_correct_initialisation(self):
        self.assertEqual('Liverpool', self.shop.shop_name)
        self.assertEqual(1000.0, self.shop.budget)
        self.assertEqual({}, self.shop.products)

    def test_shop_name_incorrect_start_with_lower_case_property(self):

        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = 'pesho'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_incorrect_contain_digit_property(self):

        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = 'Pesho2'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_correct_shop_name_property(self):
        self.assertEqual('Liverpool', self.shop.shop_name)

    def test_add_to_cart_too_hgh_price(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart("Mane", 100.001)

        self.assertEqual(f"Product Mane cost too much!", str(ve.exception))

    def test_test_add_to_cart_with_fair_price(self):
        self.shop.products = {'Liverpool': 23}
        expect = self.shop.add_to_cart('Liverpool', 99.99999)
        self.assertEqual("Liverpool product was successfully added to the cart!", expect)
        self.assertEqual({'Liverpool': 99.99999}, self.shop.products)

    def test_remove_from_cart_no_found_value(self):
        self.shop.products = {'Liverpool': 1000, 'Shity': 20}

        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart('Arsenal')

        self.assertEqual(f"No product with name Arsenal in the cart!", str(ve.exception))

    def test_remove_available_item(self):
        self.shop.products = {'Shity': 20, 'Liverpool': 1000, 'Arsenal': 50}
        expected = self.shop.remove_from_cart('Shity')

        self.assertEqual(expected, "Product Shity was successfully removed from the cart!")
        self.assertEqual({'Liverpool': 1000, 'Arsenal': 50}, self.shop.products)

    def test__add__method(self):
        self.shop.products = {'Liverpool': 1000}
        self.other_shop.products = {'Arsenal': 250, 'Chelsea': 300}
        expected = self.shop.__add__(self.other_shop)

        self.assertEqual(expected.shop_name, "LiverpoolShity")
        self.assertEqual(expected.budget, 1020)
        self.assertEqual(expected.products, {'Liverpool': 1000, 'Arsenal': 250, 'Chelsea': 300})

    def test_buy_product_enough_budget(self):
        self.shop.products = {'Salah': 500, 'Mane': 400}
        expected = self.shop.buy_products()
        self.assertEqual(expected, 'Products were successfully bought! Total cost: 900.00lv.')

    def test_buy_products_not_enough_budget(self):
        self.shop.products = {'Salah': 500, 'Mane': 600}
        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with 100.00lv!", str(ve.exception))


if __name__ == '__main__':
    main()
