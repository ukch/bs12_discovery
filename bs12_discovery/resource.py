from bs12_discovery.models import DBSession, Service, Server


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


class ModelFinderResource(Resource):

    # FIXME this class probably needs rewriting

    MODEL = None
    MODEL_ACCESSOR = "name"
    CHILD_RESOURCE = Server

    def _getitem__(self, name):
        try:
            return super(ModelFinderResource, self).__getitem__(name)
        except KeyError:
            if self.MODEL is None:
                raise
            obj = DBSession.query(self.MODEL).get(
                **{self.MODEL_ACCESSOR: name})
            return _add(self.CHILD(self.request, obj), name, self)


class ApiServiceList(ModelFinderResource):

    MODEL = Service


class ApiServerList(ModelFinderResource):

    MODEL = Server


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
