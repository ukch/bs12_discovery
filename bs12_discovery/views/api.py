from functools import partial

from pyramid.view import view_config

from bs12_discovery.resource import ApiRoot

view_config = partial(view_config, renderer="json")

@view_config(context=ApiRoot)
def main(request):
    return {}
