import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.header("Line Equation Visualizer (y = mx + c)")
    
    # Create sliders for m (slope) and c (y-intercept)
    m = st.slider("Select slope (m)", -10.0, 10.0, 1.0, step=0.1)
    c = st.slider("Select y-intercept (c)", -10.0, 10.0, 0.0, step=0.1)
    
    # Create the visualization
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Generate x values
    x = np.linspace(-10, 10, 200)
    
    # Calculate y values using y = mx + c
    y = m * x + c
    
    # Plot the line
    ax.plot(x, y, 'b-', label=f'y = {m}x + {c}')
    
    # Add grid
    ax.grid(True)
    
    # Add x and y axes
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Set equal aspect ratio
    ax.set_aspect('equal')
    
    # Set limits
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    
    # Add labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Linear Equation Visualization')
    ax.legend()
    
    # Display the plot in Streamlit
    st.pyplot(fig)
    
    # Display the equation
    st.markdown(f"### Current Equation: y = {m}x + {c}")