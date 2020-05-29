import pytest
from pytestpractice.LoggerInfo import getlogger



@pytest.mark.usefixtures("setupteardown")
class Test_Example:



    def testShow1(self):
        Logger = getlogger()
        print("Test_Show1 of Example_Test")
        Logger.info("Test_Show1 of Example_Test")

    def test_Nagesh(self):
        Logger = getlogger()
        print("Nagesh Method is called")
        Logger.warning("Nagesh Method is called")

    def test_show2(self):
        Logger = getlogger()
        print("test_show2 of Example_Test")
        assert 5 == 5
        Logger.critical("test_show2 of Example_Test")






#@pytest.fixture()
#def setupteardown(scope='function'):
    #print("This is called Before method")
    #yield
    #print("This is called after method")
