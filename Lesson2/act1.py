file_read = open('codingal.txt','r')
content = file_read.read(8)
print(f"{content}")

file_append = open("codingal.txt","a")
modified_content = file_append.write("\nHello there ???")

print(f"{modified_content}")
file_read.close()
