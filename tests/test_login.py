from requests_folder.login import login

class TestLogin():
    def test_successful_login(self):
        r = login("eve.holt@reqres.in", "cityslicka")
        assert r.status_code == 200, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'

    def test_unsuccessful_login1(self):
        r = login("peter@klaven", "")
        expected_error = "Missing password"
        assert r.status_code == 400, f'Error: status code is incorrect. Expected 400, actual {r.status_code}'
        assert r.json()["error"] == expected_error, f"Error: is incorrect.Expected error:{expected_error}, Actual error: {r.json()['error']}"

    def test_unsuccessful_login2(self):
        r = login("", "lup")
        expected_error2 = "Missing email or username"
        assert r.status_code == 400, f'Error: status code is incorrect. Expected 400, actual {r.status_code}'
        assert r.json()["error"] == expected_error2, f"Error: is incorrect.Expected error:{expected_error2}, Actual error: {r.json()['error']}"