from .echo import echo
from .face_collection import face_collection
from .rank import rank_send

process_func = [
    echo,
    face_collection,
    rank_send,
]  # 插件加载
