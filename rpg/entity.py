from utils.logger import Logger
from rpg.ability import Ability


class Entity(object):
    validstatuses = ["STUNNED"]
    validstates = ["NORMAL", "MADDENED", "RELAXED"]

    def __init__(self, maxhp:int, strength:int, mp:int, armor:int, mr:int, agility:float, statuses:list, state:str):
        self.logger = Logger("rpg/entity")

        self.logger.log("Creating an entity.")
        self.maxhp = maxhp
        self.hp = maxhp
        self.str = strength
        self.mp = mp
        self.armor = armor
        self.mr = mr
        self.agility = agility
        self.statuses = statuses
        self.state = state

        self.validate()
        
        self.abilities = []

    def validate(self):
        if self.agility < 0 or self.agility > 1:
            self.logger.log_error("Agility cannot be outside range 0-1.")
            raise Exception("Agility outside range 0-1.")

        if self.maxhp < 1:
            self.logger.log_error("Max HP cannot be lower than 1.")
            raise Exception("Max HP cannot be lower than 1.")

        if self.str < 0:
            self.logger.log_error("Strengh cannot be lower than 0.")
            raise Exception("Strengh cannot be lower than 0.")

        if self.mp < 0:
            self.logger.log_error("MP cannot be lower than 0.")
            raise Exception("MP cannot be lower than 0.")

        if not (self.state in Entity.validstatuses):
            self.logger.log_error(f"{self.state} is not a valid state.")
            raise Exception(f"{self.state} is not a valid state.")

        for status in self.status:
            if not (status in Entity.validstatuses):
                self.logger.log_error(f"{status} is not a valid status.")
                raise Exception(f"{status} is not a valid status.")

    #stats

    def get_maxhp(self):
        pass

    def give_maxhp(self, maxhp:int):
        pass

    def get_str(self):
        pass

    def give_str(self, str:int):
        pass

    def get_mp(self):
        pass

    def give_mp(self, mr:int):
        pass

    def get_armor(self):
        pass

    def give_armor(self, armor:int):
        pass

    def get_mr(self):
        pass

    def give_mr(self, mr:int):
        pass

    def get_agility(self):
        pass

    def give_agility(self, agility:float):
        pass

    def get_statuses(self):
        pass

    def give_status(self, status:str):
        pass

    def remove_status(self, status:str):
        pass


    # hp

    def get_hp(self):
        pass

    def give_hp(self, hp:int):
        pass

    def deal_physical(self, strength:int):
        pass

    def deal_magical(self, mp:int):
        pass

    
    # abilities

    def get_abilities(self):
        return self.abilities

    def get_usable_abilities(self):
        pass

    def give_ability(self, ability:Ability):
        pass

    def take_ability(self, ability_id:str):
        pass


    # death

    def death(self):
        # if self.hp > 0:
        #     self.logger.log_error(f"Player with id {self.id} is not dead yet. They still have {self.hp} HP.")
        #     raise Exception(f"Player with id {self.id} is not dead yet. They still have {self.hp} HP.")
        pass