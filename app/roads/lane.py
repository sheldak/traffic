class Lane:
    def __init__(self, direction):
        self.direction = direction
        self.entities = set()
        self.last_entity = None

    def add_entity(self, entity):
        self.entities.add(entity)

        entity.preceding = self.last_entity
        if self.last_entity is not None:
            self.last_entity.following = entity

        self.last_entity = entity

    def close_entities(self, entity):
        if entity.preceding is None:
            return []
        else:
            return [entity.preceding]
