import requests
import json

_json = {
    "name": "morpheus",
    "job": "leader"
}
__resCode = '[201]'
def postMethod(url):
    resStatus = requests.post(url, _json)
    resText = requests.Response.json(resStatus)
    if __resCode in str(resStatus):
        print('Response code is: "{}", Create method is successfully executed'.format(__resCode))
        print('json response is: "{}"'.format(resText))

postMethod('https://reqres.in/api/users')
