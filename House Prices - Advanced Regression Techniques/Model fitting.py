from Model_training import *

# Separate categorical and numeric data
categories_test = test.select_dtypes(include=['object'])
numbers_test = test.select_dtypes(include=['number']).drop(columns=['Id'])

# Fill NaN with mean values for numeric data
imputer.fit(numbers_test)
numbers_test = imputer.transform(numbers_test)
pd.DataFrame(numbers_test)

# Standardise numeric data
numbers_standardised_test = pd.DataFrame(sc.fit_transform(numbers_test))

# Fill NaN with string type for categorical data
categories_test.replace(np.nan, 'NaN')
le = LabelEncoder()
categories_encoded_test = categories_test.apply(le.fit_transform)

processed_test = pd.concat([categories_encoded_test,
                       numbers_standardised_test], axis=1)

# Fit model
x_test = processed_test.iloc[:,:].values

result = pd.DataFrame({'Id': test['Id'], 'SalePrice':regressor.predict(x_test)})
