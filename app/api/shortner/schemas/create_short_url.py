CreateShortUrlSchema = {
    'type': 'object',
    'properties': {
        'longUrl': {'type': 'string'},
        'customName': {'type': 'string'},
        'expiryInMin': {'type': 'integer'},
    },
    'required': ['longUrl']
}
