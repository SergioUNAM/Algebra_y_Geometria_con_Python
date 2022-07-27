def read_matrix_from_console():
    n = int(input())  # Number of rows
    m = int(input())  # Number of columns
    A = []

    for i in range(n):
        row = input().split()
        for j in range(m):
            row[j] = int(row[j])
            A.append(row)
    return A


def print_matrix_to_console(A):
    for row in A:
        for element in row:
            print(element, end="")
            print()


def run():
    A = read_matrix_from_console()
    print_matrix_to_console(A)


if __name__ == "__main":
    run()
