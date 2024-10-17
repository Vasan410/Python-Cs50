from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Devid") == "hello, Devid"

# Converting the folder as package by creating new file with the name of "__init__.py"
# It will converts the folder as package
# This helps to test all code in the folder