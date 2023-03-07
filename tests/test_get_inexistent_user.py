from requests_folder.get_inexistent_user import get_inexistent_user

class TestGetInexistentUser():
    def test_get_inexistent_user(self):
        r = get_inexistent_user()
        assert r.status_code == 404, f'Error: status code is incorrect. Expected 404, actual {r.status_code}'