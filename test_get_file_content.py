from functions.get_file_content import get_file_content

def print_block(title, result):
    print(title)
    # add two spaces in front of each line
    for line in result.split("\n"):
        print(f"  {line}")

if __name__ == "__main__":
    result = get_file_content("calculator", "lorem.txt")
    print_block("Result for current file:", result)
    result = get_file_content("calculator", "main.py")
    print_block("Result for current file:", result)
    result = get_file_content("calculator", "pkg/calculator.py")
    print_block("Result for current file:", result)
    result = get_file_content("calculator", "/bin/cat")
    print_block("Result for current file:", result)
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print_block("Result for current file:", result)
