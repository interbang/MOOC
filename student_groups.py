students = int(input("How many students on the course? "))
size_group = int(input("Desired group size? "))
mod_number = students % size_group

if mod_number == 0:
    number_group = students // size_group
else:
    number_group = students // size_group + 1 

print(f"Number of groups formed: {number_group}")