from endpoints.class_for_get_one_meme import GetOneMeme


def test_get_one_meme(authorization, post_new_meme):
    token, user = authorization
    meme_id = post_new_meme
    existing_meme = GetOneMeme(token, meme_id)
    existing_meme.getting_one_meme()
    assert existing_meme.status_code_is_200()
    assert existing_meme.check_meme_id_is_same_as_sent()
