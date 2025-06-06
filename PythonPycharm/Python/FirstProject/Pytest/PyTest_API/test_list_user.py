import pytest
import requests
import json


@pytest.mark.parametrize("userid, firstname", [(1, "George"), (2, "Janet")])
def test_list_valid_user(supply_url, userid, firstname):
    url = supply_url + "/users/" + str(userid)
    resp = requests.get(url,verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text
    assert j['data']['id'] == userid, resp.text
    assert j['data']['first_name'] == firstname, resp.text


def test_list_invalid_user(supply_url):
    url = supply_url + "/users/50"
    resp = requests.get(url, verify=False)
    assert resp.status_code == 404, resp.text
