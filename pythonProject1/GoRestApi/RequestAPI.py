import requests
import random
import json
import string

# Base Url:
Base_url = "https://gorest.co.in"

#Auth_token:
auth_token = "Bearer d6bee83c57e59bf95929a41ae66328900da7fbe0d472d43079f7440a78272681"

#Random_email_generator_method:
def email_generator():
    domain = "gmail.com"
    email_lenght = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_lenght))
    email = random_string +"@"+ domain
    print("email is : ", email)
    return email


#Get request:
def get_request():
    url= Base_url + "/public/v2/users"
    print("get url:", url)
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response: ", json_data)
    print("....GET user is done....")
    print("....================....")


#POST request:
def post_request():
    url = Base_url + "/public/v2/users"
    print("Post url:", url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "rohit sharma",
        "email": email_generator(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response: ", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "rohit sharma"
    print("....User is Craeted....")
    print("....=================....")
    return user_id


#PUT request:
def PUT_request(user_id):
    url = Base_url + f"/public/v2/users/{user_id}"
    print("Post url:", url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "john doe ind",
        "email": email_generator(),
        "gender": "male",
        "status": "inactive"
    }
    resposne = requests.put(url, json=data, headers=headers)
    assert resposne.status_code == 200
    json_data = resposne.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["status"] == "inactive"
    print("....User details is updated ....")
    print("....=======================....")

#DELETE request:
def Delete_request(user_id):
    url= Base_url + f"/public/v2/users/{user_id}"
    print("Delete Url:", url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code ==204
    print("....User is Deleted....")
    print("....===============....")


#calling method"
get_request()
user_id = post_request()
PUT_request(user_id)
Delete_request(user_id)