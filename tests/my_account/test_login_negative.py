import pdb

import pytest
from test_framework.src.pages.MyAccountSignedOut import MyAccountSignedOut
from test_framework.src.helpers.specific_helpers import Users


@pytest.mark.usefixtures('init_driver')
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        username = Users.non_existent_username
        password = Users.non_existent_password
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_username(username)
        my_account.input_password(password)
        my_account.click_login_button()
        my_account.text_message('Unknown email address. Check again or try your username.')
