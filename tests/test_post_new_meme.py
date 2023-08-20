from endpoints.class_for_post_new_meme import PostNewMeme


def test_updating_meme(authorization):
    token, user = authorization
    new_meme = PostNewMeme(token)
    new_meme.post_meme()
    assert new_meme.status_code_is_200()
    assert new_meme.text_is_same_as_sent()
    assert new_meme.url_is_same_as_sent()
    assert new_meme.tags_are_same_as_sent()
    assert new_meme.info_is_same_as_sent()
