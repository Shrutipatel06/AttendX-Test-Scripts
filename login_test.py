
def test_login_with_valid_details():
    username = "student123"
    password = "student123"

    if username and password:
        print("PASS: Login details are provided")
    else:
        print("FAIL: Login details are missing")


def test_login_with_missing_username():
    username = ""
    password = "valid_password"

    if not username:
        print("PASS: Missing username detected")
    else:
        print("FAIL: Missing username not detected")


test_login_with_missing_username()