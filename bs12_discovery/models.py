class DBAPIError(Exception):
    pass


class MockCollection(object):

    def __init__(self, model):
        self.model = model

    def all(self):
        return frozenset(self.model.make_dummy_objects())

    def get(self, **kwargs):
        objs = self.model.make_dummy_objects()
        for key, value in kwargs.iteritems():
            new_objs = []
            for obj in objs:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    new_objs.append(obj)
            objs = new_objs
        if len(objs) != 1:
            raise KeyError("{} found for query".len(objs))
        return objs[0]


class DBSession(object):
    """Dummy DB session"""
    @classmethod
    def query(cls, model):
        return MockCollection(model)


# Models
class Service(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        # TODO: add image and recommended apps

    @classmethod
    def make_dummy_objects(cls):
        return [
            Service("Battleships", "This is a cool game"),
            Service("Sabacc", "This is a cooler game"),
        ]


class Server(object):

    # TODO: add name, desc, URI, #games
    pass
