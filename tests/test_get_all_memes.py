from endpoints.class_for_get_all_memes import GetAllMemes


def test_getting_all_memes(authorization):
    token, user = authorization
    list_of_memes = GetAllMemes(token)
    list_of_memes.get_all_memes()
    assert list_of_memes.status_code_is_200()
