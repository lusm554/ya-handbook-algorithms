def printr(r):
  print(' ', ' '.join(str(x) for x in range(len(r[0]))))
  for i, l in enumerate(r):
    print(i, ' '.join(str(x) for x in l)) 
  print()  
  
n, m = 10, 10
r = [[' ' for _ in range(m)] for _ in range(n)]
r[0][0] = 'L' # default lose position
printr(r)

# set default winning positions
possible_moves = [
  [0, 1],
  [1, 0],
  [0, 2],
  [2, 0],
  [2, 1],
  [1, 2],
]
for mov in possible_moves:
  if mov[0] < n and mov[1] < m:
    r[mov[0]][mov[1]] = 'W'
printr(r)

for i in range(1, n):
  _n, _m = i, 0
  print(f"{_n=} {_m=} curr={r[_n][_m]} prev={r[_n-1][_m]}")
  '''
  if r[i-1][0] == 'W':
    r[i][0] = 'L'
  else:
    r[i][0] = 'W'
  '''
#printr(r)
exit()

for j in range(1, m):
  if r[0][j-1] == 'W':
    r[0][j] = 'L'
  else:
    r[0][j] = 'W'
print('fill m')
printr(r)
print()

for i in range(1, n):
  for j in range(1, m):
    if r[i-1][j-1] == 'W' and r[i][j-1] == 'W' and r[i-1][j] == 'W':
      r[i][j] = 'L'
    else:
      r[i][j] = 'W'
print('fill body')
printr(r)
print()
print(r[n-1][m-1])
