class Resource(object):

    def __init__(self, request):
        self.request = request

    LOOKUP = None

    def __getitem__(self, name):
        if self.LOOKUP is None:
            raise KeyError(name)
        return self.LOOKUP[name](self.request)


class ApiRoot(Resource):

    pass


class Root(Resource):

    LOOKUP = {
        "api": ApiRoot,
    }
