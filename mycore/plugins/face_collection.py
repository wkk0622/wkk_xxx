from typing import Dict, Any

from utils import send_msg

image_library: Dict[str, Any] = {}  # 图片库
user_library: Dict[str, Any] = {}  # 录入发送了”收藏 tag=“指令的user_id


def face_collection(ev: Dict[str, Any]):
    if ev['post_type'] == 'message' and ev['message_type'] == 'group':
        msg = ev['message']
        if msg.startswith('收藏 tag='):
            msg = msg.replace('收藏 tag=', '', 1).strip()  # 接收“tag=”之后的cmd
            if msg not in image_library:
                user_library[ev['user_id']] = msg
            else:
                print(f'已存在指令为{msg}的tag，请更改tag')

        if msg.startswith('发'):
            if len(image_library) != 0:  # 判断图片库中有图片
                msg = msg.replace('发', '', 1)  # 获取tag
                if picture := image_library.get(msg):  # 从图片库中搜索
                    send_msg(ev, f'[CQ:image,file={picture}]')  # 发送
                else:
                    print(f"暂未收藏对应{msg}图片")
            else:
                print('暂未收藏任何图片')

        if ev['user_id'] in user_library:
            if '[CQ:image,' in msg:  # 测试是否发送图片
                msg = msg.split(',')[3].replace('url=', '', 1).replace(']', '', 1)
                # 查看该用户是否有发送状态
                image_library[user_library[ev['user_id']]] = msg
                # 将图片存入image_library
                del user_library[ev['user_id']]
                # 撤销发送状态
