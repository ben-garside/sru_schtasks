from aiohttp import web
import sru_schtasks.controllers.control as controlCtrl
import sru_schtasks.controllers.edit as editCtrl
import sru_schtasks.controllers.query as queryCtrl
import logging


logger = logging.getLogger(__name__)


params = [
    'action',
    'action_params'
]


async def control(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_params',{}) # set value if non provided
        action = getattr(controlCtrl, data['action'], controlCtrl.not_found)
        res = action(**data['action_params'])
        return res
    else:
        return web.Response(text="an invalid param was found in request")#



async def edit(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_params',{}) # set value if non provided
        action = getattr(editCtrl, data['action'], editCtrl.not_found)
        res = action(**data['action_params'])
        return res
    else:
        return web.Response(text="an invalid param was found in request")



async def query(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_params',{}) # set value if non provided
        action = getattr(queryCtrl, data['action'], queryCtrl.not_found)
        res = action(**data['action_params'])
        return res
    else:
        return web.Response(text="an invalid param was found in request")