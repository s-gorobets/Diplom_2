from faker import Faker


def fake_email():
    faker = Faker()
    return faker.email()


def fake_pass():
    faker = Faker()
    return faker.password()


def fake_name():
    faker = Faker()
    return faker.name()
