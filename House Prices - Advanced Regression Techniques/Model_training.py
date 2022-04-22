import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
pd.set_option('display.max_columns', None)

source = 'FILE LOCATION'
test = pd.read_csv(source + 'test.csv')
train = pd.read_csv(source + 'train.csv')

# separate categories and numeric values
categories = train.select_dtypes(include=['object'])
numbers = train.select_dtypes(include=['number']).drop(columns=['SalePrice', 'Id'])

# Fill missing values
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(numbers)
numbers = imputer.transform(numbers)
pd.DataFrame(numbers)

# Standardise numeric columns
sc = StandardScaler()
numbers_standardised = pd.DataFrame(sc.fit_transform(numbers))

# Encode categorical data
categories.replace(np.nan, 'NaN')
le = LabelEncoder()
categories_encoded = categories.apply(le.fit_transform)

processed = pd.concat([categories_encoded, numbers_standardised], axis=1)

# Train model
y = train['SalePrice'].values
x = processed.iloc[:,:].values

regressor = RandomForestRegressor(n_estimators = 45, random_state = 0)
regressor.fit(x, y)






