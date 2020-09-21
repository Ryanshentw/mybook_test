# p7-19
## Boston, regression 

from sklearn import datasets 
import numpy as np
import matplotlib.pyplot as plt

boston=datasets.load_boston()
X_org, yt=boston.data, boston.target
feature_names=boston.feature_names
print(X_org.shape, yt.shape)
print(feature_names)

X_data=X_org[:, feature_names=='RM']
X=np.insert(X_org, 0, 1.0, axis=1)
print(X[:10])
print(X.shape)