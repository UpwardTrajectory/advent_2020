sample = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

msg = """104: 23 105 | 105 23
40: 23 39 | 105 35
127: 23 3 | 105 49
96: 85 23 | 73 105
114: 70 23 | 106 105
124: 80 105 | 71 23
23: "a"
97: 105 12 | 23 104
18: 23 118 | 105 29
89: 121 105 | 39 23
13: 23 18 | 105 87
122: 50 105 | 24 23
6: 58 105 | 59 23
101: 105 44 | 23 43
31: 105 65 | 23 13
36: 64 105 | 68 23
74: 105 123 | 23 7
38: 19 23 | 48 105
118: 105 127 | 23 75
130: 23 30 | 105 44
59: 105 121 | 23 71
112: 92 23 | 97 105
91: 25 23 | 66 105
46: 30 23 | 39 105
111: 105 35 | 23 104
28: 105 129 | 23 112
25: 105 62 | 23 89
125: 23 61 | 105 100
120: 105 131 | 23 44
102: 43 105 | 48 23
105: "b"
27: 5 23 | 10 105
84: 21 23 | 130 105
56: 105 39
35: 23 23 | 105 23
44: 23 105
69: 80 105 | 104 23
100: 72 105 | 110 23
72: 39 105 | 19 23
95: 105 69 | 23 109
88: 120 105 | 78 23
53: 67 105 | 14 23
26: 21 23 | 56 105
80: 105 105 | 105 23
70: 19 23 | 12 105
92: 44 23 | 12 105
37: 48 105 | 55 23
132: 23 16 | 105 122
7: 105 48 | 23 12
113: 39 23 | 12 105
10: 102 105 | 126 23
94: 105 | 23
42: 105 128 | 23 132
103: 105 89 | 23 57
107: 105 79 | 23 76
11: 42 31
99: 47 105 | 1 23
55: 105 94 | 23 23
8: 42
4: 23 41 | 105 15
81: 51 105 | 116 23
76: 37 105 | 78 23
110: 12 23 | 35 105
45: 105 33 | 23 84
78: 23 131 | 105 35
63: 72 105 | 133 23
51: 19 105 | 131 23
83: 105 45 | 23 27
21: 23 71 | 105 104
19: 23 105 | 105 94
54: 23 48 | 105 55
41: 23 121 | 105 55
20: 115 105 | 86 23
15: 105 71
66: 105 113 | 23 49
121: 94 94
14: 99 105 | 81 23
22: 30 105
129: 105 109 | 23 111
5: 15 105 | 9 23
30: 105 105
131: 105 23
87: 23 77 | 105 91
98: 23 38 | 105 82
77: 23 88 | 105 74
43: 23 23 | 94 105
86: 23 98 | 105 93
58: 55 23 | 131 105
1: 23 35 | 105 30
9: 105 131 | 23 55
49: 104 105 | 55 23
68: 23 131 | 105 48
0: 8 11
71: 23 23
48: 105 23 | 23 94
29: 105 119 | 23 117
93: 52 23 | 22 105
16: 105 125 | 23 28
126: 35 23 | 43 105
65: 83 23 | 53 105
62: 19 105 | 104 23
12: 23 23 | 23 105
52: 105 19 | 23 104
67: 23 103 | 105 63
24: 4 105 | 26 23
50: 105 95 | 23 96
47: 105 30 | 23 30
32: 105 114 | 23 6
82: 105 19 | 23 12
75: 34 105 | 59 23
34: 23 39 | 105 80
17: 23 104 | 105 131
109: 44 23 | 39 105
79: 17 23 | 78 105
85: 12 23 | 39 105
57: 23 30 | 105 121
2: 23 30
3: 71 23 | 19 105
115: 108 105 | 36 23
64: 23 121 | 105 12
90: 105 32 | 23 107
116: 12 105 | 131 23
123: 71 105 | 35 23
61: 85 23 | 70 105
133: 80 94
119: 105 40 | 23 46
128: 23 90 | 105 20
60: 104 105 | 80 23
33: 23 89 | 105 101
73: 105 121 | 23 19
39: 105 105 | 23 23
108: 105 2 | 23 54
106: 71 105 | 44 23
117: 124 105 | 60 23

aababbbaaabbaaaabbabaaaabbbaababbbbbaaabbaabbbbb
aababbabaababbbabbbabaaabbbbbbababaaabaa
bababbbabaaabbaababbabaaabbbaaab
baabababaaababbaabbbbabb
baaaaaabaaaaababbbabbabbbaaaabba
abbabbaaabbbabbaabbbababaabbabbaaababaabbabbabbbaabaabababbaaabbaababababbbbbbab
bbbaabbaababaabaabbaaaabbaabaaabababbaababbbaaabaaaaaaabaabbbaabaabababa
baaabaaaababbabbbabbababbbbabaaaabaaaabb
bababaababbbababababaababbabbabbaabbaabbaaabaabb
aabbbbabbabbababbbbaabbb
bbbbbaaabbabbabbbaaabbbb
bbaaabbabababbaaaabbbabb
aaaababbaaaaaabbaaaababbababbbaa
baaaabbbabaabbbaabbabbab
aabbaabbbbbaaaaaabbaaaab
baaaabbbaabbababbbbbbaaababaabba
abaaababbbaabbababbbaaaabaabaabbbbbbbaba
baaababaaabaabaaaaabbbababbaaaaa
bbaabbabaabbbbabaabbbbaa
bbabaaaabbbbaaabbbababbb
abaaaaabbaaabbabbbabbaab
baaaabbbabaabbbaaaabaaaa
bbabbbbbbababaaabbbbabaabaaaaaaa
abababbbabbbbbbbbbababaa
ababaabbbbbabbaaaabaaaaabbbaabbaabbbbaaabbbabaababbbbbbaaaababbaabbaaaba
babbbbaabaaaabbbababbaaa
bababbbaaaaabaabbbabbaaa
babababaaaabbbbbbbababaa
aaaaaaaabbbaabbbabbaaabbabaabbbbabaabbaabababbaaaaababbababbabbaaaaabbbbbaabbbbabbaaabba
babbaabaabababbbaababbbb
baabbaabbaaaabbbbbbbabaabbbababb
bbbaaaaaabbbaaabbbabbaaa
aababbbabbaaababbaababaabbbaabba
bababbbaaabaaabbabbaabba
baaaabaabaaabbabbbbaaaaa
bbbabbabaabaaabbaaabaaabbaaabbba
bbaaaabbbaaabaaabbbaaaabbbaaaabbbabbabbbbabaaaba
bbabbbbabbabaaaaaabaabbbaababbbb
abaaababaababbabbbbaabba
bbbaabaababaaaabbbbababa
aaababaaabbaaabbaaaababa
bbaababaaaaaabaaaaabaaaa
aabbaabaaaaaabababaabaabbbaabaabbbbaabbaabbaaaab
babababababababbbbbbabbb
aabbaaaabbbaaaabbabababbbbbbbbbbaaaaaaaa
babbabaaaaaaababbabaaabb
bbbbabaaabaaabbaaaababbb
bbabaaaabbaabaaabbbaabaaabbaabba
babbbaaaabaaabbaabbaaaab
baaababbababbabbbabababaababbabbaaabbbaaababbaab
baaaabaabaaabbabbbbababa
babababbabbbaaaaaaaaaaaa
bbaababbabbaaabbabbbbabbabbbabababbbabba
aabbbaabbbabbbbbabaaabbabbabbbbbaabaababbabbbabbaabababa
aababbabaabaababbbabbabbabbabaabababbaab
abbbbbaabaaabbababbbbbaabaaabbbb
abababababaaaabbbaaaabbababaaabbabaabbbbbababaab
abaaabbaabababaaababbbbaaabaaabbabbabababababababaaabaabaaaabaaababaaababbaaaaaaabaabbbb
baaabbabaababaabbabababbbaaabaaaabbbabbaabaaaabb
abaababbababaababaabbbaababbaaaa
aaaaaababbbaababbbbaabbb
babababbbababbaabbabbbaaabaababa
aaabaababbbbabbbbbbbbbaababbabbabbbaabababbbbabbbabaaababaabababaaaaabba
abaabaababbbaaaabbaabaab
bbbabaaaabbbaababbaaaaaa
aabaaabbbbababababaaaabaabbbaaaaaaabaababaabaabb
ababbaabbaaaaaabbbbaaabaabbaaaabaababbbbbbaaabbaaababaabbbbababa
babbababbbbbbaaaababbaab
baaabbabbababaabaaaabbbb
baaababbbaabababababbaaa
bbaaabbbaaaaabbabbbaaaba
babbababbaaaabbbabbabaaabaabbbba
babbbaaabbabbbaababaabba
bbaabaaaaaabbabaaaabbabaaaaabbabbaaababa
aaaaaabaabbabaaaabaabbbaaaabbaaabaaabbbb
bababaababaaaaabbaabbaaa
aababaabaabaaababbaaaabbaababaaa
bbbabaabaaaabaababbbbbab
baabaabaaaaababbbbbbabba
abaabaabbbbaabaaababaabababbabbbbbbbaaaa
bababbaaaaaaabbaaaaaaabbabababba
bbabaabaabbabbbbbaaaabaaaabbbabb
bbabababababaababbbaaaabbbbbbaba
aabaabbbbabababaaabaaaaabbabbbabbbbbaabbbbbabbbbabbbbaba
abbaaaaabaababbabaaaabab
aabbbaabbbabbbbbbaaaabbbabbaaaaabababbbb
abaabbbbbbaaabbabaabbaabaaaaabbbbaabbabb
aabaabaababaaaaaabbabaab
abbbbbaababbaabbbbaaabaaaaabbbaa
aabbaabbaaaaababaabbabaabbbbbbbb
abbaaabbbbbabbbbaabbabba
bbabababaaabbaabbaaabbabbbbbbaaaababaabaaaaabbaabaabaaaa
bbaabaaababababbaaaabaaa
babbbbaabaaaaabbabbbaabb
babbaabaaaaabaabaabaaabaaabababa
aabaabbbaabbbabaabbbaabaababaaab
abbbbabbbbaaaabbbbababaa
bbbbbaaabbabaaaabbbbabbb
abaabababbabaaabaababbaa
bbabaaabbaaabbaaabbaaaba
bbabbbbaaaabbbbbbaabbbbababbbaabaabbbaaaabbaabababaabaaabaabbbbbabbaabaabbaaabbaaababbaa
aabaabbbabbaabaaaaaaaaaa
babbbaaababbaabbbbababba
bababbababaaaaaabbbbabba
baabababaabaabaaaaaababa
ababaabaabbabaaabbaabbbbabaaaaabbbbbbaaabbaabaababbbabaaababbaaa
bbaabbaaaabbbaabbaaabbbb
baaaaaabaabaabaaabbaaaaa
aaababaabbabbbbaabbbbbaabbbaaabababaaaba
abbbaababaabaabaabbabbaa
abbbbbaaaabbabaaabababaa
abbbaabababbaabbaababbaabbaaaabbabbbbbbaabbabbbaaaaabbba
babaaaababaaabbabbbabaaabaababbbbabbaaab
babaaaaababbbbbbbaabaaaa
bbbbbaabbabaaaaaabbbbabbaaabbbbbbbabbaabbbabbbbabbbabbbb
babababaaaaababbaaababbaabbbbaaa
aaababaaaabaabaaababaaaa
bbaaaabaabbbbabababbbaab
bbbaaaabaababbbaabaaabbababbbbab
abbbbaabbaaaaabbbabbaabaabbbaaaabbabbaab
abbbababababbabababaaaab
aabaabbbabaababbbabaabab
bbaaaababaabaabaaabbbabb
bbbabbabbabbababaaabaababbbaaabb
babababbbbaaababbbbabaab
baabbbabbbbbbaaabaabbbabaabaaabaabbaabbb
aaaaabbabaaababbbbbababb
bbbaabaabababbbababbabbabbbaabbbbbbabbaa
bbaaabababaaaaababaaaababbababbbbbbbbbbb
aaaaababbaabbbababbaaaab
bbbaaaabbaababaabbbbbbbababbbbbb
bbbbaaababbbaababababbbaabaababaababbbbbbaababbb
bbabbbaabaaabaaabbbababb
aabbababaabaaaaabbbabbabbbaaaaaa
aaababbaabbaabaaabaaaabbaabbabbababbbabbabbaabbb
ababaabaaabaabbbabbaaaaa
ababaabbaaababbaabaaaababbabbbabbbbbbbaaaaaabbaa
baaabaabbbabbabababaabba
aaabaaabaaabaababbbabaabbabbbbbb
aabaaabbaabbaabbabbbababbabbaabaabbabbab
baaaabaaaabaaabbbbbaaaababaaabbabbbababbabababaa
bbaabababbabaaabbbaabaaabaaaabba
abaabaabbbbaaaabbabaabaa
bbbaababaaaabaabababbbbbaabbbabbbaaaaaaa
bbaababbababaababbaaaaaa
bbbbbbbabbbbbbaaabaabbaa
ababbbbbbabbaabbbbaaaaab
bbabbabbaabbabaaaabbbbba
ababbaaababbabbabbaabbbabaabbabbababaabbabbbbaabbbbaaabaaaaabbbaaaaabbabbabbabbb
aaaaaaabaabbbbaababbbabbababbabbbbabaaaababaabbbbbabbabb
baaaabaabababaaaaaabbbaa
ababbbbaaabbaabaaabbababbabababaaaaababbbabaabbaabaabbaabbbbbabb
aabaaabbaaabaababbbaabaabbbbabba
bbabaaabbaabbbaaabbbbbab
bbaabaaabbbbaaababbabbba
aabbabaaabbbbbbbaabbabbb
baabababaabbabababababaa
abbbbabbaaabaababbaabbabbbbaabababaaabbabbbbabbbababababababbaaa
baabbaababababaaabbaabaaaaaabaaaabbabaaabbababaaaaaabbaaabaaabbb
bbbabbbbaaaabaabbbbaaaabbabbbaba
abaaababbabbaabbbbbaabba
ababbabbbaaaabaaabaaabaaabababbbbbbbbbbbbbbabbba
aabbbabaaaaaabaabaaabbbb
aaaaaabaababbbbaabaabbab
ababaaaaabaaabbbbbbbababbabaaababaaaabaaabbabbbb
babbabaaabaaaaabbaaabbaabaaaabaaaababaaa
bbbbbbbaaabbbbabbbbbabbb
abbbbabbbbabbabbbaabababbabaabab
babbbbaabbabaabbabaaabbabaaabbba
bbbabbbbbababababaaabbabbbbbaabb
bbabbabbbaaabbaaaabbaabbabbbbbbbabbbbbbbbabaabbbbabbabbbabaabaaaabbaaaaa
bbabaababaaabbabbbabaabbaabaabbababbbbba
bbabaaabbbaaabaaabbbabbb
aabaaabbaaaabaabababbaaa
abbbaababbabbbaaabbaaaab
abaabbbabbabaaaaaabaaabbaaaaaabbbaabbbba
bbabaabbabbbbbbbaabababb
bababbbaaaaabaabababbbaa
abbbaaaabbbaabababbbbbbaabaaaaabbabbbbbabaabbbbbababbbbabaaababbbbbabbaabbbababa
aaabaababababbaabaabbbabababbaaabaaabbaabaaabbbabbaaaaabaabaaaabaaaaaaaa
abbaaabbababbbbbbaabbaba
aabaababbbabbbabbbabaababbaaaabaabbbbbba
bbaabbaaabbbbaabababbbaa
aababaabababbbbababbbaba
bbbbbbbaaabaababaabbaabbbaaaaabababaabbb
abbbaaaabbbabbbbaababbbb
aaababbaaabbbababaabaaab
bbaaabbababbbbaabaababba
bbbbbaaaabaabbbbabbbaabb
baaabbaabababbabbbbbaaaa
abbbbababbbbbbabbaabaaabbbbbbaab
baabbbabbbbbbbbabbaaaabaababaaaa
aaaaabbaaabbaaaaaabaaabaaaabbbaa
bababbaaaabbaaaaaabbbbaa
abaaabbbaaabaabbabbbaaabaaabaaaaaababbbb
aaabbbbbbbabaaabbbaaabbaababbbbbaabaaaab
aaabbaabaabbaaaabbaaaaab
bbaabaaaaabaaaaaabbabaab
babababaababaabbabbabaab
aabaabbbbbbbbbaabbabaaaaaababbbaaaababaaaaabbbbaabaabbabaaaabbaabbaabaab
bbaaabaaaabbbbabaabbbbabbbbbabba
aaaabaabbaaababbbbbbbbaaabbabaabbbbbbbbb
abbaababbbbabaabbaabbbba
aaaabaabaababbbababbbabb
bbaabbaaaababbabaaabbabaaaaabbaa
aaabaaabaabbabaababaaaaaabaaabaa
aaabbababbaaabbababaabaa
abaaabbaababbbabaabaabbbaabaaaaabbababbb
bbaaabbbaaabaabaabbaabba
bbaababbbbabbbbbbaaababa
baaabbaababbaabaabbbbbbbbabaaaabbbbaabba
baaaabbbbaabaaaabbaaaaaabbbbbabababaaaba
bbaababaaabbbababababaaaabababab
baaaabaabbabbabbbaababbb
bbaaaabaabaaabbababbaababbbbbbbbabbabbab
babbaaaabbababbaaaababbbbabbabaabbababbbbbbabbba
bbabaaabababaabaabbbabba
bbbaababababbbababbabbab
aabbbbabaaabbbbbaabbbbaa
aabaabbbabaaaaababbabbba
bbababababbbbabbabbaabbb
baaaaabbaabbababbbaaaabbbababbbabbbbbaabaaaabbba
bbbaabaaabbabaaabaabaabb
bbbbabaaabbbababbbaabaaabbaabbaa
babbabbbbaabaaaababaaabababbbaaaaaaaabaaaabbababaabababbabbabbbabbabbbaa
aaaaabaaaaaaaabbabbabbaa
aaababbabbbabbbbababbababbbbbbbb
baaabbaabbbbabaaabbbbabbbbababbb
bbabbbbabbbaabaabaabbbabaabaaabbbabaabbababbaaaaaaaabbbb
bbabbbabaabaabaabaaabbba
ababaabbbbaaabaabbaababaaaaabbaabbaabbba
abbbaaaababababbbbbbbbbababbbabb
aabaababbbaabaaaabbabbab
abaabbbabaabaababaaabbbb
baabbbaaabbbbbaabbbabbabaaaaaabaaabaabbbbbaabbaaabbaaaab
bbabaaabaabbababaaabaabb
ababbabaabbbabababbbbaba
abaababaaaaaaabbabbbababaabababaabaabaaa
babababbabbaaaaabbbbabbbaababbbbbaabaabaaabbbbabbabababa
abbaabbaaababbaabaabbababaabaabb
abaabaabbabbabaaabaaabaa
aaaaaaaaaabaabaaabbbababbababbbbaababbaaaaaabbabababbabbbabaabab
bbaaaabaabbbbbaaaaabaaabbaaaabbabaabaaab
ababaabbbaaabaaaaaabbbab
bbabbabaabbaaabbbabbbaab
aaaabbbbaaaabababaabaabb
bbabaaabaaaaabbaaaaabbba
abbbababaabaababababaaab
bbbaaaababaaabbbbabababaabbaabbb
aabbababbaabaababaababaaababaabbbaabbbaa
ababababbaaabbaaababbabaababaaaa
bbaaabbbbbabaabbaabaabaaabaaabaaabbaaaab
bbaababaaabbaaaaaaaaabaaaaaaaababababbababaaaabaaaaaabbb
aaaaabaababbbbaabbabbabaaaaabaabaaaaabbabababbbbabbbbaaa
abbabaaababaaaabaaaaabbbbbbbaaaa
aabbaaaaaabbbaabaabbbbaa
abaabaabbabaaaaabbbbbabbbbababaa
abbaabaabbbabaaaaabbaababbaaaaababbbaaab
bbaabbabaabaabaabaaaabaabbabbaaababaaabb
aaababaabababbbabbbaaaabababbbaa
abaaabbababbbababbbaabababbababb
aababaabaabbbabaabbaaaab
abbabaaabaabbababaabbbbaabbaabbabbbaaaaa
aaabbabaaaabbbbbaabbbaabaaababaaaabaaabbbaabbaaa
babbaabbababaabbaabbabbb
aaabbbbbbbabbbaabaabbaba
abaaabbaabaababaabbaababbaababbaaaabbabb
bbabbbbbaababaabbaabbbbbabbbaabb
baabaabaabbabaaabbaaababaabbaaab
bbbaabababbbbbaaaabbaaaaaabbbaaa
aabaabbbaaabbbabbbbaaabaababababbbabbaabbbbbaababaabbbba
abbbbbaaaaabaabababaaabb
bbbabbbbbbaaaabbabbaaaba
abbabaaaababaabbbaaabbbb
ababbabababbbaaaababbbaa
bbbabaaabbaaabaabbabbaaa
babbaabaabbaabaaaabbabbb
babaaaaaabaaababbababbabbbbbaabababbbbbb
baabbbabaaabaababaaaabba
abbabbbbaabaabababbbabba
baaababbbbaababaaabbabaabbbaababaabbabbababbbbab
abbbbaababaaabbabbababba
bbaabababbaaabbbabbaaaab
baabbaabbbbababaababaaaa
bbabaaaabaabbaababbbaaab
baaaaabbaababaababbaaabbbbaaaaaa
bbabbbbaaabaaabaabbbbabbababbaabbaabbbbb
babbaabbaabbabaaaabbabbb
abaaababbabbbaaabbbbbbbb
abaabbbababbabaaababaabbbbaaabbaaaaabbaa
aabaabbbbbaaaabbaaabaaaa
ababbbbaabaabbbabbbbbabb
aabbbbabaabbbabaaaabbbab
bbabbbbaaaabaababaabaaab
aabbbbbbbbaaabbbbaabbaabaababaabbbababba
abaababbabbabaaaababbbba
aaabbbbbbbabbbbabbbbbbbabbbbbbbaabbaabbabbaabaabbabaabaa
baaabaaaaaababbabababbbb
bbaaaabbaaaaaabbaababbaa
aaaaababbabbbaaabbabaaaaabbbabbbbabbbbab
baaabaabbabbabbabbaaaaaa
bababbbabaaaaaabbaaaabababbbaabbbbbaaaaa
abaaaaabbaaaabaabbbbbbaabaaabbaababaabbb
bbaaabbababbbaaabbbbaaba
babbaabbabbbbbaababbbbab
abaabbbbbbaaababbabababbbabbabababbbabbbbaaabbbb
babbabababbbbaabaaababaaaabaabba
abbabbaaabaabaaaabbaabbabbbaaaaa
bbaaaababbabaaabaabbabba
bbabaaabaaaabaabbbbaaaabaabbbbaa
bbabbbbbbbbbbbaaaabbbbbaabaabaaa
bbbbaaabaaabbabaaaababab
babbbbaabaaaaabbbbaaaababbabbbbbaababbbabbababbbbaaaabba
aabbbbabbbbbbaaaabbaaaaa
bbaabababbabaaabbabbbbab"""