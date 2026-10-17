
def test_login_with_valid_details():
    username = "student123"
    password = "student123"

    if username and password:
        print("PASS: Login details are provided")
    else:
        print("FAIL: Login details are missing")


def test_login_with_empty_details():
    username = ""
    password = ""

    if not username and not password:
        print("PASS: Empty login details detected")
    else:
        print("FAIL: Empty login details not detected")


test_login_with_valid_details()
test_login_with_empty_details()