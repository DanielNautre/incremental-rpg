#!/usr/bin/python3.6
# -*- coding: utf8 -*


gear = {
    'Stick': {'type': 'sword', 'lvl': 1, 'price': 0, 'damage': 0.2, 'speed': 1.2, 'tt': 'A small and fragile stick found on the ground'},
    'Sandals': {'type': 'feet', 'lvl': 1, 'price': 5, 'armor': 1, 'tt': 'Overpriced plastics thongs. what\'s plastic anyway ?'},
    'Gomina': {'type': 'head', 'lvl': 1, 'price': 15, 'armor': 0.5, 'tt': 'From a distance, it almost looks like you\re wearing an helmet'},
    'Bandana': {'type': 'head', 'lvl': 1, 'price': 25, 'armor': 1, 'tt': 'Fashionnable piece of cloth with a pearsley pattern printed on it, thin but good looking'},
    'Potato sac': {'type': 'torso', 'lvl': 1, 'price': 20, 'armor': 1, 'tt': 'Better than nothing I suppose.'},
    'Dragonforce T-shirt': {'type': 'torso', 'lvl': 1, 'price': 45, 'armor': 1.5, 'tt': 'Nothing is more medieval than a Dragonforce T-shirt.'}
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

