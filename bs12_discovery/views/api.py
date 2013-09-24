from functools import partial

from pyramid.view import view_config

from bs12_discovery.resource import (
        ApiRoot,
        ApiServiceList,
#        ApiService,
        ApiServerList,
)
from bs12_discovery.models import DBAPIError, DBSession, Service

view_config = partial(view_config, renderer="json")


@view_config(context=ApiRoot)
def main(context, request):
    return {
        "services": request.resource_url(context["services"]),
        "servers": request.resource_url(context["servers"]),
    }


@view_config(context=ApiServiceList)
def service_list(context, request):
    try:
        services = DBSession.query(Service).all()
    except DBAPIError:
        request.response.status_code = 500
        return "an error occurred"
    return [{
        "name": service.name,
        "description": service.description,
        "url": None,  # FIXME
    } for service in services]


#@view_config(context=ApiService)
def service(context, request, obj):
    pass # FIXME


@view_config(context=ApiServerList)
def server_list(context, request):
    return {}
