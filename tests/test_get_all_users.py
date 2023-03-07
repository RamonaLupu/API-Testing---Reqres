from requests_folder.get_all_users import get_all_users

class TestGetAllUsers():
    def test_get_all_users(self):
        r = get_all_users()
        assert r.status_code == 200, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'