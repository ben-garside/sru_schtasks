from sru.support.web import Response
import sru_schtasks.control as controlCtrl
import sru_schtasks.edit as editCtrl
import sru_schtasks.query as queryCtrl
import logging


logger = logging.getLogger(__name__)
params = [
    'action',
    'action_param'
]


async def control(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{}) # set value if non provided
        action = getattr(controlCtrl, data['action'], controlCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")#


async def edit(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{}) # set value if non provided
        action = getattr(editCtrl, data['action'], editCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")


async def query(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_param',{}) # set value if non provided
        action = getattr(queryCtrl, data['action'], queryCtrl.not_found)
        res = action(**data['action_param'])
        return res
    else:
        return Response(text="an invalid param was found in request")
