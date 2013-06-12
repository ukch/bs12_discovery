def _add(obj, name, parent):
    obj.__name__ = name
    obj.__parent__ = parent
    return obj


class Resource(object):

    def __init__(self, request):
        self.request = request

    LOOKUP = None

    def __getitem__(self, name):
        if self.LOOKUP is None:
            raise KeyError(name)
        return _add(self.LOOKUP[name](self.request), name, self)


class ApiServiceList(Resource):

    pass


class ApiServerList(Resource):

    pass


class ApiRoot(Resource):

    LOOKUP = {
        "services": ApiServiceList,
        "servers": ApiServerList,
    }


class Root(Resource):

    __name__ = None

    LOOKUP = {
        "api": ApiRoot,
    }
