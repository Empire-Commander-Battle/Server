import re
import os

command_regex = re.compile(r"^([^#][^\s]*)[\s]*((\[<[^>]*>\]|<[^>]*>)\s+)*#(.*)$")

lines = []
with open("readme.txt", "r") as f:
    lines = f.readlines()


def escape(s):
    s = str(s)
    s = s.replace("\\", "\\\\")
    s = s.replace("\"", "\\\"")
    return s

tprint = print
f = open(os.getenv("HOME") + "/.emacs.d/warband-commands.el", "w+")

def print(*args, **kwargs):
    tprint(*args, **kwargs, file=f)

print("(defvar warband-server-commands\n  (list", end='')
for line in lines:
    result = re.search(command_regex, line)
    if result:
        groups = result.groups()
        print(f"\n   (list \"{escape(groups[0])}\"", end='')
        for arg in groups[2:-1:2]:
            if arg is None:
                continue
            print(f" \"{escape(arg)}\"", end='')
        print(f" \"{escape(groups[-1].strip())}\")", end='')
print("))\n\n(provide 'warband-commands)")

f.close()
