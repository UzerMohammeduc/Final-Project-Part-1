import numpy as np
import time

def numpy_operations(data):
    start_time = time.time()
    
    data_np = np.array(data)
    
    # Calculate mean
    mean = np.mean(data_np)
    
    # Calculate sum of squares
    sum_squares = np.sum((data_np - mean) ** 2)
    
    # Calculate variance
    variance = np.var(data_np)
    
    # Calculate standard deviation
    std_dev = np.std(data_np)
    
    # Normalize data
    normalized_data = (data_np - mean) / std_dev
    
    end_time = time.time()
    execution_time = end_time - start_time
    return {
        'Sum of Squares': sum_squares,
        'Variance': variance,
        'Standard Deviation': std_dev,
        'Normalized Data': normalized_data[:10],  # return only the first 10 elements for brevity
        'Execution Time': execution_time
    }

# Example data
data = list(range(10000))

# Execute the function
results_numpy = numpy_operations(data)
print("NumPy Results:", results_numpy)
