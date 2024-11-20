import pytest
from jar import Jar

def test_initial_capacity():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_custom_capacity():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("ten")

def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(7)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(4)

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.withdraw(5)
    assert str(jar) == ""

if __name__ == "__main__":
    pytest.main()
