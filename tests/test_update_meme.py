from endpoints.class_for_update_meme import UpdateMeme


def test_updating_meme(authorization, post_new_meme):
    token, user = authorization
    meme_id = post_new_meme
    updated_meme = UpdateMeme(token, user, meme_id)
    updated_meme.update_meme()
    assert updated_meme.status_code_is_200()
    assert updated_meme.updated_info_is_same_as_sent()
