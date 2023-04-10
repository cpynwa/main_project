from re import match, compile


def forti_search(filename, input_pattern, select_option):
    if select_option == 'policy':
        search_range = 'config firewall policy'
    elif select_option == 'address':
        search_range = 'config firewall address'

    with open(filename, 'rt', encoding='UTF8') as file:
        with open('search_file.txt', 'a') as search_file:
            for line in file:
                if match(search_range, line):
                    break
            for line in file:
                if match("end", line):
                    break
                search_file.write(line)

    stack = []
    stack2 = []

    with open("search_file.txt", "r") as search_file:


        for line in search_file:
            if match(r'^    edit', line):
                stack.append(line.strip())
            elif match(r'^    next', line):
                stack.append(line.strip())
                stack2.append(stack)
                stack = []
            else:
                stack.append(line.strip())

        pattern = input_pattern
        r = compile(f".*{pattern}.*")

        stack3 = [i for i in stack2 if list(filter(r.match, i))]


    with open("result.txt", "a") as result_file:
        for i in stack3:
            result_file.write("\n")
            for j in i:
                result_file.write(j + "\n")
