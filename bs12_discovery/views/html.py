from pyramid.view import view_config

from bs12_discovery.resource import Root


@view_config(renderer='../templates/mytemplate.pt', context=Root)
def my_view(request):
    return {'project': 'bs12_discovery'}
