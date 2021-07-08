from utils.logger import Logger
from rpg.entity import Entity


class Player(Entity):
    def __init__(self, player_id:str, name:str, maxhp:int, strength:int, mp:int, armor:int, mr:int, agility:float, statuses:list, state:str):
        self.logger = Logger("rpg/players/player")
        
        self.logger.log_neutral(f"Creating a player named {name} with id {player_id}.")
        self.id = player_id
        self.name = name
        
        Entity.__init__(maxhp, strength, mp, armor, mr, agility, statuses, state)

        self.in_party = False
        self.party_id = None


    # info

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.logger.log_neutral("Changed name of player with id {self.id} from {self.name} to {name}.")
        self.name = name

    def get_id(self):
        return self.id

    
    # party

    def get_party(self, party_id):
        return party_id

    def in_party(self):
        return self.in_party

    def add_to_party(self, party_id):
        self.in_party = True
        self.party_id = party_id

    def remove_from_party(self, party_id):
        if not (self.party_id == party_id):
            self.logger.log_error(f"Attempt to remove player from a party they don't belong to.")
            raise Exception(f"Attempt to remove player from a party they don't belong to.")
        self.in_party = False
        self.party_id = None