# reading src.txt
def get_all_lines_from_file(file_name):
    file = open(file_name)
    src = file.readlines()
    file.close()
    return src


# reading output file
def get_file_content(file_name):
    file = open(file_name)
    src = file.read()
    file.close()
    return src


# writing output file
def write_to_md(file_name, md_solution):
    file = open(file_name, 'w+')
    file.write(md_solution)
    file.close()


# generating new main file
def get_new_main(file_name, md_solution):
    file = open(file_name)
    old_main = file.read()
    file.close()
    try:
        new_main = old_main[0:old_main.index('##')]
        new_main += md_solution[0:md_solution.index('##')]
        new_main += old_main[old_main.index('##'):]
        new_main += md_solution[md_solution.index('##') - 1:]
    except:
        new_main = md_solution
    return new_main


# main class
class Task:
    # init class
    def __init__(self, title, link, source_code):
        self.title = title.split('. ')[-1].strip('\n')
        self.link = link.strip('\n')
        self.source_code = source_code

    def get_md_link(self):
        return '+ [{}](#{})'.format(self.title, self.link.split('/')[-2])

    def get_md_title(self):
        return '## {}'.format(self.title)

    # generate code block
    def get_md_python_solution(self):
        return '```python\n{}\n```'.format(
            ''.join(map(lambda x: x[4:], self.source_code)))

    # generate new md file
    def get_new_md_file(self):
        return '{}\n{}\n{}\n{}'.format(self.get_md_link(), self.get_md_title(),
                                       self.link, self.get_md_python_solution())

    def __str__(self):
        return '{}\n{}\n{}'.format(self.title, self.link, self.source_code)


if __name__ == "__main__":
    # read src.txt
    source_lines = get_all_lines_from_file('src.txt')

    # create class instance
    task = Task(source_lines[0], source_lines[1], source_lines[3:])

    # generate md file
    new_md_file = task.get_new_md_file()

    # write to main file
    new_main_md = get_new_main('main.md', new_md_file)
    print(new_main_md)
    write_to_md('main.md', new_main_md)