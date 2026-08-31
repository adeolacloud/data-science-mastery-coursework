"""
Module 2: Mathematics & Applied Statistics for Data Science
Author: Adeola (adeolacloud)
Repository: data-science-mastery-coursework
Topics Covered:
  - Vector & Matrix Operations (Linear Algebra)
  - Descriptive Statistics & Normal Distribution Analysis
  - Hypothesis Testing (Z-Score & Probability)
  - Optimization via Gradient Descent (Calculus)
"""

import numpy as np
from scipy import stats

def linear_algebra_demo():
    print("=== 1. LINEAR ALGEBRA OPERATORS ===")
    # Feature matrix X (3 samples, 2 features)
    X = np.array([[1.0, 2.0], 
                  [3.0, 4.0], 
                  [5.0, 6.0]])
    
    # Weight vector W
    W = np.array([0.5, 1.5])
    
    # Matrix-Vector Multiplication (X * W)
    predictions = np.dot(X, W)
    print("Feature Matrix X shape:", X.shape)
    print("Predictions Vector (X . W):", predictions)
    print("-" * 40)

def statistical_analysis_demo():
    print("=== 2. STATISTICAL DISTRIBUTIONS & METRICS ===")
    # Simulated dataset (e.g., daily API response times in ms)
    data = np.array([120, 125, 122, 130, 128, 121, 126, 124, 129, 350]) # Includes outlier
    
    mean_val = np.mean(data)
    median_val = np.median(data)
    std_dev = np.std(data)
    
    print(f"Dataset Mean: {mean_val:.2f} ms")
    print(f"Dataset Median (Robust to Outliers): {median_val:.2f} ms")
    print(f"Standard Deviation: {std_dev:.2f} ms")
    
    # Z-Score Calculation to detect outliers (> 2.0 or < -2.0)
    z_scores = (data - mean_val) / std_dev
    outliers = data[np.abs(z_scores) > 2.0]
    print(f"Detected Outliers (Z-Score > 2.0): {outliers}")
    print("-" * 40)

def gradient_descent_demo():
    print("=== 3. CALCULUS: GRADIENT DESCENT OPTIMIZATION ===")
    # Objective: Minimize Loss function f(w) = w^2 - 4w + 4  (Derivative f'(w) = 2w - 4)
    w = 0.0  # Initial weight weight
    learning_rate = 0.1
    epochs = 20
    
    for epoch in range(1, epochs + 1):
        gradient = 2 * w - 4  # Derivative
        w = w - learning_rate * gradient  # Parameter update rule
        
    print(f"Optimized Weight 'w' after {epochs} epochs: {w:.4f} (Global Minimum is 2.0)")
    print("-" * 40)

if __name__ == "__main__":
    linear_algebra_demo()
    statistical_analysis_demo()
    gradient_descent_demo()
