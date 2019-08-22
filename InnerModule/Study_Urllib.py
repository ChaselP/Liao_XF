from urllib import request

def fetch_data(url):
    import json
    with request.urlopen(url) as f:
        return json.loads(f.read().decode('utf-8'))

URL = 'http://news-at.zhihu.com/api/4/news/latest'
# 测试
data = fetch_data(URL)
print(data)
#assert data['query']['results']['channel']['location']['city'] == 'Beijing'
assert data['stories'][0]['type']==0
print('ok')