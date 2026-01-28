first_num = int(input("Enter the first num:"))
second_num = int(input("Enter the second num:"))

for i in range(first_num, second_num):
    if i % 2 == 0:
        continue   # skips even numbers
    elif i == 133:
        break      # stops the loop entirely at 133
    else:
        pass       # placeholder, does nothing

    print(i)

OUTPUT:-
Enter the first num:100
Enter the second num:150
101
103
105
107
109
111
113
115
117
119
121
123
125
127
129
131

=== Code Execution Successful ===
