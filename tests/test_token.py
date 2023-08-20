from endpoints.class_for_token import CheckToken


def test_if_token_is_alive(authorization):
    token, user = authorization
    user_token = CheckToken(token, user)
    user_token.get_token_info()
    assert user_token.status_code_is_200()
    assert user_token.token_is_alive()
