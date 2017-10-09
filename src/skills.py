#!/usr/bin/python3.6
# -*- coding: utf8 -*

skills = {
    'Strength': {'lvl': 1, 'lvl_step': 1, 'step': 2, 'desc': 'Damage is increased by <strong>{value}</strong>%', 'tt': 'The stronger you become, the harder you hit'},
    'Dexterity': {'lvl': 1, 'lvl_step': 1, 'step': 2, 'desc': 'Armor is increased by <strong>{value}</strong>%', 'tt': 'Avoid enemy blows'},
    'Intelligence': {'lvl': 1, 'lvl_step': 1, 'step': 2, 'desc': 'you gain <strong>{value}</strong>% more XP per second', 'tt': 'Wisdom helps you learn faster'},
    'Fiery Weapon': {'lvl': 5, 'lvl_step': 5, 'step': 5, 'desc': 'You cause <strong>{value}</strong>% fire damage', 'tt': 'Your imbue your weapon with fire'},
    'Mana Shield': {'lvl': 6, 'lvl_step': 3, 'step': 4, 'desc': 'Your armor value is increased by <strong>{value}</strong>%', 'tt': 'You focus your energy to create a protective mana shield'}

}


def get_available_skills(lvl):
    available = {}

    for name, skill in skills.items():
        if skill['lvl'] <= lvl:
            available[name] = skill

    return available
