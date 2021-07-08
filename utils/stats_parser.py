
class StatsParser(object):
    @staticmethod
    def parse(stats):
        maxhp = stats["maxhp"]
        strength = stats["damage"]["physcial"]
        mp = stats["damage"]["magical"]
        