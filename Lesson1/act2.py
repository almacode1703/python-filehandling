file_read = open("codingal.txt", "r")
print(f"{file_read.read()}")
file_read.close()

file_write = open("codingal.txt", "w")
file_write.write("I am writting .....")
file_write.close()

file_append = open("codingal.txt", "a")
file_append.write("I am writting more stuff")
file_append.close()

