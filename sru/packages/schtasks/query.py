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


def get_all(**kw):
    msg = {}
    try:
        tasks = schtasks.query.get_all()
        message = "{} sites found".format(len(tasks))
        msg.update({
            "message": message,
            "code": 200,
            "result": tasks
        })
        logger.debug(message)

    except Exception as e:
        message = "'schtasks/get_all' fialed with Exception: {}".format(e)
        msg.update({
            "message": message,
            "result" : [],
            "code": 501
        })
        logger.error(message)

    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_name(**kw):
    msg = {}
    try:
        if 'name' in kw.keys():
            kw.setdefault('partial', False)
            if isinstance(kw['name'], str):
                tasks = schtasks.query.get_by_name(kw['name'], partial=kw['partial'])
                if kw['partial'] == True:
                    site_len = len(tasks)
                else:
                    site_len = 1
                    tasks = [tasks]
                if tasks:
                    message = "{} task(s) found with name '{}' (with partial:{})".format(site_len, kw['name'], kw['partial'])
                    msg.update({
                        'result': tasks,
                        'message': message,
                        'code': 200
                    })
                    logger.debug(message)
                else:
                    message = "No tasks found with name '{}' (with partial:{})".format(kw['name'], kw['partial'])
                    msg.update({
                        "result" : [],
                        'message': message,
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'name' type must be a string"
                msg.update({
                    'message': message,
                    "result" : [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "The 'name' parameter is missing"
            msg.update({
                'message': message,
                "result" : [],
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        message = "'schtasks/get_by_name' fialed with Exception: {}".format(e)
        msg.update({
            'message': message,
            "result" : [],
            'code': 501
        })
        logger.error(message)
    
    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def get_by_status(**kw):
    allowed_states = ['ready', 'unknown']
    msg = {}
    try:
        if 'status' in kw.keys():
            if isinstance(kw['status'], str):
                if kw['status'].lower() in allowed_states:
                    tasks = schtasks.query.get_by_status(kw['status'])
                    if len(tasks) > 0:
                        message = "{} tasks(s) found that are '{}'".format(len(tasks), kw['status'])
                        msg.update({
                            'result': tasks,
                            'message': message,
                            'code': 200
                        })
                        logger.debug(message)
                    else:
                        message = "No tasks are '{}'".format(kw['status'])
                        msg.update({
                            'message': message,
                            "result" : [],
                            'code': 404
                        })
                        logger.debug(message)
                else:
                    message = 'status must be in: {}'.format(allowed_states)
                    msg.update({
                        'message': message,
                        "result" : [],
                        'code': 404
                    })
                    logger.debug(message)
            else:
                message = "'status' must be string"
                msg.update({
                    'message': message,
                    "result" : [],
                    'code': 404
                })
                logger.debug(message)
        else:
            message = "'state' parameter is missing"
            msg.update({
                'message': message,
                "result" : [],
                'code': 404
            })
            logger.debug(message)
    except Exception as e:
        message = "'sites/get_by_state' fialed with Exception: {}".format(e)
        msg.update({
            'message': message,
            "result" : [],
            'code': 501
        })
        logger.error(message)
    
    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")