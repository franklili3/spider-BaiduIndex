#%%
from get_index import BaiduIndex
import pandas as pd

#if __name__ == "__main__":
keywords = ['比特币']
baidu_index = BaiduIndex(keywords, '2013-04-01', '2014-04-30')
baidu_index_dict = {'keyword': [], 'type': [], 'date': [], 'index': []}
for index in baidu_index.get_index():
    #print(index)
    if index['type'] == 'all':
        baidu_index_dict['keyword'].append(index['keyword'])
        baidu_index_dict['type'].append(index['type'])
        baidu_index_dict['date'].append(index['date'])
        baidu_index_dict['index'].append(index['index'])

baidu_index_df = pd.DataFrame(baidu_index_dict)
