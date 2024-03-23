#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 3:
    print('Invalid arguments!', file=sys.stderr)
    exit(1)

template = sys.argv[1]
map_template = sys.argv[2]

template_name = template.rpartition('.')

if template_name[1] == '':
    print('Invalid template!', file=sys.stderr)
    exit(2)

template_name = template_name[0]

variables = []
with open('CONFIG_VARIABLES.txt') as f:
    for line in f:
        if line[:-2] == template_name:
            for line in f:
                if line[0] != '\t':
                    break

                line = line.partition(':')

                if line[1] == '':
                    print('Invalid variable!', file=sys.stderr)
                    exit(3)

                variables.append((line[0].strip(), line[2].strip()))
            break

maps = ''
with open(map_template) as f:
    maps = f.read()

template_str = ''
with open(template) as f:
    template_str = f.read()

template_str = template_str.replace('$MAPS', maps)
for name, val in variables:
    template_str = template_str.replace('$' + name, val)

with open('INIT.txt', 'w+') as f:
    f.write(template_str)
