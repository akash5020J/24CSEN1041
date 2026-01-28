for i in range(1, 120):
    if i % 2 == 0:
        continue  # Skip even numbers, go to next iteration
    elif i == 55:
        continue   # Exit the loop when i becomes 25
    else:
        pass      # Explicitly do nothing (dummy placeholder)

    # This block runs only for odd numbers before 25
    print(i)
  OUTPUT:-
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
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

=== Code Execution Successful ===
