from binary_tree import BST, to_list, search


def main():
    from random import randint, seed

    seed(123)

    integers = BST(randint(0, 100))
    for x in range(20):
        integers.insert(randint(0, 100))

    # to_list
    sorted_list = to_list(integers)
    print(sorted_list)

    # search
    print(search(integers, 68))
    print(search(integers, 100))


if __name__ == "__main__":
    main()
