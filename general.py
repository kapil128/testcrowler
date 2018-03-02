import os


# create directory for projects
def create_project_directory(directory):
    if not os.path.exists(directory):
        print("creating project" + directory)
        os.makedirs(directory)


# create queue and crawled file
def create_data_file(project_name, base_url):
    queue = os.path.join(project_name + "/queue.txt")
    crawled = os.path.join(project_name + "/crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, " ")


# create data files
def write_file(path, data):
    f = open(path, "w")
    f.write(data)


# add contents to a existing
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# delete contents of a file
def delete_file_content(path):
    open(path, 'w').close()


# read a file and convert to each line into set element
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
        return results


# Iterate through a set, each line will be new line in a file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l+"\n")
