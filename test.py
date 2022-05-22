from binary_tree import BinaryTree, BT_to_list


def main():
    from random import randint, seed

    seed(123)

    integers = BinaryTree(randint(0, 100))
    for x in range(20):
        integers.insert(randint(0, 100))

    sorted_list = BT_to_list(integers)
    print(sorted_list)


if __name__ == "__main__":
    main()
