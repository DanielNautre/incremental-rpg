#!/usr/bin/python3.6
# -*- coding: utf8 -*

import random

phrase_list = [
    'Crushing {monster} with his {weapon}',
    'Slicing {monster}',
    'Pureeing {monster}',
    'Getting his ass handed over by {monster}',
    'Making fun of {monster}',
    'Taking a leak on {monster}',
    'Looting the corpse of {monster}',
    'Exploring {place}',
    'Travelling through {place}',
    'Taking on {dungeon}',
    'Discussing {topic} with {npc}',
    'Meditating on {topic}',
    'Drinking a healing potion',
    'Dropping his {weapon} on the ground',
    'Blaming his {weapon} for not doing enough damage',
    'Wiping blood from his {weapon}'
]

monster_list = [
    {'name': 'a Bat', 'lvl': 1},
    {'name': 'a Spider', 'lvl': 1},
    {'name': 'a Rat', 'lvl': 1},
    {'name': 'a Wolf', 'lvl': 2},
    {'name': 'a Bear', 'lvl': 3},
    {'name': 'a Skeleton', 'lvl': 4},
    {'name': 'a Skeleton Archer', 'lvl': 5},
    {'name': 'an Orc', 'lvl': 10}
]

npc_list = [
    'Sylvia the healer',
    'Wise Deckard',
    'Cross-eyed Mary',
    'That guy who took an arrow to the knee',
    'A benevolent Orc'
    'Handsome John'
]

topic_list = [
    'the art of killing',
    'how to best deal with {monster}',
    'the geopolitical consequences of the apocalypse',
    'his latest scars',
    'the pros and cons of battling while drunk',
]

place_list = [
    {'name': 'the countryside', 'lvl': 1},
    {'name': 'the highlands', 'lvl': 1},
    {'name': 'the desert', 'lvl': 3}

]

dungeon_list = [
    {'name': 'a dark cellar', 'lvl': 1},
    {'name': 'a dark cave', 'lvl': 2}
]


def get_action(lvl, weapon):
    phrase = random.choice(phrase_list)
    monster = random.choice(get_lvled_item(lvl, monster_list))
    place = random.choice(get_lvled_item(lvl, place_list))
    dungeon = random.choice(get_lvled_item(lvl, dungeon_list))
    topic = random.choice(topic_list).format(monster=monster)
    npc = random.choice(npc_list)
    s = phrase.format(monster=monster, place=place, topic=topic, npc=npc, weapon=weapon, dungeon=dungeon)
    return s


def get_lvled_item(lvl, lvl_list):
    new_list = []
    for item in lvl_list:
        if item['lvl'] <= lvl:
            new_list.append(item['name'])

    return new_list



if __name__ == '__main__':

    for i in range(1, 15):
        print(get_action(i, 'equipped_weapon'))