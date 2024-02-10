import os
import re
import shutil

cwd = os.path.dirname(os.path.realpath(__file__))
destination = os.path.join(cwd, "../../Source/Sourcecode/mm dev - MS/")
output = "/tmp/out"

if os.path.exists(output):
    shutil.rmtree(output)
    os.mkdir(output)
else:
    os.mkdir(output)

addon_regex = re.compile("(.*)_addon(\.[^\.]*)")
for filename in os.listdir(cwd):
    addon_regex_out = addon_regex.match(filename)
    if addon_regex_out:
        standard_name = ''.join(addon_regex_out.groups())

        path = os.path.join(destination, standard_name)
        if not os.path.exists(path):
            print("No such path %s" % path)
            continue

        content = ''
        with open(path, 'r') as f:
            content = f.read()

        with open(filename, "r") as f:
            if content[-2:] != '\n\n':
                content += '\n'
            content += "## WSE2 PATCH\n" + f.read()

        with open(os.path.join(output, standard_name), "w+") as f:
            f.write(content)
