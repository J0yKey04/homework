class buuu:
    def __init__(self, value, parent = None, left = None, right = None):
        self.v = value
        self.l = left
        self.r = right

class Binary__Tree:
    def __init__(self):
        self.ro = None

    def add(self, value):
        if self.ro is None:
            self.ro = buuu(value)
        else:
            cde = self.ro
            while True:
                if value < cde.v:
                    if cde.l is None:
                        cde.l = buuu(value, cde)
                        return
                    cde = cde.l
                else:
                    if cde.r is None:
                        cde.r = buuu(value, cde)
                        return
                    cde = cde.r

    def get(self, cde=0):
        if cde == 0:
            cde = self.ro
        if cde is None:
            return []
        if cde.l is None and cde.r is None:
            return[cde.v]
        else:
            return (self.get(cde.l) +
                self.get(cde.r))


n = int(input())
d = [int(x) for x in input().split()]
zip = {x for x in d}
tree = Binary__Tree()
for num in d:
    if num in zip:
        tree.add(num)
        zip.remove(num)
d = tree.get()
print(*d)

