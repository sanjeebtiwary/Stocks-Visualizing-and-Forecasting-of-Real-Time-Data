<<<<<<< HEAD
﻿**Visualising and forecasting stocks**

**Objective**

You will be creating a single-page web application and some machine-learning models which will show company information (logo, registered name and description) and stock plots based on the stock code given by the user. Also, the ML model will enable the user to get predicted stock prices for the data inputted by the user.

**Project Context**

Stock investments provide one of the highest returns in the market. Even though they are volatile in nature, one can visualize share prices and other statistical factors which helps keen investors carefully decide on which company they want to spend their earnings on.

We can make dynamic plots of the financial data of a specific company by using the tabular data provided by the yfinance python library. On top of it, we can use a machine learning algorithm to predict upcoming stock prices.

This project is a good start for beginners in python/data science and a good refresher for professionals who have dabbled in python / ML before. This web application can be applied to any company (whose stock code is available) of one's choosing

**Project Stages**

![Aspose Words 9847ff2d-818d-4a4b-b880-1b5c51072ccf 001](https://user-images.githubusercontent.com/63203112/208687691-c1f6cbd1-f81c-4a7e-a377-48ebe164ecae.png)

![](Aspose.Words.9847ff2d-818d-4a4b-b880-1b5c51072ccf.001.png)

**High-Level Approach**

- Make the main website's structure using mainly HTML Components.
- Enhance the site's UI by styling using CSS
- Generate plots of data using the plotly library of Python. The data is fetched using yfinance python library
- Implement a machine learning model to predict the stock price for the dates requested by the user.
- Deploy the project to host the application.





**Requirements**

- app.py contains the web layout and server function. We will be referring to it as our main file.
- model.py is where we will implement a machine-learning model for forecasting the stock price.
- The assets folder is where we keep our CSS files for styling and any other miscellaneous files like images (if u wish to include them in your site)
- requirements.txt is created so that other developers can install the correct versions of the required Python packages to run your Python code.
- The Procfile is created for deployment. It is not needed to run the app locally.


**Creating the machine learning model**

We are now going to build a machine learning model - Support Vector Regression (SVR) for predicting stock prices.

**Requirements**

- Make the model in the model.py file.
- Use the support vector regression (SVR) module from the sklearn library. Fetch the stock prices for the last 60 days. Split the dataset into 9:1 ratios for training and testing respectively.
- Use the RBF kernel in GridSearchCV for tuning your hyperparameters.
- Then, train the SVR model with the training dataset.
- Test your model's performance by using metrics such as Mean Squared Error (MSE) and Mean Absolute Error (MAE) on the testing dataset.
- After the model is built, make sure another callback function (as seen in Task 2) for the same is made in the main file i.e., app.py (where the model is to be imported).


**Stock data visulaising**

![google stock data visualising_page-0001](https://user-images.githubusercontent.com/63203112/208687737-da41d5d7-0906-4b67-9ca6-455acae2f397.jpg)

![PowerBi file for data visualising_page-0001](https://user-images.githubusercontent.com/63203112/208687773-5aa8017b-54e9-4473-b114-419e6d966c20.jpg)
=======
﻿**Visualising and forecasting stocks**

**Objective**

You will be creating a single-page web application and some machine-learning models which will show company information (logo, registered name and description) and stock plots based on the stock code given by the user. Also, the ML model will enable the user to get predicted stock prices for the data inputted by the user.

**Project Context**

Stock investments provide one of the highest returns in the market. Even though they are volatile in nature, one can visualize share prices and other statistical factors which helps keen investors carefully decide on which company they want to spend their earnings on.

We can make dynamic plots of the financial data of a specific company by using the tabular data provided by the yfinance python library. On top of it, we can use a machine learning algorithm to predict upcoming stock prices.

This project is a good start for beginners in python/data science and a good refresher for professionals who have dabbled in python / ML before. This web application can be applied to any company (whose stock code is available) of one's choosing

**Project Stages**

![Aspose Words 9847ff2d-818d-4a4b-b880-1b5c51072ccf 001](https://user-images.githubusercontent.com/63203112/208687691-c1f6cbd1-f81c-4a7e-a377-48ebe164ecae.png)

![](Aspose.Words.9847ff2d-818d-4a4b-b880-1b5c51072ccf.001.png)

**High-Level Approach**

- Make the main website's structure using mainly HTML Components.
- Enhance the site's UI by styling using CSS
- Generate plots of data using the plotly library of Python. The data is fetched using yfinance python library
- Implement a machine learning model to predict the stock price for the dates requested by the user.
- Deploy the project to host the application.





**Requirements**

- app.py contains the web layout and server function. We will be referring to it as our main file.
- model.py is where we will implement a machine-learning model for forecasting the stock price.
- The assets folder is where we keep our CSS files for styling and any other miscellaneous files like images (if u wish to include them in your site)
- requirements.txt is created so that other developers can install the correct versions of the required Python packages to run your Python code.
- The Procfile is created for deployment. It is not needed to run the app locally.


**Creating the machine learning model**

We are now going to build a machine learning model - Support Vector Regression (SVR) for predicting stock prices.

**Requirements**

- Make the model in the model.py file.
- Use the support vector regression (SVR) module from the sklearn library. Fetch the stock prices for the last 60 days. Split the dataset into 9:1 ratios for training and testing respectively.
- Use the RBF kernel in GridSearchCV for tuning your hyperparameters.
- Then, train the SVR model with the training dataset.
- Test your model's performance by using metrics such as Mean Squared Error (MSE) and Mean Absolute Error (MAE) on the testing dataset.
- After the model is built, make sure another callback function (as seen in Task 2) for the same is made in the main file i.e., app.py (where the model is to be imported).


**Stock data visulaising**

![google stock data visualising_page-0001](https://user-images.githubusercontent.com/63203112/208687737-da41d5d7-0906-4b67-9ca6-455acae2f397.jpg)

![PowerBi file for data visualising_page-0001](https://user-images.githubusercontent.com/63203112/208687773-5aa8017b-54e9-4473-b114-419e6d966c20.jpg)
>>>>>>> 08c624d6cd2a8d13160822991c27d14b9c26ecb6
