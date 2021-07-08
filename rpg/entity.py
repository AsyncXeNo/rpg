from utils.logger import Logger


class Entity(object):
    validstatuses = ["NORMAL", "STUNNED"]

    def __init__(self, maxhp:int, strength:int, mp:int, armor:int, mr:int, agility:float, status:list):
        self.logger = Logger("rpg/entity")

        self.maxhp = maxhp
        self.hp = maxhp
        self.str = strength
        self.mp = mp
        self.armor = armor
        self.mr = mr
        self.agility = agility
        self.status = status
        
        self.validate()

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

        for status in self.status:
            if not (status in Entity.validstatuses):
                self.logger.log_error(f"{status} is not a valid status.")
                raise Exception(f"{status} is not a valid status.")

    #stats

    def get_maxhp(self):
        pass

    def give_maxhp(self, maxhp):
        pass

    def get_str(self):
        pass

    def give_str(self, str):
        pass

    def get_mp(self):
        pass

    def give_mp(self, mr):
        pass

    def get_armor(self):
        pass

    def give_armor(self, armor):
        pass

    def get_mr(self):
        pass

    def give_mr(self, mr):
        pass

    def get_agility(self):
        pass

    def give_agility(self, agility):
        pass

    def get_status(self):
        pass

    def give_status(self, status):
        pass

    def remove_status(self, status):
        pass


    # hp

    def get_hp(self):
        pass

    def give_hp(self):
        pass

    def deal_physical(self):
        pass

    def deal_magical(self):
        pass