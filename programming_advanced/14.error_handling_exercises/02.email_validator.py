class NameTooShortError(Exception):
    """When the name in the email is less than or equal to 4"""


class MustContainAtSymbolError(Exception):
    """When there is no "@" in the email"""


class InvalidDomainError(Exception):
    """When the domain of the email is invalid (valid domains are: .com, .bg, .net, .org"""


entered_email = input()
while entered_email != 'End':

    # second check about containing at sign. Starting with it because this value is needed on the first check
    at_sign_position = ''
    if '@' in entered_email:
        at_sign_position = entered_email.index('@')
    else:  # this will be the error type in case of missing at sign
        raise MustContainAtSymbolError('Email must contain @"')

    # first check about name length
    if at_sign_position:
        signs_before_at = at_sign_position + 1  # because of index starting from zero
        if signs_before_at <= 4:
            raise NameTooShortError('Name must be more than 4 characters')

    # third check will use the last dot to confirm validity of the domain, will take it with slicing and length
    last_dot_reverse_position = entered_email[::-1].find('.')
    entered_email_length = len(entered_email)

    if last_dot_reverse_position == - 1:  # this will be returned if no dot in the email == invalid domain
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    else:
        last_dot_index = entered_email_length - 1 - last_dot_reverse_position
        domain = entered_email[last_dot_index::]

        if domain == '.com' or domain == '.bg' or domain == '.org' or domain == '.net':  # valid domain
            print('Email is valid')
        else:
            raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    entered_email = input()
