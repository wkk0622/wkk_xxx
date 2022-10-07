import requests
from typing import Dict, Any


def call_api(name: str, **kwargs) -> Dict[str, Any]:  # 调用API
    url = f'http://127.0.0.1:5700/{name}'  # url拼接——url前缀+后缀
    ret = requests.post(url, data=kwargs)  # 选用post方法请求API
    return ret


def send_msg(ev: Dict[str, Any], msg: Any) -> Dict[str, Any]:  # 发送消息
    return call_api(
        'send_msg',
        message_type=ev['message_type'],
        user_id=ev.get('user_id'),
        group_id=ev.get('group_id'),
        message=msg
    )  # 返回字典，便于获取参数
