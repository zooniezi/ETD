import pygame as pg
import math





class Tower:
    def __init__(self,x,y,elt):
        self.damage = elt.damage # 원소랑 상호작용
        self.atkspeed = elt.attackspeed # 원소랑 상호작용
        self.towx = x
        self.towy = y
        self.has_elt = False
        self.range_in = False

    def attack(self):
        if self.haselt == True and self.rangein == True:
            pass
    

    def add_elt(self):
        pass #이미 원소가 있는 경우 원소의 레벨이 업


    def is_range_in(self):
        # a,b = mobposition 몬스터 위치를 받아야할듯
        # if math.sqrt((a-self.towx)^2 + (b-self.towy)^2) <= 3: 

            self.rangein = True
        



    def reset(self):
        pass



class element:
    def __init__(self,dmg,ats,atr,price,lv,dote,kb,sp,sw,rt,st,ec):
        self.equipped = False
        self.damage = dmg
        self.attackspeed = ats
        self.attackrange = atr
        self.price = price
        self.level = lv
        self.dote = dote
        self.knock_back = kb
        self.splash = sp
        self.slow = sw
        self.root = rt
        self.stun = st
        self.enchant = ec


    def sell_element(self):
        pass
    
    def compose_element(self):
        pass


    def with_slow(self):
        pass

    def with_dote(self):
        if self.dote == True:
            mob_hp -= 1


    def with_Knock_back(self):
        pass

    def with_splash(self):
        pass

    def with_root(self):
        pass
    
    def with_stun(self):
        pass

    def with_enchant(self):
        pass
