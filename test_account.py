from unittest.mock import Mock

import main


def test_print_name():
    username = 'todduser'
    email = "todd@example.com"
    data = {'email': email, 'username': username}
    req = Mock(get_json=Mock(return_value=data), args=data)

    # Call tested function
    assert main.subscribe(req)


def test_print_hello_world():
    data = {}
    req = Mock(get_json=Mock(return_value=data), args=data)

    # Call tested function
    assert main.subscribe(req)
