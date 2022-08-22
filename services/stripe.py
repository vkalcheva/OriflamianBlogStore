import stripe
from decouple import config


class StripeService:
    # def create_customer(self, user):
    #     stripe.api_key = config("STRIPE_API_KEY")
    #     customer = stripe.Customer.create(
    #         email=user.email,
    #         name=f"{user.first_name} {user.last_name}",
    #         description="simple_user",
    #         phone=user.phone,
    #     )
    #
    #     return customer

    def create_card(self):
        stripe.api_key = config("STRIPE_API_KEY")
        card = stripe.Token.create(
            card={
                "number": "4242424242424242",
                "exp_month": 8,
                "exp_year": 2023,
                "cvc": "314",
            },
        )
        card_token = card["id"]
        return card_token

    # def generate_card_token(self):
    #     data = stripe.Token.create(
    #         card={
    #             "number": "4242424242424242",
    #             "exp_month": 9,
    #             "exp_year": 2023,
    #             "cvc": "123",
    #         })
    #     card_token = data['id']
    #
    #     return card_token

