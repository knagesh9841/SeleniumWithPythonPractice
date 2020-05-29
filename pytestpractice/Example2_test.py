import pytest


def show1():
    print("Show 1 of Example2_Test")


@pytest.mark.smoke
def test_show2():
    print("test_show2 of Example2_Test")

