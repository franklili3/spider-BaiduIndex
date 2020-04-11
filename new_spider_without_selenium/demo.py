#%%
from get_index import BaiduIndex
import pandas as pd

if __name__ == "__main__":
    keywords = ['比特币']
    baidu_index = BaiduIndex(keywords, '2013-04-01', '2013-04-30')
    baidu_index_all = pd.DataFrame(columns={'keyword', 'type', 'date', 'index'})
    for index in baidu_index.get_index():
        if index['type'] == 'all':
            index_df = pd.DataFrame(index)
            baidu_index_all.append(index_df)


# %%
import requests

url = 'http://www.baidu.com'

resp = requests.get(url=url)
print ('resp', resp.cookies._cookies)
print ('req',  resp.request._cookies._cookies)

# %%
