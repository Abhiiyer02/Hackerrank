def count_substring(string, sub_string):
    s = string
    counter = s.count(sub_string)

    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)