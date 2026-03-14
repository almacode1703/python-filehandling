from colorama import Fore, Style

file_text = open("multiLine.txt", "r")
print(f"Content of the file... ")
print(f"{Fore.GREEN}{'.'*25}{Style.RESET_ALL}")

# Reading content of the file
file_content  = file_text.read()
print(f"{file_content}")

print(f"{Fore.GREEN}{'.'*25}{Style.RESET_ALL}")

# Checking how many lines by each \n
line_list = file_content.split("\n")
line_counter = 0
for line in line_list:
    if line:
        line_counter += 1

# Total number of lines
print(f"Total Number of lines :{Fore.BLUE} {line_counter}{Style.RESET_ALL}")
file_text.close()