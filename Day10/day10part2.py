data = [x.split(" ") for x in open("day10input.txt", "r").read().splitlines()]

signals = [1]

for ins in data:
    X = signals[-1]
    if ins[0] == 'noop':
        signals.append(X)
    else:
        signals.extend([X, X+int(ins[1])])

screen = [list("."*40) for _ in range(6)]
for i, x in enumerate(signals):
    row = i // 40
    col = i - (row * 40)
    
    if abs(col - x) <= 1:
        screen[row][col] = "#"

for i in screen:
    print(''.join(i))