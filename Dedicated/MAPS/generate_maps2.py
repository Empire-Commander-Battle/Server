#!/usr/bin/env python3
import argparse
import re
import pathlib
import sys
import shutil

def map_dir_type(arg):
    path = pathlib.Path(arg)

    if not path.exists():
        raise argparse.ArgumentTypeError(f"{path} doesn't exists")

    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"{path} isn't a directory")

    return path

def output_dir_type(arg):
    path = pathlib.Path(arg)

    if not path.is_dir() and path.exists():
        raise argparse.ArgumentTypeError(f"{path} isn't a directory")

    return path

def shared_maps_dir_type(arg):
    path = pathlib.Path(arg)

    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"{path} isn't a directory")

    return path

def scenes_file_type(arg):
    path = pathlib.Path(arg)

    if not path.exists():
        raise argparse.ArgumentTypeError(f"{path} doesn't exist")

    if not path.is_file():
        raise argparse.ArgumentTypeError(f"{path} isn't a file")

    return path

parser = argparse.ArgumentParser(
    description = "generate maps files based on map directory"
)

parser.add_argument("maps_dir", type = map_dir_type)
parser.add_argument("output_dir", type = output_dir_type)
parser.add_argument("--scenes_file", type = scenes_file_type,
                    default = pathlib.Path(__file__).parent / "scenes.txt")
parser.add_argument("--shared_maps_dir", type = shared_maps_dir_type,
                    default = pathlib.Path(__file__).parent / "shared_maps")
parser.add_argument("--insert_maps", nargs = "*", default = [])
parser.add_argument("--init_file", type = argparse.FileType('w'), default = sys.stdout)
parser.add_argument("--skip_maps", type = int, default = 162)


args = parser.parse_args()

maps_dir = args.maps_dir
shared_maps_dir = args.shared_maps_dir
output_dir = args.output_dir
scenes_file = args.scenes_file
insert_maps = args.insert_maps
init_file = args.init_file
skip_maps = args.skip_maps

scenes_regex = re.compile(r"^scenesfile +version +1 *\n +\d+ *\n(\w+ +\w+ +\d+ +\w+ +\w+ +((|-)\d+\.\d+ +){5}0(x[0-9a-f]+|) *\n( *0 *\n){2} *\w+ *\n)*\w+ +\w+ +\d+ +\w+ +\w+ +((|-)\d+\.\d+ +){5}0(x[0-9a-f]+|) *\n( *0 *\n){2} *\w+ *\n*$")
code_regex = re.compile(r"^\w+ +\w+ +\d+ +\w+ +\w+ +((|-)\d+\.\d+ +){5}0(x[0-9a-f]+|) *\n( *0 *\n){2} *\w+ *\n*$")
insert_regex = re.compile(r"^add_map (\w+)$")
custom_map_regex = re.compile(r"^mp_custom_map_\d+$")

maps = list(filter(lambda x: x.suffix == ".sco", maps_dir.iterdir()))

# i have no fucking idea why functools solution isn't working so this code assumes that iterdir sorts alphabetically
maps.sort(key=lambda x: len(x.name))

# check correctness before running
codes = []
for m in maps:
    code_file = maps_dir / (m.stem + ".txt")
    if not code_file.exists():
        print(f"{code_file} doesn't exist", file = sys.stderr)
        exit(1)

    if not code_file.is_file():
        print(f"{code_file} isn't a file", file = sys.stderr)
        exit(1)

    with open(code_file, "r") as f:
        code = f.read()

        if not code_regex.match(code):
            print(f"{code_file} doesn't follow codefile format", file = sys.stderr)
            exit(1)

        codes.append(code.strip())


inserts_file = maps_dir / "inserts.txt"
if inserts_file.exists():
    if not inserts_file.is_file():
        print(f"{inserts_file} inserts file isn't a file", file = sys.stderr)
        exit(1)

    with open(inserts_file, "r") as f:
        for line in f.readlines():
            rmatch = insert_regex.match(line)

            if not rmatch:
                print(f"{line} in inserts file doesn't follow format", file = sys.stderr)
                exit(1)

            insert_maps.append(rmatch.groups()[0])


scenes = ""
with open(scenes_file, "r") as f:
    scenes = f.read()
    if not scenes_regex.match(scenes):
        print(f"{scenes_file} doesn't follow scenesfile format", file = sys.stderr)
        exit(1)

    scenes = scenes.strip().split("\n")

    maps_no = (len(scenes) - 2)/4
    if maps_no < skip_maps + len(maps):
        print(f"{scenes_file} scenes file does {maps_no} maps which is less than required ammonut of {skip_maps + len(maps)} maps", file = sys.stderr)
        exit(1)

# ensure that output can be done
if not output_dir.exists():
    output_dir.mkdir()


maps_output_dir = output_dir / "SceneObj/"

if maps_output_dir.exists():
    if maps_output_dir.is_dir():
        shutil.rmtree(maps_output_dir)
    elif maps_output_dir.is_file():
        maps_output_dir.unlink()

maps_output_dir.mkdir()

scenes_output_file = output_dir / "scenes.txt"
if scenes_output_file.exists():
    if scenes_output_file.is_dir():
        shutil.rmtree(scenes_output_file)
    elif scenes_output_file.is_file():
        scenes_output_file.unlink()


# after checks
shared_maps = list(filter(lambda x: x.suffix == ".sco", shared_maps_dir.iterdir()))
for s in shared_maps:
    shutil.copyfile(s, maps_output_dir / s.name)

for m in maps:
    shutil.copyfile(m, maps_output_dir / m.name)

with open(scenes_output_file, "w+") as f:
    f.write("\n".join(scenes[:2 + skip_maps*4]) + "\n")
    for i, code in enumerate(codes):
        code_splited = code.split(" ", 2)
        scenes_splited = scenes[2 + (skip_maps + i)*4].split(" ", 2)

        f.write(code_splited[0] + " " + scenes_splited[1] + " " + code_splited[2] + "\n")

    f.write("\n".join(scenes[2 + (skip_maps + len(maps))*4:]))




print("set_map " + scenes[2 +  skip_maps*4].split(" ", 2)[1], file = init_file)

seen = set()
custom_maps = 0
for i in range(len(maps)):
    name = scenes[2 + (skip_maps + i)*4].split(" ", 2)[1]

    seen.add(name)

    if custom_map_regex.match(name):
        custom_maps += 1

    print("add_map " + name, file = init_file)

for name in insert_maps:
    if name in seen:
        continue

    if custom_map_regex.match(name):
        custom_maps += 1

    print(f"add_map " + name, file = init_file)


print(f"custom_maps_enabled {custom_maps}", file = init_file)

print(f"OK")
