# test_restfull_bookings.py
from API_Automation.SampleAPI import restfullbooker
from pyassert import *
from assertpy import assert_that

def test_bookings_for_mark():
    resp = restfullbooker.get_bookings('Mark')
    print(resp.ok)
    assert_that(resp.ok).is_true()
    assert_that("{}".format(resp)).is_equal_to('<Response [200]>')
    for booking in resp.json():
        assert_that(resp.ok).is_true()
        assert_that("{}".format(resp)).is_equal_to('<Response [200]>')
        resp2 = restfullbooker.describe_booking(booking['bookingid'])
        print(resp2)
        assert_that(resp2.json()["firstname"], 'Firstname').contains('Mark')

def test_addbooking():
    resp = restfullbooker.add_random_booking()
    print(resp.json())
    assert_that(resp.ok).is_true()
    assert_that("{}".format(resp)).is_equal_to('<Response [200]>')
    # TODO construct a booking to create and assert created booking against it


def test_updatebooking():
    auth_token = restfullbooker.get_authtoken()
    new_booking = restfullbooker.add_random_booking().json()['bookingid']
    resp = restfullbooker.update_booking(new_booking, auth_token)
    assert_that(resp.ok).is_true()
    assert_that("{}".format(resp)).is_equal_to('<Response [200]>')


def test_removebooking():
    auth_token = restfullbooker.get_authtoken()
    new_booking = restfullbooker.add_random_booking().json()['bookingid']
    resp = restfullbooker.remove_booking(new_booking, auth_token)
    assert_that(resp.ok).is_true()
    assert_that("{}".format(resp)).is_equal_to('<Response [201]>')

test_bookings_for_mark()
#test_addbooking()