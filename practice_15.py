for i in range(1, 120):
    if i % 2 != 0:
        continue  # Skip even numbers, go to next iteration
    elif i == 26:
        break   # Exit the loop when i becomes 25
    else:
        pass      # Explicitly do nothing (dummy placeholder)

    # This block runs only for odd numbers before 25
    print(i)
  OUTPUT:-
2
4
6
8
10
12
14
16
18
20
22
24

=== Code Execution Successful ===
