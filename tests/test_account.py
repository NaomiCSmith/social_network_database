from lib.account import Account

def test_account_constructs():
    account = Account(1, "My username", "My email")
    assert account.id == 1
    assert account.username == "My username"
    assert account.email_address == "My email"

def test_account_are_equal():
    account1 = Account(1, "Test username", "Test email")
    account2 = Account(1, "Test username", "Test email")
    assert account1 == account2


def test_accounts_format_correctly():
    account = Account(1, "Test username", "Test email")
    assert str(account) == "Account(1: Test username, Test email)"