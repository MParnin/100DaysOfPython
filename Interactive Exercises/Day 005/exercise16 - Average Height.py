student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = int()
count = int()
for n in student_heights:
  total_height += n
  count += 1
print(f"total height = {total_height}")
print(f"number of students = {count}")

average_height = int(round(total_height / count, 0))
print(f"average height = {average_height}")