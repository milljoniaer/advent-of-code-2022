input_file = "input.txt"


with open(input_file) as file:
    output = file.read().split("\n")

    path = ["/"]
    files = []
    dir_list = ["/"]
    for line in output:
        if line.startswith("$"):
            cmd = line.split(" ")[1]

            if cmd == "ls":
                continue

            arg = line.split(" ")[2]

            if arg == "..":
                path.pop()
            elif arg == "/":
                path = ["/"]
            else: 
                path.append(arg)
                root_path = "/".join(path).replace("//", "/") + "/"
                dir_list.append(root_path)

        else:
            if line.startswith("dir"):
                continue

            name = line.split(" ")[1]
            size = line.split(" ")[0]
            
            root_path = "/".join(path).replace("//", "/") + "/"
            size = int(size)

            if len([file for file in files if file["path"] == f'{root_path}/{name}']) > 0:
                continue

            files.append({
                "path": f'{root_path}/{name}',
                "size": size
            })

    dir_sizes = []
    for d in dir_list:
        filtered_sizes = [f["size"] for f in files if f["path"].startswith(d)]
        tot_sum = sum(filtered_sizes)
        dir_sizes.append({
            "path": d,
            "size": tot_sum
        })

    free_space = 70000000 - [d for d in dir_sizes if d["path"] == "/"][0]["size"]
    still_needed_size = 30000000 - free_space

    filtered_dir_sizes = [d["size"] for d in dir_sizes if d["size"] >= still_needed_size]

    size_to_be_deleted = min(filtered_dir_sizes)
        
    print(size_to_be_deleted)
