def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

def main():
    # Example marks list
    marks = [80, 85, 90]
    total = calculate_total(marks)
    average = calculate_average(marks)
    print(f"Total: {total}")
    print(f"Average: {average}")

if __name__ == "__main__":
    main()
