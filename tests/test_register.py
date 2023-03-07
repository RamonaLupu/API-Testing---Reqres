from requests_folder.register import register

class TestRegister():
    def test_successful_register(self):
        r = register("eve.holt@reqres.in", "pistol")
        assert r.status_code == 200, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'

    def test_unsuccessful_register(self):
        r = register("sydney@fife", "")
        expected_error = "Missing password"
        assert r.status_code == 400, f'Error: status code is incorrect. Expected 400, actual {r.status_code}'
        assert r.json()["error"] == expected_error, f"Error: is incorrect.Expected error:{expected_error}, Actual error: {r.json()['error']}"
