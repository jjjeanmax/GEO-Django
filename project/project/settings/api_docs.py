SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'description': 'JSON Web Token<br/><br/>'
                           'Пример:<br/>'
                           '**Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.<br/>'
                           'eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.<br/>'
                           'SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c**',
            'name': 'Authorization',
            'in': 'header'
        }
    },
}

REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
}