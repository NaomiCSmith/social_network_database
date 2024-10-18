from lib.account import Account

class AccountRepository():
    def __init__(self, _connection):
        self._connection = _connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM accounts ORDER BY id ASC')
        accounts = []
        for row in rows:
                item = Account(row["id"], row["username"], row["email_address"])
                accounts.append(item)
        return accounts
    
    def find(self, account_id):
        rows = self._connection.execute('SELECT * from accounts WHERE id = %s', [account_id])
        row = rows[0]
        return Account(row["id"], row["username"], row["email_address"])

    def create(self, account):
        self._connection.execute('INSERT INTO accounts (username, email_address) VALUES (%s, %s)', [account.username, account.email_address])
        return None

    def delete(self, account_id):
        self._connection.execute('DELETE FROM accounts WHERE id = %s', [account_id])
        return None
    
    def update(self, account):
        self._connection.execute('UPDATE accounts SET username = %s, email_address = %s WHERE id = %s',[account.username, account.email_address, account.id])
