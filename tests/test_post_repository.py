from lib.post import *
from lib.post_repository import *

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    assert repository.all() == [
        Post(1, "Naomis Diary", "There is not much to say...", 1, 1),
        Post(2, "How to have the best second breakfast", "Do not let anyone else in!", 5, 2),
        Post(3, "Plutos birthday", "Hey everybody! It is his birthday today!", 2, 3)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = repository.find(1)
    assert post == Post(1, "Naomis Diary", "There is not much to say...", 1, 1)

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.create(Post(None, "I'm tired", "I can't sleep", 3, 1))
    result = repository.all()
    assert result == [
        Post(1, 'Naomis Diary', 'There is not much to say...', 1, 1),
        Post(2, 'How to have the best second breakfast', 'Do not let anyone else in!', 5, 2),
        Post(3, 'Plutos birthday', 'Hey everybody! It is his birthday today!', 2, 3),
        Post(4, "I'm tired", "I can't sleep", 3, 1)
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(1)
    result = repository.all()
    assert result == [
        Post(2, 'How to have the best second breakfast', 'Do not let anyone else in!', 5, 2),
        Post(3, 'Plutos birthday', 'Hey everybody! It is his birthday today!', 2, 3)
    ]

def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = repository.find(1)
    post.title = "New title"
    assert repository.update(post) is None
    assert repository.all() == [
        Post(1, 'New title', 'There is not much to say...', 1, 1),
        Post(2, 'How to have the best second breakfast', 'Do not let anyone else in!', 5, 2),
        Post(3, 'Plutos birthday', 'Hey everybody! It is his birthday today!', 2, 3)
    ]
