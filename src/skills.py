#!/usr/bin/python3.6
# -*- coding: utf8 -*

skills = {
    'Strength': {'lvl': 1, 'desc': 'Damage is increased by <strong>{value}</strong>%', 'tt': 'The stronger you become, the harder you hit'},
    'Dexterity': {'lvl': 1, 'desc': 'Armor is increased by <strong>{value}</strong>%', 'tt': 'Avoid enemy blows'},
    'Intelligence': {'lvl': 1, 'desc': 'you gain <strong>{value}</strong>% more XP per second', 'tt': 'Wisdom helps you learn faster'}

}


def get_available_skills(lvl):
    available = {}

    for name, skill in skills.items():
        if skill['lvl'] <= lvl:
            available[name] = skill

    return available
