from numb3rs import validate

def test_valid_addresses():
    assert validate("192.168.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("127.0.0.1") == True
    assert validate("10.0.0.1") == True

def test_invalid_addresses():
    assert validate("256.256.256.256") == False
    assert validate("192.168.0") == False
    assert validate("192.168.0.0.1") == False
    assert validate("192.168.0.-1") == False
    assert validate("192.168.0.256") == False
    assert validate("192.168.0.999") == False
    assert validate("192.168.0.abc") == False
    assert validate("192.168.0.") == False
    assert validate(".192.168.0.1") == False
    assert validate("192.168..1") == False
    assert validate("192.168.0.1.1") == False
    assert validate("192,168,0,1") == False
    assert validate("192 168 0 1") == False
