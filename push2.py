def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    marks = [80, 85, 90]
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
