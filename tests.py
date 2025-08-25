from functions import get_files_info, get_file_content, write_file
# import functions.get_files_info

test1 = write_file.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
test2 = write_file.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
test3 = write_file.write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#test4 = get_file_content.get_file_content("calculator", ".pkg/does_not_exist.py")

print(test1)
print(test2)
print(test3)
#print(test4)