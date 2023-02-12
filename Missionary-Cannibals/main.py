def solver(n):
    x1 = n
    y1 = n
    x2 = 0
    y2 = 0
    temp = 0
    a_list = []
    b_list = []
    init_set = (n, n)
    a_list.append(init_set)
    init_set = (0, 0)
    b_list.append(init_set)

    #     initially transfer 1 cannibals forom Island 1 and keep 1 as the boater

    for i in range(n + n - 2):
        if i == 0:
            y1 -= 2
            y2 += 1
            temp += 1
            a_list.append((x1, y1))
            b_list.append((x2, y2))
        else:
            if x1 > y1 and (x1 > 0 and y1 > 0):
                x1 -= 1
                x2 += 1
                a_list.append((x1, y1))
                b_list.append((x2, y2))
            else:
                y1 -= 1
                y2 += 1
                a_list.append((x1, y1))
                b_list.append((x2, y2))
    x1 -= 1
    x2 += 1
    a_list.append((x1, y1))
    b_list.append((x2, y2))

    # free the boat cannibal
    temp -= 1
    y2 += 1
    a_list.append((x1, y1))
    b_list.append((x2, y2))

    display_output(a_list, b_list)


def display_output(a_list, b_list):
    for i in range(len(a_list)):
        print(f"{a_list[i]}        {b_list[i]}")

    pass


if __name__ == "__main__":
    solver(3)
