import sys

input = sys.stdin.readline

stack_list = []

def run_command(cmd):
    cmd = str(cmd).rstrip('\n')
    if cmd[0] == '1':
        a = list(cmd.split())
        stack_list.append(a[1])
    elif cmd == '2':
        if not stack_list:
            print(-1)
        else:
            print(stack_list.pop())
    elif cmd == '3':
        print(len(stack_list))
    elif cmd == '4':
        if not stack_list:
            print(1)
        else:
            print(0)
    elif cmd == '5':
        if not stack_list:
            print(-1)
        else:
            print(stack_list[-1])
N = int(input())

for _ in range(N):
    command = input()
    run_command(command)
    