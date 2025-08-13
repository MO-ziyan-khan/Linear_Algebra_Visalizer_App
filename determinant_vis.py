import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.title("📐 Determinant & Area Change")
    st.write("See how the determinant scales area in 2D.")

    matrix = np.zeros((2, 2))
    matrix[0, :] = list(map(float, st.sidebar.text_input("Row 1", "1,0").split(',')))
    matrix[1, :] = list(map(float, st.sidebar.text_input("Row 2", "0,1").split(',')))

    square = np.array([[0, 1, 1, 0], [0, 0, 1, 1]])
    transformed_square = matrix @ square

    det = np.linalg.det(matrix)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.axhline(0, color='gray', lw=1)
    ax.axvline(0, color='gray', lw=1)

    ax.fill(square[0], square[1], alpha=0.3, label="Original Unit Square", color="lightblue")
    ax.fill(transformed_square[0], transformed_square[1], alpha=0.5, label=f"Transformed Square (Area ×{abs(det):.2f})", color="salmon")

    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
