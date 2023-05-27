# Car Price Prediction
## Content
- Data Cleaning (Identifying null values, filling missing values and removing outliers)
- Some insights from data
- Data Preprocessing (Standardization or Normalization)
- ML Models: Linear Regression, Ridge Regression, Lasso, Random Forest Regressor and XGBoost Regressor
- Comparison of the performance of the models
- Dumping the Model which gives Best Results
- Loading Dumped Model to deploy on/as a Webpage.

### Some Key Concepts
- The Data:
The dataset used in this project was downloaded from <a href="https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge" target="_blank">Kaggle.</a>

- Data Cleaning:
The first step is to remove duplicate/null values from the dataset.

- Insights from Dataset, you can check <a href="https://github.com/shaikh-7abish/Car_Price_Prediction/blob/main/app/data_preprocessing.ipynb">Data Preprocessing</a> file.
  - There are many duplicates values, we need to remove it
  - Mileage column has a "km" attached with it's value
  - Price column have very disturbed data
  - 'Manufacturer' column has "სხვა" value in it
  - Replace '-' values with mean in 'Levy' column
  - 'Cylinders' column has values lesser than 4 which is not expected
  - Engine volume have 'Turbo' in certain values, need separate column for Turbo
  - Change '4x4' values in 'Drive wheels' column
  - Channge the values in 'Doors' column
  - Remove the 'Hydrogen' value from 'Fuel type' column

- Some insights from the dataset <a href="https://github.com/shaikh-7abish/Car_Price_Prediction/blob/main/app/EDA.ipynb">Exploratory Data Analysis.</a>: 
Some values are present very much in dataset like Sedan, Petrol, Automatic, Black, White.

- <a href="https://github.com/shaikh-7abish/Car_Price_Prediction/blob/main/app/EDA.ipynb">Data preprocessing</a>:
  - One Hot Encoder
  - Normalization
  - Train the data

- <a href="https://github.com/shaikh-7abish/Car_Price_Prediction/blob/main/app/models.ipynb">ML Models</a>:
In this section, different machine learning algorithms are used to predict price/target-variable. And the result of Random Forest Regressor is `R2 Score:  0.7742242930508028 , MAE:  0.3168989547306263` which is good. Later dumped it with pickle module for further usage.

- <a href="https://github.com/shaikh-7abish/Car_Price_Prediction/blob/main/app.ipynb">Deployment of Pretrained Model</a>:
Then we used Flask for deployment of our model in <a href="https://github.com/shaikh-7abish/Car_Price_Prediction/blob/main/app.ipynb">app.ipynb</a> and use it on <a href="https://github.com/shaikh-7abish/Car_Price_Prediction/blob/main/templates/main.html">webpage</a>

## To use the Model
- first, Unzip the `model.zip` file in  <a href="https://github.com/shaikh-7abish/Car_Price_Prediction/blob/main/models/model.zip">models</a> folder.
- I recommend to install the following packages in the your anaconda environment

    - "numpy" package : `pip install numpy` command.
    - "pandas" package : `pip install pandas` command.
    - "matplotlib" package : `pip install matplotlib` command.
    - "seaborn" package : `pip install seaborn` command.
    - "pickle" package : `pip install pickle` command.
    - "sklearn" package : `pip install sklearn` command.
    - "flask" package : `pip install flask` command.
   
- Run the `app.ipynb` in the anaconda prompt / jupyter notebook using `python3 app.ipynb` then open the web-address displayed below.
