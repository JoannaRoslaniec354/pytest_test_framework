import random
import string
import logging as logger


def generate_random_credentials(domain=None, email_prefix=None):
    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    random_passwd_length = 20
    rand_password = ''.join(random.choices(string.ascii_letters + string.digits, k=random_passwd_length))

    if not domain:
        domain = 'test.com'
    if not email_prefix:
        email_prefix = 'testuser'

    email = email_prefix + '_' + random_string + '@' + domain

    logger.info(f'Generated random email: {email}')
    logger.info(f'Generated random pass: {rand_password}')

    random_email_and_password_dict = {'email': email, 'password': rand_password}

    return random_email_and_password_dict


def generate_number_sequence(random_number_sequence_length):
    random_number_sequence = ''.join(random.choices(string.digits, k=random_number_sequence_length))
    return random_number_sequence


def generate_random_strings():
    random_length = random.randint(0, 15)
    random_string = ''.join(random.choices(string.ascii_letters, k=random_length))
    return random_string
