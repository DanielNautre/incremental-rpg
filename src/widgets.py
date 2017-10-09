#!/usr/bin/python3.6
# -*- coding: utf8 -*

from PyQt5.QtWidgets import (
    QWidget, QFormLayout, QLabel, QProgressBar, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton)

from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt

from gear import get_available_gear, remove_gear
from skills import get_available_skills


def s_to_string(s):
    if s > 31535999:
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)
        return f'{y} years, {d} days, {h} hours, {m} minutes and {s} seconds'
    if s > 86399:
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        return f'{d} days, {h} hours, {m} minutes and {s} seconds'
    if s > 3599:
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return f'{h} hours, {m} minutes and {s} seconds'
    if s > 59:
        m, s = divmod(s, 60)
        return f'{m} minutes and {s} seconds'

    return f'{s} seconds'


class InfoWidget(QWidget):

    def __init__(self):
        super(InfoWidget, self).__init__()

        fbox = QFormLayout()
        fbox.setHorizontalSpacing(25)

        self.lbl_lvl = QLabel('0')
        self.lbl_xp = QLabel('0')
        self.lbl_gold = QLabel('0')
        self.lbl_dps = QLabel('0')
        self.lbl_armor = QLabel('0')

        lbl_lvl_name = QLabel('Level:')
        lbl_xp_name = QLabel('XP:')
        lbl_gold_name = QLabel('Gold:')
        lbl_dps_name = QLabel('DPS:')
        lbl_armor_name = QLabel('Armor:')

        fbox.addRow(lbl_lvl_name, self.lbl_lvl)
        fbox.addRow(lbl_xp_name, self.lbl_xp)
        fbox.addRow(lbl_gold_name, self.lbl_gold)
        fbox.addRow(lbl_dps_name, self.lbl_dps)
        fbox.addRow(lbl_armor_name, self.lbl_armor)

        self.setLayout(fbox)

    def update(self, var):
        self.lbl_lvl.setText(str(var.lvl))
        if var.xp_per_tick() > 0:
            s_to_level = int((var.next_lvl() - var.xp) / var.xp_per_tick())
            time_to_lvl = s_to_string(s_to_level)
        else:
            time_to_lvl = '∞'
        self.lbl_lvl.setToolTip('Next level in ≈ {}'.format(time_to_lvl))

        self.lbl_xp.setText('{:g}/{:g}'.format(var.xp, var.next_lvl()))
        self.lbl_xp.setToolTip('{:g} xp/s'.format(var.xp_per_tick()))

        self.lbl_gold.setText('{:g}'.format(var.gold))
        self.lbl_gold.setToolTip('{:g} gold/s'.format(var.gold_per_tick()))

        self.lbl_dps.setText('{:g}'.format(var.dps()))
        self.lbl_armor.setText('{:g}'.format(var.armor()))
        self.lbl_armor.setToolTip('Raw value: {:g}'.format(var.raw_armor()))


class ProgressionWidget(QWidget):

    def __init__(self):
        super(ProgressionWidget, self).__init__()

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.bar_xp = QProgressBar()
        self.bar_xp.setMinimum(0)
        self.bar_xp.setMaximum(1)
        self.bar_xp.setValue(0)
        self.bar_xp.setFormat('Experience: {xp:.1f}'.format(xp=0))
        self.bar_xp.setStyleSheet("::chunk {background-color: yellow}")

        self.lbl_lvl = QLabel('0')
        self.lbl_lvl.setFont(QFont('Helvetica', 18))

        self.lbl_skills_points = QLabel('')
        self.lbl_skills_points.setFont(QFont('Helvetica', 18))

        self.lbl_gold = QLabel('Gold: {gold}'.format(gold=0))

        hbox.addWidget(self.lbl_lvl)
        hbox.addWidget(self.bar_xp)
        hbox.addWidget(self.lbl_skills_points)

        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl_gold)

        self.setLayout(vbox)

    def update(self, var):
        self.bar_xp.setMaximum(var.next_lvl())
        self.bar_xp.setValue(var.xp)
        self.bar_xp.setFormat('Experience: {xp:.1f}'.format(xp=var.xp))

        self.lbl_lvl.setText(str(var.lvl))
        if var.skill_points > 0:
            points = var.skill_points
            self.lbl_skills_points.setText('+')
            self.lbl_skills_points.setToolTip(f'{points} skill points available')
        else:
            self.lbl_skills_points.setText('')
            self.lbl_skills_points.setToolTip('')

        self.lbl_gold.setText('Gold: {gold:.1f}'.format(gold=var.gold))


class EquippedGearWidget(QWidget):

    def __init__(self):
        super(EquippedGearWidget, self).__init__()

        form = QFormLayout()
        form.setHorizontalSpacing(25)

        self.lbl_weapon = QLabel('')
        lbl_weapon_name = QLabel('Weapon:')
        lbl_weapon_name.setFont(QFont('Helvetica', 12))

        self.lbl_torso = QLabel('')
        lbl_torso_name = QLabel('Torso:')
        lbl_torso_name.setFont(QFont('Helvetica', 12))

        self.lbl_head = QLabel('')
        lbl_head_name = QLabel('Head:')
        lbl_head_name.setFont(QFont('Helvetica', 12))

        self.lbl_feet = QLabel('')
        lbl_feet_name = QLabel('Feet:')
        lbl_feet_name.setFont(QFont('Helvetica', 12))

        self.lbl_offhand = QLabel('')
        lbl_offhand_name = QLabel('Offhand:')
        lbl_offhand_name.setFont(QFont('Helvetica', 12))

        form.addRow(lbl_weapon_name, self.lbl_weapon)
        form.addRow(lbl_head_name, self.lbl_head)
        form.addRow(lbl_torso_name, self.lbl_torso)
        form.addRow(lbl_feet_name, self.lbl_feet)
        form.addRow(lbl_offhand_name, self.lbl_offhand)


        self.setLayout(form)

    def update(self, var):
        self.lbl_weapon.setText(var.weapon['name'])
        self.lbl_weapon.setToolTip(self.tt(var.weapon))

        self.lbl_torso.setText(var.torso['name'])
        self.lbl_torso.setToolTip(self.tt(var.torso))

        self.lbl_head.setText(var.head['name'])
        self.lbl_head.setToolTip(self.tt(var.head))

        self.lbl_feet.setText(var.feet['name'])
        self.lbl_feet.setToolTip(self.tt(var.feet))

        if var.offhand:
            self.lbl_offhand.setText(var.offhand['name'])
            self.lbl_offhand.setToolTip(self.tt(var.offhand))
        else:
            self.lbl_offhand.setText('')
            self.lbl_offhand.setToolTip('')

    def tt(self, gear):
        text = ''
        if 'damage' in gear:
            value = gear['damage'] * gear['speed']
        elif 'armor' in gear:
            value = gear['armor']

        name = gear['name']
        tt = gear['tt']
        text = f'<h3>{name}</h3><h2>{value:.3g}</h2><em>{tt}</em>'

        return text


class BuyGearWidget(QWidget):

    def __init__(self):
        super(BuyGearWidget, self).__init__()

        self.grid = QGridLayout()

        vbox = QVBoxLayout()
        vbox.addLayout(self.grid)
        vbox.addStretch()

        self.setLayout(vbox)

    def populate(self, var):

        while self.grid.count():
            child = self.grid.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        gear = get_available_gear(var.lvl)

        x, y = (0, 0)

        for name, g in gear.items():
            self.grid.addWidget(GearButtonWidget(name, g, var), y, x)
            self.grid.setAlignment(Qt.AlignLeft)
            x += 1
            if x == 5:
                y += 1
                x = 0


class GearButtonWidget(QWidget):

    def __init__(self, name, gear, var):
        super(GearButtonWidget, self).__init__()

        self.name = name
        self.var = var
        self.gear = gear

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        lbl_name = QLabel(self.name)
        lbl_name.setFont(QFont('Helvetica', 13))
        lbl_name.setWordWrap(True)

        buy_btn = QPushButton('buy ({price})'.format(price=self.gear['price']), self)
        buy_btn.pressed.connect(self.buy)

        self.setToolTip(self.tt())

        # hbox.addStretch()
        hbox.addWidget(buy_btn)
        # hbox.addStretch()

        vbox.addWidget(lbl_name)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setMaximumWidth(128)
        self.setMinimumWidth(128)
        self.setMinimumHeight(128)
        self.setMaximumHeight(128)

    def tt(self):
        text = ''
        if 'damage' in self.gear:
            value = self.gear['damage'] * self.gear['speed']
        elif 'armor' in self.gear:
            value = self.gear['armor']

        name = self.name
        tt = self.gear['tt']
        text = f"<h3>{name}</h3><h2>{value:.3g}</h2><em>{tt}</em>"

        return text

    def buy(self):

        if self.var.gold < self.gear['price']:
            return

        self.var.gold -= self.gear['price']
        remove_gear(self.name)

        if 'damage' in self.gear:
            g = {'name': self.name, 'damage': self.gear['damage'], 'speed': self.gear['speed'], 'tt': self.gear['tt']}
            self.var.weapon = g.copy()

            # remove offhand item if weapon is two handed
            if '2h' in self.gear['subtype']:
                self.var.offhand = None

        else:
            g = {'name': self.name, 'armor': self.gear['armor'], 'tt': self.gear['tt']}

            if self.gear['type'] == 'feet':
                self.var.feet = g.copy()
            elif self.gear['type'] == 'head':
                self.var.head = g.copy()
            elif self.gear['type'] == 'torso':
                self.var.torso = g.copy()
            elif self.gear['type'] == 'offhand':
                self.var.offhand = g.copy()

        self.var.has_bought_gear = True


class BuySkillsWidget(QWidget):

    def __init__(self):
        super(BuySkillsWidget, self).__init__()

        self.grid = QGridLayout()
        vbox = QVBoxLayout()
        vbox.addLayout(self.grid)
        vbox.addStretch()

        self.setLayout(vbox)

    def populate(self, var):

        while self.grid.count():
            child = self.grid.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        skills = get_available_skills(var.lvl)

        x, y = (0, 0)

        for name, s in skills.items():
            self.grid.addWidget(SkillItemWidget(name, s, var), y, x)
            self.grid.setAlignment(Qt.AlignLeft)
            x += 1
            if x == 6:
                y += 1
                x = 0


class SkillItemWidget(QWidget):

    def __init__(self, name, skill, var):
        super(SkillItemWidget, self).__init__()

        self.name = name
        self.skill = skill
        self.var = var

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        lbl_name = QLabel(self.name)
        lbl_name.setFont(QFont('Helvetica', 13))


        if self.name in self.var.skills:
            current_level = self.var.skills[self.name]['lvl']
            skill_next_lvl = (current_level * self.skill['lvl_step']) + self.skill['lvl']
            desc = self.skill['desc'].format(value=self.var.skills[self.name]['value'])
            tt = self.skill['tt']
            text = f'<p>{desc}</p><p><i>{tt}</i></p>'
        else:
            current_level = 0
            skill_next_lvl = self.skill['lvl']
            text = 'You do not have that skill yet'

        lbl_lvl = QLabel(str(current_level))
        lbl_lvl.setFont(QFont('Helvetica', 18))

        hbox.addWidget(lbl_lvl)
        if self.var.skill_points > 0 and self.var.lvl >= skill_next_lvl:
            btn_add = QPushButton('+', self)
            btn_add.pressed.connect(self.buy)
            hbox.addWidget(btn_add)

        vbox.addWidget(lbl_name)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setToolTip(text)

    def buy(self):
        if self.var.skill_points < 1:
            return

        self.var.skill_points -= 1
        self.var.has_bought_skill = True

        if self.name in self.var.skills:
            # increase skill level
            self.var.skills[self.name]['lvl'] += 1
            self.var.skills[self.name]['value'] += self.skill['step']

        else:
            # add skill
            self.var.skills[self.name] = {'lvl': 1, 'value': self.skill['step']}
