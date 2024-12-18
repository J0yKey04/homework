def reverse_groups(gr, st):

  gr_length = len(st) // gr
  reversed_st = ""
  for i in range(gr):
    gr = st[i * gr_length:(i + 1) * gr_length]
    reversed_st += gr[::-1]
  return reversed_st

groups = int(input())
string = input()

reversed_string = reverse_groups(groups, string)

print(reversed_string)

