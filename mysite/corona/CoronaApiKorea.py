import requests, json

key = "492ec27592a4538a675a169c6e075cc5e"
url = "http://api.corona-19.kr/korea/?serviceKey={}".format(key)

content = requests.get(url).content
Korea_json = json.loads(content)
print(Korea_json)