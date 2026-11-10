def calculate_average(numbers: list[int]) -> float:
    if not numbers:
        raise ValueError("Lista liczb jest pusta")
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

if __name__ == "__main__":        
    print(calculate_average([]))            