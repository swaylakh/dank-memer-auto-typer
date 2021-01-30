import select
import sys
import time
import random
import cooldowns as cd
import pynput
from pynput.keyboard import Key, Controller
import config
keyboard = Controller()
pmtypes = ["f", "r", "i", "c", "k"]


def type_send(msg):
    keyboard.type(str(msg))
    time.sleep(2)
    keyboard.press(Key.enter)

def print_buyj(scheduler):
    type_send("pls buy j")
    scheduler.run_after(print_buyj, cd.buy_cooldown)

def print_j(scheduler):
    type_send("pls use j")
    time.sleep(random.randint(cd.plsusej_cooldown, cd.plsusej_cooldown+5))
    type_send(config.send_id)
    time.sleep(random.randint(cd.sendtoid_cooldown,cd.sendtoid_cooldown+ 5))
    type_send("1")
    time.sleep(random.randint(cd.sendjAnswer_cooldown, cd.sendjAnswer_cooldown+5))
    scheduler.run_after(print_j, cd.use_cooldown)

def print_beg(scheduler):
    type_send("pls beg")
    scheduler.run_after(print_beg, cd.beg_cooldown)

def print_hunt(scheduler):
    type_send("pls hunt")
    scheduler.run_after(print_hunt, cd.hunt_cooldown)

def print_fish(scheduler):
    type_send("pls fish")
    scheduler.run_after(print_fish, cd.fish_cooldown)

def print_pm(scheduler):
    type_send("pls pm")
    time.sleep(random.randint(cd.pmAnswer_cooldown, cd.pmAnswer_cooldown+5))
    type_send(random.choice(pmtypes))
    scheduler.run_after(print_pm, cd.pm_cooldown)

def print_bet(scheduler):
    msg= "pls bet " + str(config.bet_amount)
    type_send(msg)
    scheduler.run_after(print_bet, cd.bet_cooldown)

def print_slots(scheduler):
    msg= "pls slots " + str(config.slots_amount)
    type_send(msg)
    scheduler.run_after(print_slots, cd.slots_cooldown)

def print_hl(scheduler):
    type_send("pls hl")
    time.sleep(random.randint(cd.hlAnswer_cooldown, cd.hlAnswer_cooldown+5))
    type_send(config.hl_answer)
    scheduler.run_after(print_hl, cd.hl_cooldown)

class Scheduler:
    def __init__(self):
        self.ready = []
        self.waiting = []

    def run_soon(self, task):
        self.waiting.append((task, 0))

    def run_after(self, task, delay):
        self.waiting.append((task, time.time() + delay))

    def run_until_complete(self):
        while self.ready or self.waiting:
            while self.ready:
                self.ready.pop()(self)
                time.sleep(random.randint(3,7))
            for i in range(len(self.waiting) - 1, -1, -1):
                task, start_after = self.waiting[i]
                if start_after < time.time():
                    self.ready.append(task)
                    del self.waiting[i]

s = Scheduler()
time.sleep(5) #activate your window where you need to type within 5 sec
if config.beg:
    s.run_soon(print_beg)
if config.pink:
    s.run_soon(print_j)
if config.buyj:
    s.run_soon(print_buyj)
if config.hunt:
    s.run_soon(print_hunt)
if config.fish:
    s.run_soon(print_fish)
if config.pm:
    s.run_soon(print_pm)
if config.bet:
    s.run_soon(print_bet)
if config.slots:
    s.run_soon(print_slots)
if config.hl:
    s.run_soon(print_hl)
s.run_until_complete()