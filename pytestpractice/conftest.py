import pytest


@pytest.fixture(scope="function")
def setupteardown(scope='function'):

    print("This is called Before method Conftest")
    yield
    print("This is called after method Conftest")

@pytest.fixture(scope="class")
def dataload():
    return ["Nagesh", "Hadapsar", "Xpanxion"]


@pytest.fixture(params=[("Nagesh","Shubhangi"),("Mahesh","Komal")])
def crossbrowesr(request):
    return request.param


