from faker import Faker
class SignUp:
    name = "nayan"
    # random email generation
    fake_email = Faker()
    email = fake_email.email()