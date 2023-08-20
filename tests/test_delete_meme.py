from endpoints.class_for_delete_meme import DeleteMeme


def test_deleting_meme(authorization, post_new_meme):
    token, user = authorization
    meme_id = post_new_meme
    delete_meme = DeleteMeme(token, meme_id)
    delete_meme.delete_meme()
    assert delete_meme.status_code_is_200()
    assert delete_meme.check_the_response_message()
    assert delete_meme.check_that_meme_is_not_found()
