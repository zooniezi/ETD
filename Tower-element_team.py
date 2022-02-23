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
        
    # def set_tower(self):
        #랜덤으로 좌표를 받아서 
        # pass
       

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

    # ----------원소 행동---------------
    def sell_element(self):
        # gain_gold = self.price
        # total_gold += self.price
        # 원소가 없어지는 메소드
        pass
    def buy_element(self):
        # total_gold -= self.price
        # 상점에서 원소를 없애고 인벤토리로 추가해라
        pass

    def generate_element(self):
        #inventory.append(dictionry.[원소번호-1])
        #백과사전은 만들예정
        pass


    def compose_element(self):
        pass
        #인벤토리에서 합칠수도 있고 타워에서도 합칠 수 있다
        #[tower]리스트 안에 원소가 있으면 그 원소는 없애고 새로운 원소를 만들어라. 
        #인벤토리로 추가하는 함수
        

    def delete_element(self):
        pass
        #del(inventory)로 리스트를 받아서 없애기 아래에 예시?
        #인벤토리 = [원소] 안에 원소를 없앤다.
        #타워 = [원소]


    # ---------원소 성질------------
    def with_slow(self):
        pass

    def with_dote(self):
        # if self.dote == True: 몇초동안 몇 대미지 넣을지 디테일 필요
        # mop_hp -= 1
        pass

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
