import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Function to display error message for positive diabetes test
def alert():
    st.error("⚠ You Diabetes Test is True! You Need to Consult Doctor")

# Function to display success message for negative diabetes test
def safe():
    st.success("You don't have Diabetes 😊. Feel free!!!")

# Title of the Streamlit app
st.title('Diabetes Prediction')

# Load the diabetes dataset
Diabetes = pd.read_csv('diabetes_dataset.csv')

# Define features (X) and target variable (y) for model training
x = Diabetes[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
              'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = Diabetes['Outcome']

# HTML/CSS for marking fields as required
required_field_html = """
<style>
label:after {
  color: red;
  content: "  *";
}
</style>
"""

# Display the HTML code using markdown to mark fields as required
st.markdown(required_field_html, unsafe_allow_html=True)

# Input fields for user data
Feature1 = st.number_input('Pregnancies', value=None, placeholder='Enter No of Pregnancies', step=1)
Feature2 = st.number_input('Glucose rate', value=None, placeholder='Enter Glucose rate', step=1)
Feature3 = st.number_input('BloodPressure Rate', value=None, placeholder='Enter BloodPressure Rate', step=1)
Feature4 = st.number_input('SkinThickness', value=None, placeholder='Enter SkinThickness', step=1)
Feature5 = st.number_input('Insulin', value=None, placeholder='Enter Insulin rate', step=1)
Feature6 = st.number_input('BMI', value=None, placeholder='Enter BMI Rate', step=0.1)
Feature7 = st.number_input('DiabetesPedigreeFunction', value=None, placeholder='Enter DiabetesPedigreeFunction', step=0.1)
Feature8 = st.number_input('Age', value=None, placeholder='Enter your Age', step=1)

# Check if 'Test' button is clicked
if st.button("Test"):
    # Check if any required field is empty
    if (Feature1 is None or Feature2 is None or Feature3 is None or
            Feature4 is None or Feature5 is None or Feature6 is None or
            Feature7 is None or Feature8 is None):
        st.error("Please fill in all required fields.")
    else:
        # Split the dataset into training and testing sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=2529)
        # Create a Random Forest Classifier model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        # Train the model using the training data
        model.fit(x_train, y_train)
        # Gather user input
        User_Input = [Feature1, Feature2, Feature3, Feature4, Feature5, Feature6, Feature7, Feature8]
        # Make prediction using the Random Forest model
        A = model.predict([User_Input])
        st.write(f"The Diabetes Test is: {A[0]}")  # 1 - True  0 - False
        # Display appropriate message based on prediction result
        if A == 1:
            alert()
        else:
            safe()