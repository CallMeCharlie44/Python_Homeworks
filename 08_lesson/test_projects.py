from config import APIconfig


api = APIconfig()

def test_create_project():
    resp = api.create_poject("Api project")
    assert resp.status_code == 201
    assert resp.json()["id"] is not None

def test_get_project():
    resp = api.create_poject("Api project")
    id = resp.json()["id"]
    get_resp = api.get_poject(id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Api project"

def test_create_project_negative():
    resp = api.create_poject("")
    assert resp.status_code == 400
    assert resp.json()["message"][0] == "title should not be empty"  


def test_update_title_project():
    id = "fa637221-4082-4539-9e90-b8deee7770b9"
    new_title = "New Api Project"
    resp = api.update_title_project(new_title, id)
    get_resp = api.get_poject(id)
    assert get_resp.json()["title"] == new_title
    