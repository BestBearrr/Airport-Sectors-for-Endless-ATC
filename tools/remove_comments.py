# This file removes lines that are comments, i.e. start with #.

# Specify your target file here
target_file = "ENTER TARGET FILE HERE"

# Read file
with open(target_file) as file:
    contents = file.readlines()

# Counts number of removed lines, so that if a line is removed, no lines in the remaining list are skipped during the for loop
removed_lines_count = 0

# Iterate each line
for i in range(len(contents)):

    # Does the line contain '#'
    if "#" in contents[i - removed_lines_count]:

        # Remove the line if it starts with '#'
        if contents[i - removed_lines_count].startswith("#"):
            contents.pop(i - removed_lines_count)
            removed_lines_count += 1

# Write to new file
with open(f"{target_file} without comments.py","w") as file:
    file.writelines(contents)