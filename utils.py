import requests
from typing import Dict, Any


def call_api(name: str, **kwargs) -> Dict[str, Any]:
    url = f'http://127.0.0.1:5700/{name}'
    ret = requests.post(url, data=kwargs)
    return ret


def send_msg(ev: Dict[str, Any], msg: Any) -> Dict[str, Any]:
    return call_api(
        'send_msg',
        message_type=ev['message_type'],
        user_id=ev.get('user_id'),
        group_id=ev.get('group_id'),
        message=msg
    )
