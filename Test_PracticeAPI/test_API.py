from API_Automation.Test_PracticeAPI.APICode import *
import pytest
from os import *
import pytest_ordering

# Create an object of class API_Methods and use methods belonging to this class.
__test_Obj = API_Methods()
@pytest.fixture(scope='module')
def setUp() -> None:
    print("This is API testing with 1.Get, 2.Put, 3.Post, 4.Delete methods")
    print("*"*70)

@pytest.mark.run(order=1)
def test_getMethod():
    msg = __test_Obj.getMethod('https://reqres.in/api/users?page=2')
    return msg

@pytest.mark.run(order=2)
def test_getSingleUser():
    __test_Obj.getSingleUser('https://reqres.in/api/users/2')

@pytest.mark.run(order=3)
def test_putMethod():
    __data = {"name": "morpheus", "job": "zion resident"}
    __test_Obj.putMethod('https://reqres.in/api/users/2',__data)

@pytest.mark.run(order=4)
def test_postMethod():
    __data = ['{"name": "morpheus", "job": "zion resident"}',
              '{"name": "mark", "job": "security agent"}',
              '{"name": "paul", "job": "Consultant"}']
    __test_Obj.postMethod('https://reqres.in/api/users',__data)

@pytest.mark.run(order=5)
def test_deleteMethod():
    __test_Obj.deleteMethod('https://reqres.in/api/users/2')

@pytest.mark.run(order=6)
def tearDown() -> None:
    print("*"*70)
    print('API testing is successfully completed')






