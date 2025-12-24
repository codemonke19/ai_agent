from functions.write_file import write_file

def print_block(title, result):
    print(title)
    # add two spaces in front of each line
    for line in result.split("\n"):
        print(f"  {line}")

if __name__ == "__main__":
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print_block("Result for current directory:", result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print_block("Result for 'pkg' directory:", result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print_block("Result for '/tmp' directory:", result)
