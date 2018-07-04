import os


def create_project_dir(fullpath):
    if not os.path.exists(fullpath):
        print 'Creating directory', fullpath
        os.makedirs(fullpath)
    else:
        print 'Directory exists'


def create_data_file(project_name, url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    fullpath = os.path.join(os.getcwd() , project_name)
    create_project_dir(fullpath)
    if not os.path.isfile(queue):
    	write_file(queue, url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    f = open(path, 'w')
    f.write(data + '\n')
    f.close


def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data)


def delete_filecontent(path, data):
    with open(path, 'w') as f:
        pass


def file_to_set(file_name):
    results = set()
    with open(file_name, 'r') as f:
        for line in f:
            result.add(line.replace('/n', ''))
        return results


def set_to_file(links, file):
    delete_filecontent(file)
    for link in sorted(links):
        append_to_file(file, link)

create_data_file('facebook','https://wwww.facebook.com/')