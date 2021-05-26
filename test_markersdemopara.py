import pytest
import sys

@pytest.mark.parametrize("username", "password",
                         [
                             ("ravali", "gade"),
                             ("Python", "Pytest"),
                             ("tyt", "unijkut"),
                         ]
                         )
def test_login(username, password):
    print(username)
    print(password)
