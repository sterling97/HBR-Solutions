

usr_numbers = int(input("Digite el numero que quiere invertir: "))


def reverse(usr_numbers):
    string=str(usr_numbers)
    reverse=string[::-1]
    reversed_number=int(reverse)
    return reversed_number


print(reverse(usr_numbers))


if __name__ == '__main__':
    reverse
