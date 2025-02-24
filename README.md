## Stock Forecasting Using LSTM

### Software and Tools Requirements

1. [Github Account](https://github.com)
2. [Streamlit](https://streamlit.io/cloud)
3. [VSCodeIDE](HTTPS://code.visualstudio.com/)
4. [AnacondaPrompt](https://anaconda.org/anaconda/anaconda_prompt)

### Installation Instructions

Create a new environment 

```python
conda create --name timeseries python==3.10 -y
```
Clone the repository:
```python
git clone  https://github.com/richardmukechiwa/AppleStockTimeSeries.git
```
Navigate to the project directory
```python
cd C:\Users\RICH-FILES\Desktop\ml\AppleStockTimeSeries
```
Open the VS code 
```python
(base) C:\Users\RICH-FILES\Desktop\ml\AppleStockTimeSeries>code .
```

### Project Overview

This project focuses on building a Long Short-Term Memory (LSTM) model to forecast the closing stock prices of a company based on historical market data. The model helps in understanding price trends and provides insights for better financial decision-making.

### Problem Statement

Stock price prediction is a challenging task due to the noisy, volatile, and non-linear nature of the market. Traditional models struggle to capture sequential dependencies, making LSTMs an ideal choice. The dataset contains   Apple historical stock data with features such as:

- Date

- Open

- High

- Low

- Close (Target variable for prediction)

- Volume

- Dividends

- Stock Splits

### Key Features

- Time-Series Forecasting: Uses LSTM to predict future stock prices.

- Data Preprocessing: Min-max scaling to normalize data.

- Model Training: Trained using recent stock data to improve accuracy.

- Evaluation: RMSE (Root Mean Squared Error) used to assess model performance.

- Model Saving and Loading: Implemented using joblib for easier deployment.

### Technologies Used

- Python

- TensorFlow/Keras

- Pandas

- NumPy

- Matplotlib

- Scikit-learn

- Joblib

### Usage Guidelines

- Ensure the dataset (Apple.csv) is available in the correct directory.

- Run the notebook step-by-step to preprocess the data, train the model, and make predictions.

- Modify the window_size variable to adjust the sequence length for LSTM.

- Load the saved model using:

- from joblib import load
  model = load("model.keras")

### Challenges Faced and Solutions

- Model Performance Issues: Initially, the model performed well on training data but failed on test data.

- Solution: Reduced the dataset to more recent data, as older data (before 2000) had significantly lower prices, causing trend differences.

- Saving and Loading Model Issues: Faced difficulties in efficiently saving and loading the trained model.

- Solution: Used joblib to ensure the model could be easily saved and restored without errors.

### Future Improvements

- Experiment with Different Variables: Instead of predicting Close price, explore predictions for Open, High, or Volume.

- Hyperparameter Tuning: Optimize LSTM architecture using techniques like Grid Search or Bayesian Optimization.

- Try Different Models: Explore alternative deep learning models such as GRU or Transformers for improved accuracy.

- Deploy Model: Develop a Flask or Streamlit web application for real-time stock price predictions.

### Results and Evaluation

The trained LSTM model achieved a validation RMSE of 0.0126, indicating a good fit for recent stock price trends.

Model predictions were plotted against actual values to visually assess accuracy.

### Contributing

- Fork the repository and create a new branch for your changes.

- Commit your changes and create a pull request.

- Suggestions and improvements are welcome!

### License

This project is licensed under the MIT License. Feel free to use and modify the code.

__Author: Richard Mukechiwa__
