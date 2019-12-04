

start = 147981
end = 691423

total = 0
for password in range(start, end):

    password_str = str(password)

    for i in range(5):
        if password_str[i] == password_str[i + 1]:
            break
    else:
        continue

    for i in range(5):
        if int(password_str[i]) > int(password_str[i + 1]):
            break
    else:
        total += 1


print(total)
