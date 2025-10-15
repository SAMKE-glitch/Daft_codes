import numpy as np
import pandas as pd

# Step 1: Create a random array (20x3)
data = np.random.rand(20, 3)

# Step 2: Split into two equal arrays (M and N)
M = data[:10, :]
N = data[10:, :]

# Step 3: Assign instance names (A–J for M, Q–Z for N)
M_labels = list('ABCDEFGHIJ')
N_labels = list('QRSTUVWXYZ')

# Step 4: Create DataFrames for readability
M_df = pd.DataFrame(M, index=M_labels, columns=['Col1', 'Col2', 'Col3'])
N_df = pd.DataFrame(N, index=N_labels, columns=['Col1', 'Col2', 'Col3'])

# Display the results
print("Array M:")
print(M_df)
print("\nArray N:")
print(N_df)

