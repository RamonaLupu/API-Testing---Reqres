from requests_folder.create_user import create_user

class TestCreateUser():
    def test_create_user(self):
        r = create_user()
        assert r.status_code == 201, f'Error: status code is incorrect. Expected 201, actual {r.status_code}'