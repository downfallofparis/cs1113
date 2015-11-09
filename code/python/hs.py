n = input("enter a positive integer:")
n = int(n)
new_list = [n]
while n != 1:
    if (n % 2 == 0 and n != 1):
        n = n/2
        new_list.append(n)
    if (n % 2 != 0):
        n = (3*n) + 1
        new_list.append(n)

return new_list
