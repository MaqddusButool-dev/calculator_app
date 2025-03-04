import streamlit as st
import numpy as np
import sympy as sp

def main():
    st.set_page_config(page_title="Advanced Calculator", page_icon="🔢", layout="centered")
    
    st.markdown(
        """
        <style>
            .stButton button {
                width: 100%;
                height: 50px;
                font-size: 20px;
                font-weight: bold;
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
            }
            .stButton button:hover {
                background-color: #45a049;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🔢 Advanced Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, step=0.1, format="%.2f")
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, step=0.1, format="%.2f")
    
    operations = {
        "➕ Addition": np.add, 
        "➖ Subtraction": np.subtract, 
        "✖️ Multiplication": np.multiply, 
        "➗ Division": np.divide,
        "^ Power": np.power,
        "% Modulus": np.mod
    }
    
    operation = st.radio("Select operation", list(operations.keys()))
    
    if st.button("Calculate"):
        try:
            result = operations[operation](num1, num2)
            st.success(f"Result: {result}")
        except ZeroDivisionError:
            st.error("Error: Division by zero is not allowed.")
    
    with st.expander("ℹ️ Advanced Functions"):
        adv_col1, adv_col2 = st.columns(2)
        
        with adv_col1:
            if st.button("Square Root of First Number"):
                if num1 >= 0:
                    st.success(f"√{num1} = {np.sqrt(num1):.4f}")
                else:
                    st.error("Error: Cannot compute square root of a negative number.")
            
            if st.button("Logarithm (Base 10) of First Number"):
                if num1 > 0:
                    st.success(f"log10({num1}) = {np.log10(num1):.4f}")
                else:
                    st.error("Error: Logarithm is undefined for non-positive values.")
        
        with adv_col2:
            if st.button("Power (First ^ Second)"):
                st.success(f"{num1}^{num2} = {np.power(num1, num2):.4f}")
            
            if st.button("Factorial of First Number"):
                if num1 >= 0 and num1 == int(num1):
                    st.success(f"{int(num1)}! = {np.math.factorial(int(num1))}")
                else:
                    st.error("Error: Factorial is only defined for non-negative integers.")
    
    with st.expander("📈 Algebraic and Trigonometric Functions"):
        expression = st.text_input("Enter an algebraic expression (e.g., x^2 + 2*x + 1)")
        variable = st.text_input("Enter the variable (default: x)", value="x")
        if st.button("Differentiate"):
            try:
                x = sp.symbols(variable)
                derivative = sp.diff(expression, x)
                st.success(f"Derivative: {derivative}")
            except Exception as e:
                st.error(f"Error: {e}")
        
        if st.button("Integrate"):
            try:
                x = sp.symbols(variable)
                integral = sp.integrate(expression, x)
                st.success(f"Integral: {integral}")
            except Exception as e:
                st.error(f"Error: {e}")
        
        angle = st.number_input("Enter angle in degrees", value=0.0, step=1.0)
        trig_functions = {"sin": np.sin, "cos": np.cos, "tan": np.tan}
        trig_choice = st.selectbox("Select trigonometric function", list(trig_functions.keys()))
        if st.button("Compute Trigonometric Value"):
            angle_rad = np.radians(angle)
            result = trig_functions[trig_choice](angle_rad)
            st.success(f"{trig_choice}({angle}°) = {result:.4f}")
    
    st.markdown("---")
    st.write("Created with ❤️ using Streamlit")
    
if __name__ == "__main__":
    main()
