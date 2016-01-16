import sys
import os

if len(sys.argv) < 2:
    print("Usage: python %s solution_file" % sys.argv[0])
    exit()

sol_lines = []
with open(sys.argv[1]) as sol_file:
    for line in sol_file.readlines():
        sol_lines.append(line.strip())

file_names = [f for f in os.listdir('.') 
            if os.path.isfile(f)  and f not in [sys.argv[0], sys.argv[1]]]
for file_name in file_names:
    with open(file_name) as f:
        count = 0
        for idx, line in enumerate(f.readlines()):
            if idx < len(sol_lines) and line.strip() == sol_lines[idx]:
                count += 1
        print("%s = %d" % (file_name, count))




