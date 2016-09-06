from sru.support.web import Response
import .control as controlCtrl
import .edit as editCtrl
import .query as queryCtrl
import logging


logger = logging.getLogger(__name__)
params = [
    'action',
    'action_param'
]


async def control(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{})
        action = getattr(controlCtrl, data['action'], controlCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")#


async def edit(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{})
        action = getattr(editCtrl, data['action'], editCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")


async def query(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{})
        action = getattr(queryCtrl, data['action'], queryCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")
