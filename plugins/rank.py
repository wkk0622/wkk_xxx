from typing import Dict, Any

from mongodb import rank
from utils import send_msg


def rank_send(ev: Dict[str, Any]):
    if ev['post_type'] == 'message' and ev['message_type'] == 'group':
        if ev['message'].startswith("rank"):
            rank_sort = rank.find().sort("cnt", -1)
            list = []
            for x in rank_sort.find({}, {"_id": 0, "id": 1, "name": 1, "cnt": 1}):
                list.append(x)
            if len(list) >= 5:
                send_msg(ev, f'{list[0:5]}')
            else:
                send_msg(ev, f'{list}')
        # list_rank = list(rank.items())
        # list_rank.sort(key=lambda x: x[1], reverse=True)
        # if len(rank) >= 5:
        #    send_msg(ev, '\n'.join(list_rank[:5]))
        #   else:
        #      send_msg(ev, '\n'.join(list_rank[:]))
