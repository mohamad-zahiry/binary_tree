from binary_tree import BST, to_list


def main():
    from random import randint, seed

    seed(123)

    integers = BST(randint(0, 100))
    for x in range(20):
        integers.insert(randint(0, 100))

    sorted_list = to_list(integers)
    print(sorted_list)


if __name__ == "__main__":
    main()
