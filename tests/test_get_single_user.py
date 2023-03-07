from requests_folder.get_single_user import get_single_user

class TestGetSingleUser():
    def test_get_single_user(self):
        r = get_single_user()
        assert r.status_code == 200, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'