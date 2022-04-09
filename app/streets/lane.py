class Lane:
    def __init__(self, junction_ahead, direction):
        self.junction_ahead = junction_ahead
        self.direction = direction

        self.entities = set()
        self.first_entity = None
        self.last_entity = None

    def add_entity(self, entity):
        self.entities.add(entity)

        if self.first_entity is None:
            self.first_entity = entity

        entity.preceding = self.last_entity
        if self.last_entity is not None:
            self.last_entity.following = entity

        self.last_entity = entity

    def update(self):
        for entity in self.entities:
            if entity.preceding is None:
                close_entities = []
            else:
                close_entities = [entity.preceding]

            entity.update(close_entities, self.junction_ahead)

        if self.first_entity is not None and self.junction_ahead is not None \
                and self.junction_ahead.is_car_on_junction(self.first_entity.entity):
            if self.first_entity.following is not None:
                self.first_entity.following.preceding = None

                new_first_entity = self.first_entity.following
                self.first_entity.following = None

                self.junction_ahead.add_entity(self.first_entity)
                self.entities.remove(self.first_entity)
                self.first_entity = new_first_entity
            else:
                self.junction_ahead.add_entity(self.first_entity)
                self.entities.remove(self.first_entity)
                self.first_entity = None


    def blit(self):
        for entity in self.entities:
            entity.blit()
