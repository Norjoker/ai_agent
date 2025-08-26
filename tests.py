from functions import get_file_content, get_files_info, write_file, run_python

test1 = run_python.run_python_file("calculator", "main.py")
test2 = run_python.run_python_file("calculator", "main.py", ["3 + 5"])
test3 = run_python.run_python_file("calculator", "tests.py")
test4 = run_python.run_python_file("calculator", "../main.py")
test5 = run_python.run_python_file("calculator", "nonexistent.py")

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)