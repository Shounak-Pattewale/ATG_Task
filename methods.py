# Resource : https://reqres.in/
import json
import requests
import jsonpath

# get method
def get(page):
    url = "https://reqres.in/api/users"

    try:
        res = requests.get(url, params={"page": page})
        json_data = res.json()
        df = {
            "Page": jsonpath.jsonpath(json_data, "page")[0],
            "User id": jsonpath.jsonpath(json_data, "data")[0][0]["id"],
            "Full name": jsonpath.jsonpath(json_data, "data")[0][0]["first_name"]+" "+jsonpath.jsonpath(json_data, "data")[0][0]["last_name"],
            "Email": jsonpath.jsonpath(json_data, "data")[0][0]["email"]
        }
    except:
        return "Site not reachable"

    try:
        assert res.status_code == 200
        return json.dumps(df)
    except:
        return (f'Something went wrong \nStatus code : {res.status_code}')

# post method
def post(data):
    url = "https://reqres.in/api/users"

    try:
        res = requests.post(url, data)
        json_data = res.json()
        print("id : ",json_data['id'],"\nCreated at : ",json_data['createdAt'])

    except:
        return "Site not reachable"

    try:
        assert res.status_code == 201
        return "Data added successfuly"
    except:
        return (f'Something went wrong \nStatus code : {res.status_code}')


# delete method
def delete(uid):
    url = "https://reqres.in/api/users/"+str(uid)

    try:
        res = requests.delete(url)
    except:
        return "Site not reachable"

    try:
        assert res.status_code == 204
        return "Data deleted successfuly"
    except:
        return (f'Something went wrong \nStatus code : {res.status_code}')


data = {
    "name": "ABC",
    "job": "Data Scientist"
    }

# function calls

print("\nGET METHOD")
print("Message : ",get(2))

print("\nPOST METHOD")
print(post(json.dumps(data)))

print("\nDELETE METHOD")
print(delete(159),"\n")
