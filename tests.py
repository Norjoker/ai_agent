from functions import get_files_info, get_file_content
# import functions.get_files_info

test1 = get_file_content.get_file_content("calculator", "main.py")
test2 = get_file_content.get_file_content("calculator", "pkg/calculator.py")
test3 = get_file_content.get_file_content("calculator", "/bin/cat")
test4 = get_file_content.get_file_content("calculator", ".pkg/does_not_exist.py")

print(test1)
print(test2)
print(test3)
print(test4)