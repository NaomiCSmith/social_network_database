from lib.database_connection import DatabaseConnection
from lib.post_repository import *
from lib.account_repository import *


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Retrieve all posts
post_repository = PostRepository(connection)
posts = post_repository.all()

# List them out
for post in posts:
    print(post)

# List out accounts

account_repository = AccountRepository(connection)
accounts = account_repository.all()
for account in accounts:
    print(account)
