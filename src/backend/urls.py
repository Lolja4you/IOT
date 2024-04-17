from src.backend.serializers import main, gazp, yndx, chmf


urls = [
    ('/', main),
    ('/YNDX', yndx),
    ('/GAZP', gazp),
    ('/CHMF', chmf),
]