from sru.support.web import Response
from sru.support import data_process as hc
import sru.packages.schtasks_shim as schtasks
import logging


logger = logging.getLogger(__name__)


def not_found(**kw):
    msg = {
        "message": "invalid Action requested",
        "result" : [],
        "code": 404
    }

    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")

    
def run_by_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            run = schtasks.control.run_by_name(kw['name'])
            if run['status']:
                msg.update({
                            'code': 200,
                            "message" : run['message'],
                            "result" : [],
                })
            else:
                msg.update({
                            'code': 500,
                            "message" : run['message'],
                            "result" : [],
                })
        else:
            message = "'name' is missing"
            msg.update({
                        'message': message,
                        'result': [],
                        'code': 500
            })
            logger.debug(message)
    except Exception as e:
        message = "'schtasks/run_by_name' failed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result': [],
                    'code': 501
        })
        logger.error(message)

    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def end_by_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            run = schtasks.control.end_by_name(kw['name'])
            if run['status']:
                msg.update({
                            'code': 200,
                            "message" : run['message'],
                            "result" : [],
                })
            else:
                msg.update({
                            'code': 500,
                            "message" : run['message'],
                            "result" : [],
                })
        else:
            message = "'name' is missing"
            msg.update({
                        'message': message,
                        'result': [],
                        'code': 500
            })
            logger.debug(message)
    except Exception as e:
        message = "'schtasks/run_by_name' failed with Exception: {}".format(e)
        msg.update({
                    'message': message,
                    'result': [],
                    'code': 501
        })
        logger.error(message)

    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")
