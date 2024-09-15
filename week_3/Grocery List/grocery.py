def main():
    dic = {}

    while True:
        try:
            item = input().strip().title()
            if item:
                dic[item] = dic.get(item, 0) + 1
        except EOFError:
            break

    sorted_list = sorted(dic.items(), key=lambda x: x[0])

    for item, count in sorted_list:
        print(count,item.upper(),sep=' ')

if __name__ == "__main__":
    main()
