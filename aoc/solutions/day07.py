def get_directory_sizes(lines):
    """Helper function to convert input into dictionary
    of directories and their sizes"""

    sub_dirs = {}
    dir_sizes = {}
    curr_file_path = "/"

    # Create dict to store total file size for each directory
    # and another dict to store subdirectories for each directory

    for i, line in enumerate(lines):

        if i == 0:
            continue
        if line.startswith("$ cd"):
            if not line.endswith(".."):
                # add current directory to file path
                curr_file_path += "/" + line.replace("$ cd ", "")
            else:
                # remove current directory from file path
                curr_file_path = "/".join(curr_file_path.split("/")[:-1])
            continue

        if line.startswith("$ ls"):
            dir_sizes[curr_file_path] = 0
            sub_dirs[curr_file_path] = []
            continue

        if line.startswith("dir"):
            sub_dirs[curr_file_path] += [
                curr_file_path + "/" + line.replace("dir ", "")
            ]
            continue

        dir_sizes[curr_file_path] += int(line.split(" ")[0])

    # Loop through directories, updating size with subdirectory sizes
    # until all subdirectories have been processed

    non_empty_dirs = [k for k, v in sub_dirs.items() if len(v) > 0]

    while non_empty_dirs:

        for child_dir, child_sub_dirs in sub_dirs.items():

            # Only want to update parent directory size when the child
            # directory has no subdirectories

            if len(child_sub_dirs) == 0:

                for parent_dir, parent_sub_dirs in sub_dirs.items():

                    if child_dir in parent_sub_dirs:

                        dir_sizes[parent_dir] += dir_sizes[child_dir]

                        sub_dirs[parent_dir].remove(child_dir)

                if child_dir in non_empty_dirs:
                    non_empty_dirs.remove(child_dir)

    return dir_sizes


def part1(data):

    lines = data.rstrip("\n").split("\n")

    dir_sizes = get_directory_sizes(lines)

    return sum([v for k, v in dir_sizes.items() if v <= 100000])


def part2(data):

    lines = data.rstrip("\n").split("\n")

    dir_sizes = get_directory_sizes(lines)

    space_required = 30000000 - (70000000 - dir_sizes["/"])

    return min([v for k, v in dir_sizes.items() if v > space_required])
