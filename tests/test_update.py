from requests_folder.update import update

class TestUpdate():
    def test_update(self):
        r = update()
        assert r.status_code == 200, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'