import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def draw_grid(ax, lines, line_color="blue", alpha=1.0, label=None):
    for i, (start, end) in enumerate(lines):
        ax.plot([start[0], end[0]], [start[1], end[1]], color=line_color, alpha=alpha, zorder=1, label=label if i == 0 else None)

def generate_grid(num_lines=10):
    grid_lines = []
    xs = np.linspace(-num_lines, num_lines, 2*num_lines + 1)
    ys = np.linspace(-num_lines, num_lines, 2*num_lines + 1)
    for x in xs:
        grid_lines.append((np.array([x, -num_lines]), np.array([x, num_lines])))  # vertical
    for y in ys:
        grid_lines.append((np.array([-num_lines, y]), np.array([num_lines, y])))  # horizontal
    return grid_lines

def app():
    st.header("Grid Linear Transformation Visualizer")

    with st.sidebar:
        st.markdown("### Transformation Matrix (2x2)")
        row1 = st.text_input("Row 0 (comma separated)", value="1,0")
        row2 = st.text_input("Row 1 (comma separated)", value="0,1")

        show_vector = st.checkbox("Show Vector", value=True)
        if show_vector:
            vx = st.number_input("Vector x", value=1.0)
            vy = st.number_input("Vector y", value=1.0)

        show_unit = st.checkbox("Show Unit Vectors (i, j)", value=True)

        transform = st.button("Transform")

    try:
        matrix = np.array([list(map(float, row1.split(','))), list(map(float, row2.split(',')))])
        assert matrix.shape == (2, 2)
    except Exception:
        st.error("Invalid matrix input! Please enter two rows of 2 numbers separated by commas.")
        return

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal', 'box')
    ax.grid(True, linestyle='--', alpha=0.3)

    grid_lines = generate_grid()

    # Draw original grid
    draw_grid(ax, grid_lines, line_color="lightblue", alpha=0.8, label="Original Grid")

    if transform:
        # Draw transformed grid
        transformed_lines = [(matrix @ start, matrix @ end) for start, end in grid_lines]
        draw_grid(ax, transformed_lines, line_color="coral", alpha=0.8, label="Transformed Grid")

        if show_vector:
            v = np.array([vx, vy])
            tv = matrix @ v
            ax.arrow(0, 0, v[0], v[1], color='green', linewidth=3, head_width=0.3, label='Original Vector')
            ax.arrow(0, 0, tv[0], tv[1], color='purple', linewidth=3, head_width=0.3, label='Transformed Vector')

        if show_unit:
            # Original unit vectors
            ax.arrow(0, 0, 1, 0, color='black', linewidth=2, linestyle='--', head_width=0.15, label='Unit Vectors')
            ax.arrow(0, 0, 0, 1, color='black', linewidth=2, linestyle='--', head_width=0.15)
            ax.text(1, 0, "i", fontsize=14)
            ax.text(0, 1, "j", fontsize=14)

            # Transformed unit vectors
            ti = matrix @ np.array([1,0])
            tj = matrix @ np.array([0,1])
            ax.arrow(0, 0, ti[0], ti[1], color='brown', linewidth=2, head_width=0.15, label='Transformed Unit Vectors')
            ax.arrow(0, 0, tj[0], tj[1], color='brown', linewidth=2, head_width=0.15)
            ax.text(ti[0], ti[1], "i'", fontsize=14)
            ax.text(tj[0], tj[1], "j'", fontsize=14)

    else:
        if show_vector:
            ax.arrow(0, 0, vx, vy, color='green', linewidth=3, head_width=0.3, label='Original Vector')
        if show_unit:
            ax.arrow(0, 0, 1, 0, color='black', linewidth=2, linestyle='--', head_width=0.15, label='Unit Vectors')
            ax.arrow(0, 0, 0, 1, color='black', linewidth=2, linestyle='--', head_width=0.15)
            ax.text(1, 0, "i", fontsize=14)
            ax.text(0, 1, "j", fontsize=14)

    ax.legend(loc='upper left')
    st.pyplot(fig)