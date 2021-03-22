# Full 0,-4, 55 min 
```
return [list(range(7, 17, 1)),
            list(range(12, 27, 1)),
            list(range(15, 37, 1)),
            list(permutations(range(1, 5), 4))]
            
C:\Users\guilh\miniconda3\python.exe C:/Users/guilh/Dropbox/projetos/maguic/tests/test_aces.py
C:\Users\guilh\Dropbox\projetos\maguic\openmagic\effects\four_aces.py:62: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
  return concatenate(ps[[self.sorting_order]])
[10 11 12 13 14 15 16 17 18 19  9 20 31 32 33 34 35 36 37 38 39 40 41 42
 43 44 45 46 47 48 49 50 51 52  5  6  7  8 21 22 23 24 25 26 27 28 29 30]
delta 0 20 meaning dez de espadas
delta -4 17 meaning quatro de paus
delta 0 9 meaning cinco de paus
delta -4 18 meaning quatro de ouros
[[7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]]
100%|██████████| 79200/79200 [07:14<00:00, 182.13it/s]
51 used positions: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
52711 generated rules
Satisfiable? sat
Elapsed 3299.3885565 seconds
(:added-eqs                      14794640
 :arith-eq-adapter               4574
 :arith-bound-propagations-cheap 18322
 :arith-diseq                    9371
 :arith-lower                    13696
 :arith-make-feasible            5930
 :arith-max-columns              58
 :arith-propagations             18322
 :arith-upper                    4634
 :binary-propagations            10205
 :conflicts                      4686042
 :decisions                      7234407
 :del-clause                     4680745
 :final-checks                   1
 :max-memory                     222.22
 :memory                         32.88
 :minimized-lits                 117082363
 :mk-bool-var                    9255
 :mk-clause                      4717496
 :num-allocs                     5531414604240.00
 :num-checks                     1
 :pb-conflicts                   4926
 :pb-predicates                  2703
 :pb-propagations                62469758
 :pb-resolves                    4926
 :propagations                   262911034
 :restarts                       2088
 :rlimit-count                   567966301
 :time                           3296.98)
{
1: 'as de espadas',
2: 'as de copas',
3: 'as de ouros',
4: 'as de paus',
5: 'rei de ouros',
6: 'dama de paus',
7: 'sete de espadas',
8: 'oito de ouros',
9: 'sete de ouros',
10: 'seis de ouros',
11: 'nove de copas',
12: 'tres de copas',
13: 'dois de copas',
14: 'cinco de paus',
15: 'seis de copas',
16: 'sete de copas',
17: 'nove de ouros',
18: 'dama de copas',
19: 'dama de ouros',
20: 'oito de copas',
21: 'tres de ouros',
22: 'dez de copas',
23: 'valete de espadas',
24: 'dois de ouros',
25: 'oito de paus',
26: 'sete de paus',
27: 'dois de espadas',
28: 'nove de espadas',
29: 'quatro de ouros',
30: 'seis de espadas',
31: 'valete de paus',
32: 'cinco de espadas',
33: 'cinco de copas',
34: 'rei de espadas',
35: 'quatro de espadas',
36: 'quatro de copas',
37: 'oito de espadas',
38: 'valete de copas',
39: 'valete de ouros',
40: 'tres de espadas',
41: 'dez de ouros',
42: 'rei de copas',
43: 'rei de paus',
45: 'cinco de ouros',
52: 'dois de paus',
53: 'tres de paus',
54: 'seis de paus',
55: 'nove de paus',
56: 'quatro de paus',
57: 'dez de espadas',
58: 'dez de paus',
59: 'dama de espadas',
}
```






# Spelling with last N: # test_aces = 24k, 0, -4 => dois juntos 7 a 10, 3min!!!!

```
C:\Users\guilh\miniconda3\python.exe C:/Users/guilh/Dropbox/projetos/maguic/tests/test_aces.py
[10 11 12 13 14 15 16 17 18 19  9 20 31 32 33 34 35 36 37 38 39 40 41 42
 43 44 45 46 47 48 49 50 51 52  5  6  7  8 21 22 23 24 25 26 27 28 29 30]
delta 0 20 meaning dez de espadas
delta -4 17 meaning quatro de paus
delta 0 9 meaning cinco de paus
delta -4 18 meaning quatro de ouros
[[7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]]
C:\Users\guilh\Dropbox\projetos\maguic\openmagic\effects\four_aces.py:64: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
  return concatenate(ps[[self.sorting_order]])
100%|██████████| 24000/24000 [03:15<00:00, 123.08it/s]
51 used positions: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
24055 generated rules


[0,-4] [] os dois juntos!!!! 

espaco mais avancado
Satisfiable? sat
Elapsed 216.4030246 seconds
(:added-eqs                      2042437
 :arith-eq-adapter               2810
 :arith-bound-propagations-cheap 10168
 :arith-diseq                    5141
 :arith-lower                    7884
 :arith-make-feasible            3437
```

# # test_aces = 79k, 0, -4 => dois juntos 7 a 10

```
C:\Users\guilh\miniconda3\python.exe C:/Users/guilh/Dropbox/projetos/maguic/tests/test_aces.py
C:\Users\guilh\Dropbox\projetos\maguic\openmagic\effects\four_aces.py:64: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
  return concatenate(ps[[self.sorting_order]])
[10 11 12 13 14 15 16 17 18 19  9 20 31 32 33 34 35 36 37 38 39 40 41 42
 43 44 45 46 47 48 49 50 51 52  5  6  7  8 21 22 23 24 25 26 27 28 29 30]
delta 0 20 meaning dez de espadas
delta -4 17 meaning quatro de paus
delta 0 9 meaning cinco de paus
delta -4 18 meaning quatro de ouros
[[7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]]
100%|██████████| 79200/79200 [07:07<00:00, 185.06it/s]
51 used positions: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
52711 generated rules
Satisfiable? sat
Elapsed 3303.5150018 seconds
(:added-eqs                      14794640
 :arith-eq-adapter               4574
 :arith-bound-propagations-cheap 18322
 :arith-diseq                    9371
 :arith-lower                    13696
 :arith-make-feasible            5930
 :arith-max-columns              58
 :arith-propagations             18322
 :arith-upper                    4634
 :binary-propagations            10205
 :conflicts                      4686042
 :decisions                      7234407
 :del-clause                     4680745
 :final-checks                   1
 :max-memory                     222.22
 :memory                         32.88
 :minimized-lits                 117082363
 :mk-bool-var                    9255
 :mk-clause                      4717496
 :num-allocs                     5531414604240.00
 :num-checks                     1
 :pb-conflicts                   4926
 :pb-predicates                  2703
 :pb-propagations                62469758
 :pb-resolves                    4926
 :propagations                   262911034
 :restarts                       2088
 :rlimit-count                   567966301
 :time                           3301.24)
{
1: 'as de espadas',
2: 'as de copas',
3: 'as de ouros',
4: 'as de paus',
5: 'rei de ouros',
6: 'dama de paus',
7: 'sete de espadas',
8: 'oito de ouros',
9: 'sete de ouros',
10: 'seis de ouros',
11: 'nove de copas',
12: 'tres de copas',
13: 'dois de copas',
14: 'cinco de paus',
15: 'seis de copas',
16: 'sete de copas',
17: 'nove de ouros',
18: 'dama de copas',
19: 'dama de ouros',
20: 'oito de copas',
21: 'tres de ouros',
22: 'dez de copas',
23: 'valete de espadas',
24: 'dois de ouros',
25: 'oito de paus',
26: 'sete de paus',
27: 'dois de espadas',
28: 'nove de espadas',
29: 'quatro de ouros',
30: 'seis de espadas',
31: 'valete de paus',
32: 'cinco de espadas',
33: 'cinco de copas',
34: 'rei de espadas',
35: 'quatro de espadas',
36: 'quatro de copas',
37: 'oito de espadas',
38: 'valete de copas',
39: 'valete de ouros',
40: 'tres de espadas',
41: 'dez de ouros',
42: 'rei de copas',
43: 'rei de paus',
45: 'cinco de ouros',
52: 'dois de paus',
53: 'tres de paus',
54: 'seis de paus',
55: 'nove de paus',
56: 'quatro de paus',
57: 'dez de espadas',
58: 'dez de paus',
59: 'dama de espadas',
}

Process finished with exit code 0
```

