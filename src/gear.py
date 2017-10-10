#!/usr/bin/python3.6
# -*- coding: utf8 -*


gear = {
    'Stick': {'type': 'weapon', 'subtype': 'mace', 'lvl': 1, 'price': 0, 'damage': 0.4, 'speed': 1.4, 'tt': 'A small and fragile stick found on the ground'},
    'Sandals': {'type': 'feet', 'lvl': 1, 'price': 5, 'armor': 0.5, 'tt': 'Overpriced plastics thongs. what\'s plastic anyway ?'},
    'Gomina': {'type': 'head', 'lvl': 1, 'price': 15, 'armor': 0.5, 'tt': 'From a distance, it almost looks like you\'re wearing an helmet'},
    'Potato sac': {'type': 'torso', 'lvl': 1, 'price': 20, 'armor': 1, 'tt': 'Better than nothing I suppose.'},
    'Bandana': {'type': 'head', 'lvl': 1, 'price': 50, 'armor': 1, 'tt': 'Fashionnable piece of cloth with a pearsley pattern printed on it, thin but good looking'},
    'Dragonforce T-shirt': {'type': 'torso', 'lvl': 1, 'price': 65, 'armor': 1.7, 'tt': 'Nothing is more medieval than a Dragonforce T-shirt.'},
    'Club': {'type': 'weapon', 'subtype': 'mace', 'lvl': 1, 'price': 75, 'damage': 1, 'speed': 1.1, 'tt': 'A solid piece of oak wood'},
    'Worn Shoes': {'type': 'feet', 'lvl': 1, 'price': 95, 'armor': 1.2, 'tt': 'They smell like bad cheese but they provide some protection'},
    'Dagger': {'type': 'weapon', 'subtype': 'sword', 'lvl': 2, 'price': 260, 'damage': 1.2, 'speed': 1.5, 'tt': 'A quick and deadly weapon, if you can get close enough'},
    'Cap': {'type': 'head', 'lvl': 2, 'price': 285, 'armor': 2, 'tt': 'A strange hat with the runes NY inscribed on it, this has to be a powerful ancient artifact'},
    'Cloth Tunic': {'type': 'torso', 'lvl': 2, 'price': 300, 'armor': 2.5, 'tt': 'Pink was not your first choice but they didn¨\'t have your size in crimson red anymore'},
    'Buckler': {'type': 'offhand', 'lvl': 1, 'price': 310, 'armor': 1.5, 'tt': 'It\'s mostly just a piece of wood with a handle on the back'},
    'Leather Boots': {'type': 'feet', 'lvl': 2, 'price': 315, 'armor': 1.8, 'tt': 'Shiny, shiny, shiny boots of leather'},
    'Hand Axe': {'type': 'weapon', 'subtype': 'axe', 'lvl': 2, 'price': 450, 'damage': 2.2, 'speed': 1.1, 'tt': 'As long as you\'re combatting logs, you\'ll be fine'},
    'Rusted Greaves': {'type': 'feet', 'lvl': 2, 'price': 500, 'armor': 2.3, 'tt': 'Don\'t forget to oil them or the squeal is gonna drive you mad'},
    'Leather Doublet': {'type': 'torso', 'lvl': 2, 'price': 570, 'armor': 3.4, 'tt': 'Let\'s just hope they won\'t target your arms'},
    'Leather Hood': {'type': 'head', 'lvl': 2, 'price': 600, 'armor': 2.7, 'tt': 'It did come with an orange ball to protect your mouth, but it\'s not really practical'},
    'Short Sword': {'type': 'weapon', 'subtype': 'sword', 'lvl': 3, 'price': 1070, 'damage': 2.7, 'speed': 1.4, 'tt': 'A fine steel weapon'},
    'Coif': {'type': 'head', 'lvl': 3, 'price': 1250, 'armor': 3.5, 'tt': 'How do you even pronounce that ?'},
    'Brigandine Coat': {'type': 'torso', 'lvl': 3, 'price': 1450, 'armor': 4.5, 'tt': 'You\'re looking swell ! what\'s that smell ?'},
    'Morning Star': {'type': 'weapon', 'subtype': 'mace', 'lvl': 3, 'price': 1970, 'damage': 4.2, 'speed': 1.2, 'tt': 'For the early bird'},
    'Targe Shield': {'type': 'offhand', 'lvl': 3, 'price': 2130, 'armor': 3, 'tt': 'Don\'t get a splinter'},
    'Flail': {'type': 'weapon', 'subtype': 'flail', 'lvl': 4, 'price': 2700, 'damage': 5, 'speed': 1.3, 'tt': 'Careful now, don\'t hurt yourself'},
    'Sabatons': {'type': 'feet', 'lvl': 4, 'price': 3150, 'armor': 4.2, 'tt': 'You might get some blisters, but you ain\'t gonna lose your feets'},
    'Used Chain Mail': {'type': 'torso', 'lvl': 4, 'price': 3500, 'armor': 6, 'tt': 'The smell strongly suggests that the previous owner was an Orc'},

    
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
