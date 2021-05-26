
def test_1():
    a = 10
    b = 20
    assert a != b

def test_2():
    name = "selenium"
    title = "selenium is for web automation"
    assert name in title

def test_3():
    name = "jenkins"
    title = "jenkins is CI server"
    assert name in title, "title does not match"
