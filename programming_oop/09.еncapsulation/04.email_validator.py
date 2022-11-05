class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str):
        return True if len(name) >= self.min_length else False

    def __is_mail_valid(self, mail: str):
        return True if mail in self.mails else False

    def __is_domain_valid(self, domain: str):
        return True if domain in self.domains else False

    def validate(self, email: str):
        username, domain_mails = email.split('@')
        mail, domain = domain_mails.split('.')

        if self.__is_domain_valid(domain) and self.__is_mail_valid(mail) and self.__is_name_valid(username):
            return True

        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
