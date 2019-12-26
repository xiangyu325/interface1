import requests
payload = {
        "password": "zhangwei@123",
        "platform": 1,
        "tenant_domain": "web",
        "username": "zhangweia"
    }
def gettoken():
    url = "https://t-u1.sancaijia.net/api/v1/user/backyard_login"
    r = requests.post(url, json=payload)
    a = r.json()['data']['token']
    token = "Bearer " + a
    header = {'Authorization': token}
    #print(r.json())
    #print(head)
    return header
print(gettoken())