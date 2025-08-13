import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.title("↗ Shear Transformation")
    st.write("Visualize how shear matrices work.")

    shear_x = st.sidebar.slider("Shear in X", -3.0, 3.0, 1.0, 0.1)
    shear_y = st.sidebar.slider("Shear in Y", -3.0, 3.0, 0.0, 0.1)

    matrix = np.array([[1, shear_x], [shear_y, 1]])

    square = np.array([[0, 1, 1, 0], [0, 0, 1, 1]])
    transformed_square = matrix @ square

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.axhline(0, color='gray', lw=1)
    ax.axvline(0, color='gray', lw=1)

    ax.fill(square[0], square[1], alpha=0.3, label="Original", color="lightblue")
    ax.fill(transformed_square[0], transformed_square[1], alpha=0.5, label="Sheared", color="gold")

    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
