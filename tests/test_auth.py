from endpoints.class_for_auth import AuthorizeUser


def test_user_authorization():
    user_authorization = AuthorizeUser()
    user_authorization.user_auth()
    assert user_authorization.status_code_is_200()
    assert user_authorization.name_is_same_as_sent()
    assert user_authorization.token_is_not_empty()
