from requests_folder.delete_user import delete_user

class TestDeleteUser():
    def test_delete_user(self):
        r = delete_user()
        assert r.status_code == 204, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'