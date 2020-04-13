#%%
from get_index import BaiduIndex
import pandas as pd

#if __name__ == "__main__":
keywords = ['bitcoin']
baidu_index = BaiduIndex(keywords, '2013-04-01', '2013-04-30')
baidu_index_dict = {'keyword': [], 'type': [], 'date': [], 'index': []}
for index in baidu_index.get_index():
    print(index)
'''     if index['type'] == 'all':
        baidu_index_dict['keyword'].append(index['keyword'])
        baidu_index_dict['type'].append(index['type'])
        baidu_index_dict['date'].append(index['date'])
        baidu_index_dict['index'].append(index['index'])
 '''
        


# %%
import requests

url = 'http://www.baidu.com'

resp = requests.get(url=url)
print ('resp', resp.cookies._cookies)
print ('req',  resp.request._cookies._cookies)

# %%
