from typing import Dict, Any
import pymongo

from mongodb import find, image_library, user_library, rank, ban_user
from utils import send_msg


def face_collection(ev: Dict[str, Any]):
    if ev['post_type'] == 'message' and ev['message_type'] == 'group':
        uid = ev['user_id']
        msg = ev['message']
        if (msg.startswith('收藏 tag=')) and not find(ban_user, uid):
            msg = msg.replace('收藏 tag=', '', 1).strip()  # 接收“tag=”之后的cmd
            if not find(user_library, msg):
                if not find(rank, uid):
                    dict1 = {"id": uid, "cnt": 1}
                    rank.insert_one(dict1)
                else:
                    for x in rank.find({}, {"id": uid}):
                        print(x)
                    value = x.get("cnt") + 1
                    dict2 = {"id": uid}
                    new_values1 = {"$set": {"cnt": value}}
                    rank.update_one(dict2, new_values1)
                dict3 = {"id": uid, "tag": msg, "image": "0"}
                image_library.insert_one(dict3)  # 向image_library中添加tag
            else:
                print(f'已存在指令为{msg}的tag，请更改tag')

        if msg.startswith('发'):
            msg = (msg.replace('发', '', 1))  # 获取tag
            if find(image_library, msg):  # 从图片库中搜索
                for picture in image_library.find({}, {"id": uid}):
                    print(picture)
                pic = picture.get("image",)
                send_msg(ev, f'[CQ:image,file={pic}]')  # 发送
            else:
                send_msg(ev, f"暂未收藏对应{msg}图片")

        if find(user_library, uid) and not find(ban_user, uid):
            if '[CQ:image,' in msg:  # 测试是否发送图片
                msg = msg.split(',')[3].replace('url=', '', 1).replace(']', '', 1)
                # 查看该用户是否有发送状态
                dict4 = {"id": uid}
                new_values2 = {"$set": {"image": msg}}
                rank.update_one(dict4, new_values2)
                # 将图片存入image_library
                dict5 = {"id": uid}
                rank.delete_one(dict5)
                # 撤销发送状态
