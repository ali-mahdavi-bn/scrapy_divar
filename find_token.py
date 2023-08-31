import requests

url = 'https://api.divar.ir/v8/web-search/1/apartment-rent'

json = {"json_schema": {"category": {"value": "apartment-sell"}},
        "last-post-date": 1693514609572940}
headers = {
    "Content-Type": "application/json"
}

res = requests.post(url, json=json, headers=headers)
data = res.json()
last_post_date = data['last_post_date']

list_of_tokens = []

count = 0
while True:

    json = {"json_schema": {"category": {"value": "apartment-sell"}},
            "last-post-date": last_post_date}

    res = requests.post(url, json=json, headers=headers)
    data = res.json()
    last_post_date = data['last_post_date']

    for widget in data["web_widgets"]["post_list"]:
        token = widget['data']['token']
        list_of_tokens.append(token)
        count += 1
        print(token)

    if count >= 30:
        break
print(list_of_tokens)
txt_file = open('tokens.txt', 'w', encoding='utf8')
txt_file.write(','.join(list_of_tokens))
txt_file.close()
