from lib.post import Post

def test_post_constructs():
    post = Post(1, "Title", "Content", 5, 1)
    assert post.id == 1
    assert post.title == "Title"
    assert post.content == "Content"
    assert post.views == 5
    assert post.account_id == 1

def test_posts_are_equal():
    post1 = Post(1, "Test Title", "Test Content", 1, 1)
    post2 = Post(1, "Test Title", "Test Content", 1, 1)
    assert post1 == post2


def test_posts_format_correctly():
    post = Post(1, "Test Title", "Test Content", 1, 1)
    assert str(post) == "Post(1, Test Title: Test Content - 1 views, account 1)"