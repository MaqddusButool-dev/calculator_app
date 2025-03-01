import streamlit as st

def main():
    st.title("Simple Calculator")
    
    # Input fields for numbers
    num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
    num2 = st.number_input("Enter second number", value=0.0, format="%.2f")
    
    # Operation selection
    operation = st.radio("Select operation:", ("Addition", "Subtraction", "Multiplication", "Division"))
    
    result = None
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed.")
    
    if result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()






# st.title('BML CALCULATOR')
# st.markdown('This app is for calculating your BMI')
# st.write('Please enter your weight and height in the sidebar' )
# weight = st.sidebar.number_input('Enter your weight (in kg)')
# height = st.sidebar.number_input('Enter your height (in cm)')
# if st.button('Calculate BMI'): #(calculate BML):
#     bmi = weight / ((height/100)**2)
#     st.write('Your BMI is:', bmi)

#     if bmi < 18.5:
#         st.write('You are underweight')
#     elif bmi < 25:
#         st.write('You are normal weight')
#     else:
#         st.write('You are overweight')







# if st.button('Save'):
#     st.write('Button clicked')

# #slider added
# age = st.slider('Select your age', 0, 100, 25)
# st.write('Your age is:', age)

# # add lodedata 
# import pandas as pd
# df = pd.DataFrame({
#     'Name': ['John', 'Jane', 'Bob'],
#     'Age': [30, 28, 25]
# })
# st.dataframe(df)
# #make line chart od data
# import matplotlib.pyplot as plt
# plt.plot(df['Name'], df['Age'])
# st.pyplot()
