from requests_folder.delayed_response import delayed_response

class TestDelayed():
    def test_delayed_response(self):
        r = delayed_response()
        assert r.status_code == 200, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'