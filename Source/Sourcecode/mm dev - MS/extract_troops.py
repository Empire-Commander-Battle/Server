import csv
import math

import argparse

from header_troops import *
from module_troops import *

parser = argparse.ArgumentParser(
    prog='extract-troops',
    description='extract troops data form source code')

parser.add_argument('outfile',
                    type=str)

args = parser.parse_args()

OUTFILE = args.outfile

# MAIN

troop_id = 0
troop_name = 1
troop_reserved = 5
troop_faction = 6
troop_attribs = 8
troop_profs = 9
troop_skills = 10

str_bits = 0
agi_bits = 8
int_bits = 16
cha_bits = 24

# ironflesh to start since it is the most important one
ironflesh_bits = int(math.log(knows_ironflesh_1, 2))
trade_bits = int(math.log(knows_trade_1, 2))
leadership_bits = int(math.log(knows_leadership_1, 2))
prisoner_management_bits = int(math.log(knows_prisoner_management_1, 2))
persuasion_bits = int(math.log(knows_persuasion_1, 2))
engineer_bits = int(math.log(knows_engineer_1, 2))
first_aid_bits = int(math.log(knows_first_aid_1, 2))
surgery_bits = int(math.log(knows_surgery_1, 2))
wound_treatment_bits = int(math.log(knows_wound_treatment_1, 2))
inventory_management_bits = int(math.log(knows_inventory_management_1, 2))
spotting_bits = int(math.log(knows_spotting_1, 2))
pathfinding_bits = int(math.log(knows_pathfinding_1, 2))
tactics_bits = int(math.log(knows_tactics_1, 2))
tracking_bits = int(math.log(knows_tracking_1, 2))
trainer_bits = int(math.log(knows_trainer_1, 2))
looting_bits = int(math.log(knows_looting_1, 2))
horse_archery_bits = int(math.log(knows_horse_archery_1, 2))
athletics_bits = int(math.log(knows_athletics_1, 2))
shield_bits = int(math.log(knows_shield_1, 2))
weapon_master_bits = int(math.log(knows_weapon_master_1, 2))
power_draw_bits = int(math.log(knows_power_draw_1, 2))

skills_bits = [
    ironflesh_bits,
    trade_bits,
    leadership_bits,
    prisoner_management_bits,
    persuasion_bits,
    engineer_bits,
    first_aid_bits,
    surgery_bits,
    wound_treatment_bits,
    inventory_management_bits,
    spotting_bits,
    pathfinding_bits,
    tactics_bits,
    tracking_bits,
    trainer_bits,
    looting_bits,
    horse_archery_bits,
    athletics_bits,
    shield_bits,
    weapon_master_bits,
    power_draw_bits,
]

skills_names = [
    'ironflesh',
    'trade',
    'leadership',
    'prisoner_management',
    'persuasion',
    'engineer',
    'first_aid',
    'surgery',
    'wound_treatment',
    'inventory_management',
    'spotting',
    'pathfinding',
    'tactics',
    'tracking',
    'trainer',
    'looting',
    'horse_archery',
    'athletics',
    'shield',
    'weapon_master',
    'power_draw',
]

def get_attrb(attribs, bits):
    return int(attribs >> bits) & 0xFF

def get_wep_prof(profs, bits):
    return (profs >> bits) & 0x3FF

def get_skill(skills, bits):
    return int(skills >> bits) & 0xF

faction_whitelist = {
    fac_britain: 'Britain',
    fac_rhine: 'Rhine',
    fac_russia: 'Russia',
    fac_prussia: 'Prussia',
    fac_austria: 'Austria',
    fac_france: 'France'
}

with open(OUTFILE, 'w+') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['name',
                     'faction',
                     'strength',
                     'agility',
                     'intelligence',
                     'charisma',
                     'one handed',
                     'two handed',
                     'polearm',
                     'archery',
                     'crossbow',
                     'throwing',
                     'firearm'] + skills_names)

    for troop in troops:
        if troop[troop_faction] not in faction_whitelist:
            continue

        if troop[troop_id][-2:] == 'ai':
            continue

        if troop[troop_reserved] != 0:
            continue

        if '!' in troop[troop_name]:
            continue

        row = [troop[troop_name]]

        row.append(faction_whitelist[troop[troop_faction]])

        attribs = troop[troop_attribs]
        row.append(get_attrb(attribs, str_bits))
        row.append(get_attrb(attribs, agi_bits))
        row.append(get_attrb(attribs, int_bits))
        row.append(get_attrb(attribs, cha_bits))

        profs = troop[troop_profs]
        row.append(get_wep_prof(profs, one_handed_bits))
        row.append(get_wep_prof(profs, two_handed_bits))
        row.append(get_wep_prof(profs, polearm_bits))
        row.append(get_wep_prof(profs, archery_bits))
        row.append(get_wep_prof(profs, crossbow_bits))
        row.append(get_wep_prof(profs, throwing_bits))
        row.append(get_wep_prof(profs, firearm_bits))

        skills = troop[troop_skills]

        for bits in skills_bits:
            row.append(get_skill(skills, bits))

        writer.writerow(row)
