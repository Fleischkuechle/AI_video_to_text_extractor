from tqdm import tqdm
import time

# Number of iterations for the progress bar
total_iterations = 100

# Create a progress bar
for i in tqdm(range(total_iterations), desc="Processing", ascii=True, unit="iter"):
    time.sleep(0.05)  # Simulate some processing time

print("Process completed!")
