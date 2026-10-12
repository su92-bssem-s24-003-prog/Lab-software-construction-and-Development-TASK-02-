



def read_student_name():
    """Ask for the student's name and keep asking until it is not empty."""
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def read_marks(subject_number):
    """Ask for one subject's marks and keep asking until they are valid (0-100)."""
    while True:
        raw_value = input(f"Enter marks for subject {subject_number} "
                          f"(0-{MAX_MARKS_PER_SUBJECT}): ")
        try:
            marks = float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= marks <= MAX_MARKS_PER_SUBJECT:
            return marks
        print(f"Marks must be between 0 and {MAX_MARKS_PER_SUBJECT}.")


def read_all_marks(subject_count=NUMBER_OF_SUBJECTS):
    """Collect marks for every subject and return them as a list."""
    return [read_marks(number) for number in range(1, subject_count + 1)]


def calculate_total(marks):
    """Return the sum of all subject marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the average of the marks (0 if the list is empty)."""
    if not marks:
        return 0
    return calculate_total(marks) / len(marks)


def calculate_percentage(marks):
    """Return the overall percentage based on the maximum possible marks."""
    if not marks:
        return 0
    return calculate_total(marks) / (len(marks) * MAX_MARKS_PER_SUBJECT) * 100



def determine_grade(percentage):
    """Convert a percentage into a letter grade."""
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= PASS_MARK:
        return "D"
    return "F"


def determine_status(marks):
    """Return 'PASS' only if every subject is at or above the pass mark."""
    if all(mark >= PASS_MARK for mark in marks):
        return "PASS"
    return "FAIL"



def build_student_result(name, marks):
    """Combine the input data and all calculated values into one result record."""
    percentage = calculate_percentage(marks)
    return {
        "name": name,
        "marks": marks,
        "total": calculate_total(marks),
        "average": calculate_average(marks),
        "percentage": percentage,
        "grade": determine_grade(percentage),
        "status": determine_status(marks),
    }
def format_result(result):
    """Turn a result record into a printable multi-line string."""
    max_total = len(result["marks"]) * MAX_MARKS_PER_SUBJECT
    lines = [
        "=" * 40,
        "          STUDENT RESULT CARD",
        "=" * 40,
        f"Name        : {result['name']}",
    ]
    for number, mark in enumerate(result["marks"], start=1):
        lines.append(f"Subject {number}   : {mark:.1f}")
    lines += [
        "-" * 40,
        f"Total       : {result['total']:.1f} / {max_total}",
        f"Average     : {result['average']:.2f}",
        f"Percentage  : {result['percentage']:.2f}%",
        f"Grade       : {result['grade']}",
        f"Status      : {result['status']}",
        "=" * 40,
    ]
    return "\n".join(lines)


def display_result(result):
    """Print the formatted result to the screen."""
    print()
    print(format_result(result))



def process_student():
    """Run the full workflow for one student by coordinating the helpers."""
    name = read_student_name()
    marks = read_all_marks()
    result = build_student_result(name, marks)
    display_result(result)


def main():
    """Program entry point."""
    process_student()


if __name__ == "__main__":
    main()
