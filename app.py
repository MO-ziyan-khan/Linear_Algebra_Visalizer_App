import streamlit as st
import determinant_vis
import grid_transform
import matrix_multiply
import shear_transformation
import line_equation

# Sidebar navigation
st.sidebar.title("Linear Transformation Visualizer")
page = st.sidebar.radio(
    "Choose a visualization:",
    ("Matrix Multiplication", "Grid Transformation", "Shear Transformation", "Determinant Visualization", "Line Equation")
)

# Title
st.title("✨ Linear Algebra Visualization App")

# Call the correct visualization
if page == "Matrix Multiplication":
    matrix_multiply.app()
elif page == "Grid Transformation":
    grid_transform.app()
elif page == "Shear Transformation":
    shear_transformation.app()
elif page == "Determinant Visualization":
    determinant_vis.app()
elif page == "Line Equation":
    line_equation.app()