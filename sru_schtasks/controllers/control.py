from aiohttp.web import Response
from sru.helpers import controller as hc
import schtasks_shim as schtasks
import logging


logger = logging.getLogger(__name__)


def not_found(**kw):
    msg = {
        "message": "invalid Action requested",
        "code": 404
    }

    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")

    
def run_by_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            run = schtasks.control.run_by_name(kw['name'])
            if run:
                msg.update(run)
                msg.update({
                            'code': 200
                })
            else:
                message = "Someting went wrong starting the task"
                msg.update({
                            'message': message,
                            'code': 500
                })
                logger.debug(message)
        else:
            message = "'name' is missing"
            msg.update({
                        'message': message,
                        'code': 500
            })
            logger.debug(message)
    except Exception as e:
        logger.error("'schtasks/run_by_name' fialed with Exception: {}".format(e))

    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def end_by_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            run = schtasks.control.end_by_name(kw['name'])
            if run:
                msg.update(run)
                msg.update({
                            'code': 200
                })
            else:
                message = "Someting went wrong starting the task"
                msg.update({
                            'message': message,
                            'code': 500
                })
                logger.debug(message)
        else:
            message = "'name' is missing"
            msg.update({
                        'message': message,
                        'code': 500
            })
            logger.debug(message)
    except Exception as e:
        logger.error("'schtasks/end_by_name' fialed with Exception: {}".format(e))

    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")
