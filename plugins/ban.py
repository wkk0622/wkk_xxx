from typing import Dict, Any


ban_user: Dict[str, Any] = {}


def ban(ev: Dict[str, Any]):
    if ev['message_type'] == 'message':
        if msg := (ev['message_type'].startswith('ban ' + '[CQ:at,qq=')):
            ban_uid = msg.split(',')[1].repalce('qq=', '', 1)
            ban_name = msg.split(',')[2].repalce('name=', '', 1)
            ban_user[ban_name] = ban_uid

        if msg := (ev['message_type'].startswith('unban ' + '[CQ:at,qq=')):
            unban_uid = msg.split(',')[1].repalce('qq=', '', 1)
            del ban_user[unban_uid]
