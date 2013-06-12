from functools import partial

from pyramid.view import view_config

from bs12_discovery.resource import ApiRoot, ApiServiceList, ApiServerList

view_config = partial(view_config, renderer="json")

@view_config(context=ApiRoot)
def main(context, request):
    return {
        "services": request.resource_url(context["services"]),
        "servers": request.resource_url(context["servers"]),
    }

@view_config(context=ApiServiceList)
def service_list(context, request):
    return {}

@view_config(context=ApiServerList)
def server_list(context, request):
    return {}
