from hello import hello


def test_default():
    assert hello() == "Hello, world"


def test_argument():
    # assert hello("Sanjeeva") == "Hello, Sanjeeva"
    # assert hello("Shreya") == "Hello, Shreya"
    for name in ["Sanjeeva", "Shreya"]:
        assert hello(name) == f"Hello, {name}"
