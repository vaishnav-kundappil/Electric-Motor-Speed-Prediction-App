Electric Motor Speed Prediction

Overview

Electric Motor Speed Prediction is a machine learning-based project designed to estimate the rotational speed of an electric motor based on various input parameters. The project utilizes real-world data and predictive modeling techniques to enhance efficiency, control, and maintenance of electric motors.

Features

Predicts electric motor speed based on sensor data

Utilizes machine learning algorithms for accurate estimations

Supports real-time or batch processing

Helps in preventive maintenance and efficiency optimization

Technologies Used

Python

Scikit-learn 
Pandas, NumPy, Matplotlib

Jupyter Notebook  Streamlit (for visualization, if applicable)

Dataset

The model is trained on a dataset containing sensor readings and motor parameters such as

Voltage

Current

Torque

Temperature

Rotational speed (target variable)

Installation

To set up the project locally, follow these steps

# Clone the repository
git clone httpsgithub.comvaishnav-kundappilElectric-Motor-Speed-Prediction-App
cd electric-motor-speed-prediction

# Create a virtual environment
python -m venv venv
source venvbinactivate  # On Windows use `venvScriptsactivate`

# Install dependencies
pip install -r requirements.txt

Usage

Run the following command to train and test the model

python train.py  # Train the model
python predict.py --input data.csv  # Make predictions

Model Performance

The model achieves high accuracy based on evaluation metrics such as

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R-squared (R²)

Contributions

Contributions are welcome! Please open an issue or submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

