# pandas的資料結構

Series 和 DataFrame 是非常基本且重要

import pandas as pd #常用好辨識
from pandas import Series, DataFrame #不建議

## Series
- 一維陣列的物件, 包含一個 numpy ndarray (值)及一個資料標籤 index
- 類似有次序, 固定長度的字典型態, 因為index和值都是成對出現

obj=pd.Series(data=[4,7,-5,3]) #一旦由list or tuple輸入形成pd物件之後, 資料變成 numpy ndarray
obj

### 透過Series的values 和index的屬性, 分別取得值和index陣列

obj.values # return <class 'numpy.ndarray'>
obj.index  # default: RangeIndex(start=0, stop=4, step=1)

### 修改index陣列

obj2 = pd.Series(data=obj.values, index=list('dbac'))
obj2.index

### 取值

obj2['a']
mask = ['c','a','d']
obj2[mask]

### 布林陣列過濾資料

mask = obj2 > 0
obj2[mask]

### 純量乘法

obj2 * 2

### 數學函式運算
- Numpy 函式或類似Numpy 運算,都會保存其index和值的連結關係

import numpy as np
np.exp(obj2)

'b' in obj2
# 'e' in obj2

### dict型態來建立Series物件
- key的部分就是index, value的部分就是資料值

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
obj3

### 修改index
- Series中的資料以index來決定排序, 因此index另外傳入時, Series的資料順序也會改變

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
obj4

### 偵測遺失資料

#'NaN': not a number, 'NA': Not available
pd.isnull(obj4)

pd.notnull(obj4)

obj4.isnull() #Series物件本身也有同樣的實例方法
#obj4.notnull()

### 運算後自動對齊
- elementwise運算
- dtype也會自動統一

print(obj3)
print(obj4)
obj3+obj4 #比擬資料庫結合(join)動作

### name屬性
- 可針對Series 物件和它內部index命名

print(obj4)
obj4.name = 'population'
obj4.index.name= 'state'
obj4


### 更改index

print(obj)
name = ['Bob','Steve', 'Jeff', 'Ryan']
obj.index = name
obj

## $$ DataFrame $$
- 每個欄位可能是不同型態(數字, 字串, 布林)
- 二維形式
- 想像是一個dict物件(data), 是由許多Series物件組成的

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada','Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data) #index自動派定
frame

### 顯示某幾列
- 遇到大型DataFrame,不需全部都顯示

frame.head()    #default:前五筆記錄
frame.tail()    #default:後五筆紀錄
frame.head(3)   #前三筆紀錄
frame.sample(2) #亂數取樣數

### 欄位指定
- 欄位順序同時也會按指定順序排好(由左到右)

pd.DataFrame(data, columns=['year','state','pop'])

#若欄位不在data的話, 則會以NaN值的方法顯示
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five','six'])
frame2

### 屬性呼叫欄位(行標籤)

frame2.columns

### 屬性呼叫索引(列標籤)

frame2.index

### 屬性呼叫資料值

frame2.values

### dict 方法顯示特定欄位

print(frame2['state'])

### 屬性呼叫某欄位

frame2.year

### 修改某欄位值

frame2['debt'] = 16.5 #常數值
frame2

frame2['debt'] = np.arange(6) #陣列值
frame2

val = pd.Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five']) #Series物件
frame2['debt'] = val
frame2

mask = (frame2.state =='Ohio')
frame2['eastern'] = mask  # boolean mask
frame2

### 用frame2.eastern這樣的語法無法建立新欄位

### 刪除行欄位

del frame2['eastern']

frame2.columns

### dict的巢式結構
- 外層的dict key解讀為欄位標籤
- 內層的dict key解讀為索引標籤

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
frame3

### 欄位、索引標籤互換

frame3.T

frame3.index.name='year';frame3.columns.name='state'
frame3

frame2.values #如果DataFrame的欄位dtype不同的話,哪就會選定可以滿足所有欄位的dtype

# $$重要功能$$ 

### 重作索引(reindex)

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj

obj2 = obj.reindex(['a','b','c','d','e'])
obj2

obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0) #fillna值

obj3 = pd.Series(['blue','purple','yellow'], index=[0, 2, 4])
obj3

obj3.reindex(range(6), method='ffill')

### 對列進行reindex

frame = pd.DataFrame(np.arange(9).reshape(3,3), index=['a','c','d'],
                     columns= ['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(list('abcd'))
frame2

### 對欄進行reindex

print(frame)
states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)

### 指定軸刪除資料

obj = pd.Series(np.arange(5.), index=list('abcde'))
print(obj)
obj.drop('c')

obj.drop(['d','c'])

### 兩軸都可以指定index來刪除資料

data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data

data.drop(['Colorado','Ohio']) # default: axis=0

data.drop(['two'], axis=1)

### inplace 就地植入，不建立新物件 (化學變化)

obj.drop('c', inplace=True) # default:(inplace=False), (物理變化)
obj

### 索引、選擇和過濾

#### Series做索引和numpy array的索引很類似，差別在Series可用index值，不用一定要是整數

## Series和numpy的索引很類似
obj = pd.Series(np.arange(4.), index=list('abcd'))
print(obj)
obj['b']

obj[1]

obj[2:4]

obj[['']]