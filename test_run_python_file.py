from functions.run_python_file import run_python_file

def print_block(title, result):
    print(title)
    # add two spaces in front of each line
    for line in result.split("\n"):
        print(f"  {line}")

if __name__ == "__main__":
    result = run_python_file("calculator", "main.py")
    print_block("Result for calculator/main.py:", result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print_block("Result for calculator/main.py:", result)

    result = run_python_file("calculator", "tests.py")
    print_block("Result for calculator/tests.py:", result)

    result = run_python_file("calculator", "../main.py")
    print_block("Result for ./main.py:", result)

    result = run_python_file("calculator", "nonexistent.py")
    print_block("Result for calculator/nonexistent.py", result)

    result = run_python_file("calculator", "lorem.txt")
    print_block("Result for calculator/lorem.txt", result)
