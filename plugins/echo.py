from typing import Dict, Any
from utils import call_api


def echo(ev: Dict[str, Any]):
    if ev['post_type'] == 'message':
        msg: str = ev['message']
        if msg.startswith("/echo"):
            msg = msg.replace('/echo', '', 1)
            msg = msg.strip()
            # 调整echo输出的消息格式
            if ev['message_type'] == 'group':
                msg = f'[CQ:at,qq={ev["user_id"]}] {msg}'  # CQ码拼接使用
            call_api(
                'send_msg',
                message_type=ev['message_type'],
                group_id=ev.get('group_id'),
                message=msg
            )  # 返回字典，便于获取参数
