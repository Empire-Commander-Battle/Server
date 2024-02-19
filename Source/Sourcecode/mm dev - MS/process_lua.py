from module_info import *

import os
import shutil

import re

print "Exporting lua..."

lua_dir = export_dir + "lua/"
msfiles_dir = lua_dir + "msfiles/"

if os.path.exists(lua_dir):
    shutil.rmtree(lua_dir)
shutil.copytree("lua", lua_dir)

os.mkdir(msfiles_dir)

header_file_regex = re.compile("^header_.*\.py")
for file_name in os.listdir("."):
    if not header_file_regex.match(file_name):
        continue

    shutil.copyfile(file_name, msfiles_dir + file_name)

shutil.copyfile("module_constants.py", msfiles_dir + "module_constants.py")
