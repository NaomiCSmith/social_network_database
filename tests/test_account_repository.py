from lib.account import *
from lib.account_repository import *

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    result = repository.all()
    assert result == [
        Account(1, "naomismith", "naomismith@gmail.com"),
        Account(2, "bilbobaggins", "bilbohatestravel@yahoo.co.uk"),
        Account(3, 'mickeymouse12', "mickeymickeymouse@hotmail.com")
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    pass

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    pass

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    pass

def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    account = repository.find(1)
    account.email_address = "lazysnoopy123@aol.com"
    assert repository.update(account) is None
    assert repository.all() == [
        Account(1, "naomismith", "lazysnoopy123@aol.com"),
        Account(2, "bilbobaggins", "bilbohatestravel@yahoo.co.uk"),
        Account(3, "mickeymouse12", "mickeymickeymouse@hotmail.com")
    ]