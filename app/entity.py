class Entity:
    def __init__(self, entity, preceding=None, following=None):
        self.entity = entity

        self.preceding = preceding
        self.following = following

    def update(self, entities, junction_ahead):
        self.entity.update(list(map(lambda e: e.entity, entities)), junction_ahead)

    def maybe_turn(self, junction):
        self.entity.maybe_turn(junction)

    def turn_on_next_junction(self):
        self.entity.turn_on_next_junction()

    def blit(self):
        self.entity.blit()
