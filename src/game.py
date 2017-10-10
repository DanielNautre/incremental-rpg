#!/usr/bin/python3.6
# -*- coding: utf8 -*

from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QHBoxLayout, QWidget

from widgets import InfoWidget, ProgressionWidget, BuyGearWidget, BuySkillsWidget, EquippedGearWidget


class _GameVar(object):

    ''' Helper class to store game variables'''

    def __init__(self):
        super(_GameVar, self).__init__()

        self.timestamp = 0
        self.xp = 0
        self.lvl = 1
        self.gold = 0
        self.skill_points = 0

        self.weapon = {'name': 'Hands', 'type': 'hands', 'damage': 0.1, 'speed': 0, 'tt': 'Just your bare hands'}
        self.head = {'name': 'Hair', 'armor': 0.1, 'tt': 'Long hair does provides some protection against direct hits and it soaks some of the blood up to reduce the mess'}
        self.torso = {'name': 'Manly chesthair', 'armor': 0.1, 'tt': 'Your mane is sure to blunt your foes swords'}
        self.feet = {'name': 'Feet', 'armor': 0.0, 'tt': 'Careful, don\'t walk on Lego'}
        self.offhand = None

        self.has_bought_gear = False
        self.has_leveled = False
        self.has_bought_skill = False

        self.skills = {}

    def xp_per_tick(self):
        return 1 * self.dps() * self.xp_boost() * self.armor()

    def gold_per_tick(self):
        return 0.5 * self.dps() * self.gold_boost() * self.armor()

    def tick(self):
        self.timestamp += 1
        self.xp += self.xp_per_tick()
        self.gold += self.gold_per_tick()

    def next_lvl(self):
        return int(((self.lvl + 1) ** 5) * 25)

    def lvl_up(self):
        self.xp = self.xp - self.next_lvl()
        self.lvl += 1
        self.has_leveled = True
        self.skill_points += 1

    def dps(self):
        # calculate damage bonus based on skills
        base_dps = self.weapon['damage'] * self.weapon['speed']
        dps = base_dps

        if 'Strength' in self.skills:
            dps += base_dps * (self.skills['Strength']['value'] / 100)
        if 'Fiery Weapon' in self.skills:
            dps += base_dps * (self.skills['Fiery Weapon']['value'] / 100)

        return dps

    def raw_armor(self):
        base_armor = self.head['armor'] + self.torso['armor'] + self.feet['armor']
        if self.offhand:
            base_armor += self.offhand['armor']

        return base_armor


    def armor(self):

        base_armor = self.raw_armor()
        armor = base_armor

        if 'Dexterity' in self.skills:
            armor += base_armor * (self.skills['Dexterity']['value'] / 100)
        if 'Mana Shield' in self.skills:
            armor += base_armor * (self.skills['Mana Shield']['value'] / 100)

        return armor

    def xp_boost(self):
        xp_boost = 1

        if 'Intelligence' in self.skills:
            xp_boost += 1 * (self.skills['Intelligence']['value'] / 100)

        return xp_boost

    def gold_boost(self):
        gold_boost = 1
        for skill in self.skills:
            if 'gold_boost' in skill:
                gold_boost *= skill['gold_boost']
        return gold_boost


class Game(object):

    def __init__(self, window):
        super(Game, self).__init__()
        self.w = window

        self.init_game()
        self.init_UI()

    def init_game(self):

        self.var = _GameVar()

    def init_UI(self):

        central_widget = QWidget()

        vbox = QVBoxLayout()
        char_hbox = QHBoxLayout()
        char_vbox = QVBoxLayout()

        self.progress_widget = ProgressionWidget()
        self.buy_skills_widget = BuySkillsWidget()
        self.buy_gear_widget = BuyGearWidget()
        self.equipped_gear_widget = EquippedGearWidget()
        self.info_widget = InfoWidget()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.buy_gear_widget, "Gear")
        self.tabs.addTab(self.buy_skills_widget, "Skills")

        char_vbox.addWidget(self.equipped_gear_widget)
        char_vbox.addWidget(self.info_widget)
        char_vbox.addStretch()


        char_hbox.addLayout(char_vbox)
        char_hbox.addWidget(self.tabs)

        vbox.addWidget(self.progress_widget)
        vbox.addLayout(char_hbox)

        central_widget.setLayout(vbox)
        self.w.setCentralWidget(central_widget)

        # first update
        self.buy_gear_widget.populate(self.var)
        self.buy_skills_widget.populate(self.var)
        self.progress_widget.update(self.var)
        self.equipped_gear_widget.update(self.var)

    def run_loop(self):
        # update action
        self.progress_widget.update_action(self.var)
        # progress
        self.var.tick()
        # lvl up
        if self.var.xp >= self.var.next_lvl():
            self.var.lvl_up()

    def refresh_interface(self):
        if self.var.has_leveled:
            # refresh available gear
            self.var.has_leveled = False
            self.buy_gear_widget.populate(self.var)
            self.buy_skills_widget.populate(self.var)

        if self.var.has_bought_gear:
            # refresh available gear, current equipped
            self.var.has_bought_gear = False
            self.buy_gear_widget.populate(self.var)
            self.equipped_gear_widget.update(self.var)

        if self.var.has_bought_skill:
            # Refresh after buying a skill point
            self.var.has_bought_skill = False
            self.buy_skills_widget.populate(self.var)

        self.progress_widget.update(self.var)
        self.info_widget.update(self.var)
