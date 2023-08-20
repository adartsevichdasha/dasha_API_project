import pytest
from endpoints.class_for_auth import AuthorizeUser
from endpoints.class_for_post_new_meme import PostNewMeme


@pytest.fixture()
def authorization():
    user_token = AuthorizeUser()
    user_token.user_auth()
    token = user_token.token
    user = user_token.user
    return token, user


@pytest.fixture()
def post_new_meme(authorization):
    token, user = authorization
    new_meme = PostNewMeme(token)
    new_meme.post_meme()
    return new_meme.meme_id
