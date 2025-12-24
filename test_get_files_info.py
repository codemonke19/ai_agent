from functions.get_files_info import get_files_info

def print_block(title, result):
    print(title)
    # add two spaces in front of each line
    for line in result.split("\n"):
        print(f"  {line}")

if __name__ == "__main__":
    result = get_files_info("calculator", ".")
    print_block("Result for current directory:", result)

    result = get_files_info("calculator", "pkg")
    print_block("Result for 'pkg' directory:", result)

    result = get_files_info("calculator", "/bin")
    print_block("Result for '/bin' directory:", result)

    result = get_files_info("calculator", "../")
    print_block("Result for '../' directory:", result)
