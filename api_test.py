import requests
from requests.exceptions import HTTPError
from decouple import config
import json
import jsonpath

# Environment variables (.env file)
appKey = config("appKey")
appSecret = config('appSecret')
appUserId = config('appUserId')
appVerifier = config('appVerifier')
oauthToken = config('oauthToken')
oauthSecret = config('oauthSecret')

def getPopularPhotos():

    # Flikr Url
    url = "https://www.flickr.com/services/rest/" 

    # Url Parameters
    p = {
        "method":"flickr.photos.getPopular",
        "api_key":appKey,
        "user_id":appUserId,
        "format":"json"
    }

    try:
        # Get response
        res = requests.get(url,params=p)
        # If the response was successful, no Exception will be raised
        res.raise_for_status()
        # Get content, decoding binary to string
        res_content = res.content.decode('UTF-8')
        # Slicing the string
        v = res_content[14:-1]
        # Converting string to JSON
        df = json.loads(v)
        print(df)
        # Getting value according to specific key
        Photos = jsonpath.jsonpath(df,'photos')
        Status_code = jsonpath.jsonpath(df,'stat')
        try:
            assert res.status_code == 200
            return(f'\n Method : flickr.photos.getPopular \n Photos : {Photos[0]}\n Status code : {res.status_code} {Status_code[0]}\n')
        except HTTPError as http_err:
            return(f"\n Something went wrong \n HTTP error occured : {http_err}")
        except Exception as e:
            print(f'Other error occurred : {e}') 
    except:
        return("Could not connect")
    
print(getPopularPhotos())
