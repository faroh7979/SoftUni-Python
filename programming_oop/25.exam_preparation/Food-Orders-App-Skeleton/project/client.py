class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        exception = False

        if not value.startswith('0'):
            exception = True

        elif len(value) != 10:
            exception = True

        else:
            for digit in value:
                try:
                    int(digit)
                except ValueError:
                    exception = True
                    break

        if exception:
            raise ValueError("Invalid phone number!")

        self.__phone_number = value

