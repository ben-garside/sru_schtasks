from aiohttp.web import Response
from sru.support import data_process as hc
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