import file_handler


file_content = file_handler.read_file_to_list("day_01.txt", True)
# file_handler.write_to_file("text.txt", file_content)
# file_content = file_handler.read_file_to_string("text.txt")

test_content = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
result = 0

for line in file_content:
  coordinates = ""
  first_number = 0
  last_number = len(line) - 1
  for letter in line:
    if letter in numbers:
      coordinates += letter
      break
  for letter in reversed(line): 
    if letter in numbers:
      coordinates += letter
      break
  int_coordinates = int(coordinates)
  result += int_coordinates

print(result)