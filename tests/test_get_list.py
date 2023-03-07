from requests_folder.get_list import get_list

class TestGetList():
    def test_list_resource(self):
        r = get_list("")
        assert r.status_code == 200, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'

    def test_single_resource(self):
        r = get_list("2")
        assert r.status_code == 200, f'Error: status code is incorrect. Expected 200, actual {r.status_code}'

    def test_single_resource_not_found(self):
        r = get_list("23")
        assert r.status_code == 404, f'Error: status code is incorrect. Expected 404, actual {r.status_code}'