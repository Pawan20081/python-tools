import streamlit as st
import math

st.title("Quadratic Equation Solver")

a = st.number_input("Enter value of a:")
b = st.number_input("Enter value of b:")
c = st.number_input("Enter value of c:")

if st.button("Solve"):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        st.success(f"Two Real Roots: {root1} and {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        st.success(f"One Real Root: {root}")
    else:
        st.warning("No Real Roots (Complex roots)")