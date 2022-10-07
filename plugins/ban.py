from typing import Dict, Any
from mongodb import ban_user


def ban(ev: Dict[str, Any]):
    if ev['message_type'] == 'message':
        if msg := (ev['message_type'].startswith('ban ' + '[CQ:at,qq=')):
            ban_uid = msg.split(',')[1].repalce('qq=', '', 1)
            ban_name = msg.split(',')[2].repalce('name=', '', 1)
            dict = {'id': ban_uid, 'name': ban_name}
            ban_user.insert_one(dict)

        if msg := (ev['message_type'].startswith('unban ' + '[CQ:at,qq=')):
            unban_uid = msg.split(',')[1].repalce('qq=', '', 1)
            dict = {'name': unban_uid}
            ban_user.delete_one(dict)
