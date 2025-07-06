class Answer:
    Forbidden = 'User already exists'
    Forbidden_field = 'Email, password and name are required fields'
    Unauthorized = 'email or password are incorrect'
    Unauthorized_autoriz = 'You should be authorised'
    BadRequest = 'Ingredient ids must be provided'
    Unauthorized_Get_Order = 'You should be authorised'


class DataUser:
    User_existing = {
        "email": "test-data@yandex.ru",
        "password": "password",
        "name": "Username"
    }

    Invalid_user = {
        "email": "wrong@yandex.ru",
        "password": "wrongpass"
    }


class Ingridiets:
    ingredients = [
        "60d3463f7034a000269f45e7",
        "60d3463f7034a000269f45e9",
        "60d3463f7034a000269f45e8",
        "60d3463f7034a000269f45ea"
    ]
