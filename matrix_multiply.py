import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.title("🔢 Matrix Multiplication Visualization")
    st.write("See how a 2×2 matrix transforms vectors.")

    # Sidebar input
    matrix = np.zeros((2, 2))
    matrix[0, :] = list(map(float, st.sidebar.text_input("Row 1", "1,0").split(',')))
    matrix[1, :] = list(map(float, st.sidebar.text_input("Row 2", "0,1").split(',')))

    # Original vectors
    v1 = np.array([1, 0])
    v2 = np.array([0, 1])

    # Apply transformation
    v1_t = matrix @ v1
    v2_t = matrix @ v2

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.axhline(0, color='gray', lw=1)
    ax.axvline(0, color='gray', lw=1)

    # Original basis vectors
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label="Original i")
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='green', label="Original j")

    # Transformed vectors
    ax.quiver(0, 0, v1_t[0], v1_t[1], angles='xy', scale_units='xy', scale=1, color='red', label="Transformed i'")
    ax.quiver(0, 0, v2_t[0], v2_t[1], angles='xy', scale_units='xy', scale=1, color='orange', label="Transformed j'")

    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
