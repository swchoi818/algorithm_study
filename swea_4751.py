T = int(input())

for _ in range(T):
    word_str = input()
    width = (len(word_str) * 5 - len(word_str) + 1)
    for i in range(5):
        if i == 0 or i == 4:
            print(f"..{'...'.join(['#'] * (width // 4))}..")
        elif i == 1 or i == 3:
            print(f".{'.'.join(['#'] * (width // 2))}.")
        elif i == 2:
            print(f"#.{'.#.'.join(list(word_str))}.#")
