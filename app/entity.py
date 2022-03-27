class Entity:
    def __init__(self, entity, lane, preceding=None, following=None):
        self.entity = entity
        self.lane = lane

        self.preceding = preceding
        self.following = following

