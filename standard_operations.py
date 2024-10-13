import time

def standard_operations(data):
    start_time = time.time()
    
    # Calculate mean
    mean = sum(data) / len(data)
    
    # Calculate sum of squares
    sum_squares = sum((x - mean) ** 2 for x in data)
    
    # Calculate variance
    variance = sum_squares / len(data)
    
    # Calculate standard deviation
    std_dev = variance ** 0.5
    
    # Normalize data
    normalized_data = [(x - mean) / std_dev for x in data]
    
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
results_standard = standard_operations(data)
print("Standard Python Results:", results_standard)
