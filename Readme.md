# Diabetes Prediction App

This Streamlit app allows users to predict whether they have diabetes based on their input data.

## How to Use

1. **Input Data**: Fill in the required fields with your information:
   - Pregnancies: Number of pregnancies
   - Glucose rate: Glucose level
   - BloodPressure Rate: Blood pressure level
   - SkinThickness: Skin thickness measurement
   - Insulin: Insulin level
   - BMI: Body Mass Index (BMI)
   - DiabetesPedigreeFunction: Diabetes pedigree function
   - Age: Age in years
   
2. **Test Button**: Click the "Test" button to run the prediction.

3. **Result**: The app will display whether the diabetes test result is positive or negative. If positive, an alert message will be shown, indicating the need to consult a doctor.

## Dependencies

- Python 3.7 or later
- Streamlit
- Pandas
- scikit-learn

## Installation

You can install the required Python packages using pip:

```bash
pip install streamlit pandas scikit-learn

```
### How to Run:
1.Clone the repository:
```bash
git clone https://github.com/yourusername/your-repo.git

```
2.Install dependencies:
```bash
pip install -r requirements.txt
```
3.Run the Streamlit app:
```bash
streamlit run app.py

```