import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

# read the data in
df = pd.read_json("dataset.json")
# df.convert_objects(convert_numeric=True)

print df.head()
# print df.describe()
# data = df[['cancelled', 'amount', 'cab_service_req', 'is_phone_booking', 'made_on_behalf', 'number_of_rooms',
#  'special_request_made']]

# print data.head()
# print data.describe()
# data.hist()
# # pl.show()
# # data['intercept'] = 1;
# print(data.columns[1:])
# Index([gre, gpa, prestige_2, prestige_3, prestige_4], dtype=object)

# logit = sm.Logit(data['cancelled'], data[train_cols])

# # fit the model
# result = logit.fit()
# print result