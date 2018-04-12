
def getcmd(str):
    s = str.split(" ", 1)
    # print(cmd)
    cmd = command.get(s[0])
    if not cmd:
        return "cann't find this command"
    return cmd()


def update():
    print("update")
    return 123


command = {'update': update}