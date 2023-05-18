import pytest

from test_framework.src.pages.CheckoutPage import CheckoutPage
from test_framework.src.pages.Store import Store
from test_framework.src.helpers.specific_helpers import Users
from test_framework.src.pages.CartPage import CartPage
from test_framework.src.helpers.generic_helpers import generate_random_credentials as cred
from test_framework.src.helpers.generic_helpers import generate_number_sequence as num_seq
from test_framework.src.helpers.generic_helpers import generate_random_strings as rand_string


@pytest.mark.usefixtures('init_driver')
class TestSandbox:
    @pytest.mark.tcid33
    def test_sandbox(self):
        code = Users.coupon
        cart = Store(self.driver)
        checkout = CheckoutPage(self.driver)

        phone = num_seq(8)
        credentials = cred()
        first_name = rand_string()
        last_name = rand_string()
        address = rand_string()
        city = rand_string()
        postcode = num_seq(6)

        cart_view = CartPage(self.driver)
        cart.go_to_store()
        cart.add_to_cart()
        cart.view_cart_via_button()
        product_names = cart_view.get_names_of_product_in_cart()
        assert len(product_names) == 1, f'Expected 1 item in cart, but found {len(product_names)}'
        cart_view.input_coupon_code(code)
        cart_view.apply_coupon()
        cart_view.proceed_to_checkout()
        checkout.chose_country('Finland')
        checkout.fill_form(first_name, last_name, address, postcode, phone, credentials['email'], city)
        checkout.place_order()

