import pytest
from test_framework.src.pages.MyAccountSignedIn import MyAccountSignedIn
from test_framework.src.pages.MyAccountSignedOut import MyAccountSignedOut
from test_framework.src.helpers.generic_helpers import generate_random_credentials as random_cred


@pytest.mark.usefixtures('init_driver')
class TestLoginPositive:

    @pytest.mark.tcid13
    def test_register_new_user(self):
        credentials = random_cred()
        register = MyAccountSignedOut(self.driver)
        register.go_to_my_account()
        register.register_send_email(credentials['email'])
        register.register_send_pass(credentials['password'])
        register.click_register_button()
        logged = MyAccountSignedIn(self.driver)
        logged.welcome_text_visible('From your account dashboard you can view your')
