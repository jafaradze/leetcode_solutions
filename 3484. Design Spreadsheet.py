class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}
        for i in range(1, rows + 1):
            for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                key = j + str(i)
                self.sheet[key] = 0
        

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula.lstrip('=').split('+')
        if not a.isdigit():
            a = self.sheet[a]
        else:
            a = int(a)
        if not b.isdigit():
            b = self.sheet[b]
        else:
            b = int(b)
        return a + b