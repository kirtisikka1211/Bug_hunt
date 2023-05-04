def calculate_average(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    avg = total_sum / len(numbers)
    return avg


numbers = []
print("Average of numbers:", calculate_average(numbers))



