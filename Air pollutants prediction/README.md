<H1> Tabular Playground Series - Jul 2021 </H1>
  Predict air pollutants from time-series data<br>
  from: https://www.kaggle.com/competitions/tabular-playground-series-jul-2021/data
  
<H2> Competition Description: </H2>
In this competition you are predicting the values of air pollution measurements over time, based on basic weather information (temperature and humidity) and the input values of 5 sensors.


<H2> Conclusions and reflections: </H2>
Kaggle score: 0.41696<br><br>

Initially time series analysis approach was tested, among SARIMA, VMA and VAR models, the result produced by the VAR model was more reasonable, and turns out despite both independent and dependent variables demonstrate time series properties (stationarity) after data preprocessing, models were not able to pick up patterns and make satisfactory predictions. Surprisingly, multiple linear regression model was able to outperform mentioned time series models significantly, it was then used for both carbon monoxide and benzene prediction, while nitrogen oxides prediction used polynomial regression model of degree=4 to make slightly better predictions.
