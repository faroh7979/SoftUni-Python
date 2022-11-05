class Profile:
    def __init__(self, user_name: str, password: str):
        self.username = user_name
        self.password = password

    @property
    def username(self):
        return self.test

    @username.setter
    def username(self, value):

        if 4 < len(value) < 16:
            self.test = value
        else:
            raise ValueError('The username must be between 5 and 15 characters.')

    @property
    def password(self):
        return self.test_two

    @password.setter
    def password(self, value):

        if len(value) < 8:
            raise ValueError(
                'The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

        digit = False
        lower_case = False
        upper_case = False

        for symbol in value:
            if symbol.islower():
                lower_case = True
            elif symbol.isupper():
                upper_case = True
            elif symbol.isdigit():
                digit = True

        if digit and lower_case and upper_case:
            self.test_two = value
        else:
            raise ValueError(
                'The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

    def __str__(self):
        return f'You have a profile with username: "{self.test}" and password: {"*" * len(self.test_two)}'

