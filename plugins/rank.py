from typing import Dict, Any

from .face_collection import rank
from utils import send_msg


def rank_send(ev: Dict[str, Any]):
    if ev['post_type'] == 'message' and ev['message_type'] == 'group':
        if ev['message'] == 'rank':
            list_rank = list(rank.items())
            list_rank.sort(key=lambda x: x[1], reverse=True)
            if len(rank) >= 5:
                send_msg(ev, '\n'.join(list_rank[:5]))
            else:
                send_msg(ev, '\n'.join(list_rank[:]))
