#!/usr/bin/python3.6
# -*- coding: utf8 -*


gear = {
    'Stick': {'type': 'weapon', 'subtype': 'mace', 'lvl': 1, 'price': 0, 'damage': 0.3, 'speed': 1.4, 'tt': 'A small and fragile stick found on the ground'},
    'Sandals': {'type': 'feet', 'lvl': 1, 'price': 5, 'armor': 0.5, 'tt': 'Overpriced plastics thongs. what\'s plastic anyway ?'},
    'Gomina': {'type': 'head', 'lvl': 1, 'price': 15, 'armor': 0.5, 'tt': 'From a distance, it almost looks like you\re wearing an helmet'},
    'Potato sac': {'type': 'torso', 'lvl': 1, 'price': 20, 'armor': 1, 'tt': 'Better than nothing I suppose.'},
    'Bandana': {'type': 'head', 'lvl': 1, 'price': 55, 'armor': 1, 'tt': 'Fashionnable piece of cloth with a pearsley pattern printed on it, thin but good looking'},
    'Dragonforce T-shirt': {'type': 'torso', 'lvl': 1, 'price': 65, 'armor': 1.5, 'tt': 'Nothing is more medieval than a Dragonforce T-shirt.'},
    'Club': {'type': 'weapon', 'subtype': 'mace', 'lvl': 1, 'price': 70, 'damage': 1, 'speed': 1.1, 'tt': 'A solid piece of oak wood'},
    'Worn Shoes': {'type': 'feet', 'lvl': 1, 'price': 95, 'armor': 1.4, 'tt': 'They smell like bad cheese but they provide some protection'},
    'Dagger': {'type': 'weapon', 'subtype': 'sword', 'lvl': 2, 'price': 250, 'damage': 1.2, 'speed': 1.5, 'tt': 'A quick and deadly weapon, if you can get close enough'}
}


def remove_gear(bought_gear):
    # remove bought gear and all inferior items
    tbd = [bought_gear]
    for name, stuff in gear.items():
        if stuff['type'] == gear[bought_gear]['type']:
            if stuff['price'] < gear[bought_gear]['price']:
                tbd.append(name)

    for name in tbd:
        del gear[name]


def get_available_gear(lvl):
    available = {}

    for name, stuff in gear.items():
        if stuff['lvl'] <= lvl:
            available[name] = stuff

    return available
