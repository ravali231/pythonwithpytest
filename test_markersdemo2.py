import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Login done")

@pytest.mark.skipif(sys.version_info<(3,7),reason="python version not supported")
def test_addProduct():
    print("add product")

@pytest.mark.xfail
def test_logout():
    assert False
    print("Logout done")
