# 02_summary_statistics_calculator.py

def calculate_mean(data):
    return sum(data) / len(data) if data else 0.0

def calculate_median(data):
    if not data:
        return 0.0
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    return float(sorted_data[mid])

def calculate_variance(data):
    if len(data) < 2:
        return 0.0
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

if __name__ == "__main__":
    dataset = [12, 15, 18, 22, 20, 25, 30, 28, 19, 24]
    
    print(f"Dataset: {dataset}")
    print(f"Mean:     {calculate_mean(dataset):.2f}")
    print(f"Median:   {calculate_median(dataset):.2f}")
    print(f"Variance: {calculate_variance(dataset):.2f}")
