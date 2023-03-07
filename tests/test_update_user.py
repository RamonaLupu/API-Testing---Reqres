from requests_folder.update_user import update_user

class TestUpdateUser():
    def test_update_user(self):
        r = update_user()
        assert r.status_code == 200, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'