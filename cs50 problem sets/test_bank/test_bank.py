from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_h_not_hello():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("howdy") == 20

def test_other():
    assert value("goodbye") == 100
    assert value("Greetings") == 100
    assert value("Welcome") == 100
