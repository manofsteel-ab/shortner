RegisterUserSchema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string', 'minLength': 4, 'maxLength': 14},
        'password': {'type': 'string', 'minLength': 6, 'maxLength': 14},
        'first_name': {'type': 'string', 'minLength': 4, 'maxLength': 14},
        'middle_name': {'type': 'string', 'minLength': 4, 'maxLength': 14},
        'last_name': {'type': 'string', 'minLength': 4, 'maxLength': 14},
        'email': {'type': 'email'},
        'primary_phone': {'type': 'string', 'minLength': 10, 'maxLength': 20}
    }
}
