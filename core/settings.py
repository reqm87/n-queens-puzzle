database_name = 'nqueenspuzzle'
database_user = 'postgres'
database_password = 'password'

try:
    from config.local_settings import *
except ImportError:
    pass
