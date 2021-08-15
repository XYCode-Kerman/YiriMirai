# -*- coding: utf-8 -*-
"""
`mirai.bot` 模块的存根文件，用于补全代码提示。
"""
from pathlib import Path
from typing import (
    Any, Awaitable, Callable, Dict, Iterable, List, Optional, Type, Union,
    overload
)

from mirai.asgi import ASGI
from mirai.models.base import MiraiBaseModel

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from mirai.adapters.base import Adapter, AdapterInterface, ApiProvider
from mirai.bus import AbstractEventBus
from mirai.models.api import (
    AboutResponse, ApiModel, FileInfoResponse, FileListResponse,
    FileMkdirResponse, FileProperties, FriendListResponse, GroupListResponse,
    MemberListResponse, MessageFromIdResponse, MessageResponse,
    ProfileResponse, Response, RespOperate, SessionInfoResponse
)
from mirai.models.entities import (
    Entity, Friend, Group, GroupConfigModel, GroupMember, MemberInfoModel,
    Subject
)
from mirai.models.events import Event, MessageEvent
from mirai.models.message import Image, MessageChain, MessageComponent, Voice
from mirai.utils import Singleton


class LifeSpan(Event):
    type: str


class Startup(LifeSpan):
    type: str


class Shutdown(LifeSpan):
    type: str


def __getattr__(name) -> Any:
    ...


class SimpleMirai(ApiProvider, AdapterInterface, AbstractEventBus):
    qq: int

    def __init__(self, qq: int, adapter: Adapter) -> None:
        ...

    def subscribe(self, event, func: Callable, priority: int = 0) -> None:
        ...

    def unsubscribe(self, event, func: Callable) -> None:
        ...

    async def emit(self, event, *args, **kwargs) -> List[Awaitable[Any]]:
        ...

    async def call_api(self, api: str, *args, **kwargs):
        ...

    def on(self, event: str, priority: int = 0) -> Callable:
        ...

    @property
    def adapter_info(self) -> Dict[str, Any]:
        ...

    async def use_adapter(self, adapter: Adapter):
        ...

    async def startup(self) -> None:
        ...

    async def background(self) -> None:
        ...

    async def shutdown(self) -> None:
        ...

    @property
    def session(self) -> str:
        ...

    @property
    def asgi(self) -> MiraiRunner:
        ...

    def run(
        self,
        host: str = ...,
        port: int = ...,
        asgi_server: str = ...,
        **kwargs
    ) -> None:
        ...


class MiraiRunner(Singleton):
    _asgi: ASGI
    bots: Iterable[SimpleMirai]

    def __init__(self, *bots: SimpleMirai) -> None:
        ...

    async def startup(self) -> None:
        ...

    async def shutdown(self) -> None:
        ...

    async def __call__(self, scope, recv, send) -> None:
        ...

    def run(
        self,
        host: str = ...,
        port: int = ...,
        asgi_server: str = ...,
        **kwargs
    ) -> None:
        ...


class Mirai(SimpleMirai):
    def __init__(self, qq: int, adapter: Adapter) -> None:
        ...

    def on(
        self,
        event_type: Union[Type[Event], str],
        priority: int = 0
    ) -> Callable:
        ...

    def api(self, api: str) -> ApiModel.Proxy:
        ...

    def __getattr__(self, api: str) -> ApiModel.Proxy:
        ...

    async def send(
        self,
        target: Union[Entity, MessageEvent],
        message: Union[MessageChain, Iterable[Union[MessageComponent, str]],
                       MessageComponent, str],
        quote: bool = ...
    ) -> int:
        ...

    async def get_friend(self, id: int) -> Optional[Friend]:
        ...

    async def get_group(self, id: int) -> Optional[Group]:
        ...

    async def get_group_member(self, group: Union[Group, int],
                               id: int) -> Optional[GroupMember]:
        ...

    async def get_entity(self, subject: Subject) -> Optional[Entity]:
        ...

    async def is_admin(self, group: Group) -> bool:
        ...

    ### 以下为自动生成 ###
    # About

    class __AboutProxy():
        async def get(self) -> AboutResponse:
            """获取插件信息。"""

    @overload
    def about(self) -> __AboutProxy:
        """获取插件信息。"""

    @overload
    async def about(self) -> AboutResponse:
        """获取插件信息。"""

    # BotProfile

    class __BotProfileProxy():
        async def get(self) -> ProfileResponse:
            """获取 Bot 资料。"""

    @overload
    def bot_profile(self) -> __BotProfileProxy:
        """获取 Bot 资料。"""

    @overload
    async def bot_profile(self) -> ProfileResponse:
        """获取 Bot 资料。"""

    # CmdExecute

    class __CmdExecuteProxy():
        async def set(
            self, command: Union[MessageChain, Iterable[Union[MessageComponent,
                                                              str]], str]
        ) -> Response:
            """执行命令。

                command (`Union[MessageChain,Iterable[Union[MessageComponent,str]],str]`): 命令。
            """

    @overload
    def cmd_execute(self) -> __CmdExecuteProxy:
        """执行命令。"""

    @overload
    async def cmd_execute(
        self, command: Union[MessageChain, Iterable[Union[MessageComponent,
                                                          str]], str]
    ) -> Response:
        """执行命令。

            command (`Union[MessageChain,Iterable[Union[MessageComponent,str]],str]`): 命令。
        """

    # CmdRegister

    class __CmdRegisterProxy():
        async def set(
            self,
            name: str,
            usage: str,
            description: str,
            alias: Union[List[str], None] = None
        ) -> Response:
            """注册命令。

                name (`str`): 命令名称。

                usage (`str`): 使用说明。

                description (`str`): 命令描述。

                alias (`Union[List[str],None] = None`): 可选。命令别名。
            """

    @overload
    def cmd_register(self) -> __CmdRegisterProxy:
        """注册命令。"""

    @overload
    async def cmd_register(
        self,
        name: str,
        usage: str,
        description: str,
        alias: Union[List[str], None] = None
    ) -> Response:
        """注册命令。

            name (`str`): 命令名称。

            usage (`str`): 使用说明。

            description (`str`): 命令描述。

            alias (`Union[List[str],None] = None`): 可选。命令别名。
        """

    # DeleteFriend

    class __DeleteFriendProxy():
        async def set(self, target: int) -> Response:
            """删除好友。

                target (`int`): 需要删除的好友 QQ 号。
            """

    @overload
    def delete_friend(self) -> __DeleteFriendProxy:
        """删除好友。"""

    @overload
    async def delete_friend(self, target: int) -> Response:
        """删除好友。

            target (`int`): 需要删除的好友 QQ 号。
        """

    # FileDelete

    class __FileDeleteProxy():
        async def set(self, id: str, target: int) -> Response:
            """删除文件。

                id (`str`): 欲删除的文件 id。

                target (`int`): 群号或好友 QQ 号。
            """

    @overload
    def file_delete(self) -> __FileDeleteProxy:
        """删除文件。"""

    @overload
    async def file_delete(self, id: str, target: int) -> Response:
        """删除文件。

            id (`str`): 欲删除的文件 id。

            target (`int`): 群号或好友 QQ 号。
        """

    # FileInfo

    class __FileInfoProxy():
        async def get(
            self,
            id: str,
            target: int,
            with_download_info: Union[bool, None] = None
        ) -> FileInfoResponse:
            """查看文件信息。

                id (`str`): 文件 id。

                target (`int`): 群号或好友 QQ 号。

                with_download_info (`Union[bool,None] = None`): 是否携带下载信息。
            """

    @overload
    def file_info(self) -> __FileInfoProxy:
        """查看文件信息。"""

    @overload
    async def file_info(
        self,
        id: str,
        target: int,
        with_download_info: Union[bool, None] = None
    ) -> FileInfoResponse:
        """查看文件信息。

            id (`str`): 文件 id。

            target (`int`): 群号或好友 QQ 号。

            with_download_info (`Union[bool,None] = None`): 是否携带下载信息。
        """

    # FileList

    class __FileListProxy():
        async def get(
            self,
            id: str,
            target: int,
            with_download_info: Union[bool, None] = None
        ) -> FileListResponse:
            """查看文件列表。

                id (`str`): 文件夹 id，空串为根目录。

                target (`int`): 群号或好友 QQ 号。

                with_download_info (`Union[bool,None] = None`): 是否携带下载信息。
            """

    @overload
    def file_list(self) -> __FileListProxy:
        """查看文件列表。"""

    @overload
    async def file_list(
        self,
        id: str,
        target: int,
        with_download_info: Union[bool, None] = None
    ) -> FileListResponse:
        """查看文件列表。

            id (`str`): 文件夹 id，空串为根目录。

            target (`int`): 群号或好友 QQ 号。

            with_download_info (`Union[bool,None] = None`): 是否携带下载信息。
        """

    # FileMkdir

    class __FileMkdirProxy():
        async def set(
            self, id: str, target: int, directory_name: str
        ) -> FileMkdirResponse:
            """创建文件夹。

                id (`str`): 父目录 id。

                target (`int`): 群号或好友 QQ 号。

                directory_name (`str`): 新建文件夹名。
            """

    @overload
    def file_mkdir(self) -> __FileMkdirProxy:
        """创建文件夹。"""

    @overload
    async def file_mkdir(
        self, id: str, target: int, directory_name: str
    ) -> FileMkdirResponse:
        """创建文件夹。

            id (`str`): 父目录 id。

            target (`int`): 群号或好友 QQ 号。

            directory_name (`str`): 新建文件夹名。
        """

    # FileMove

    class __FileMoveProxy():
        async def set(self, id: str, target: int, move_to: str) -> Response:
            """移动文件。

                id (`str`): 欲移动的文件 id。

                target (`int`): 群号或好友 QQ 号。

                move_to (`str`): 移动目标文件夹 id。
            """

    @overload
    def file_move(self) -> __FileMoveProxy:
        """移动文件。"""

    @overload
    async def file_move(self, id: str, target: int, move_to: str) -> Response:
        """移动文件。

            id (`str`): 欲移动的文件 id。

            target (`int`): 群号或好友 QQ 号。

            move_to (`str`): 移动目标文件夹 id。
        """

    # FileRename

    class __FileRenameProxy():
        async def set(self, id: str, target: int, rename_to: str) -> Response:
            """重命名文件。

                id (`str`): 欲重命名的文件 id。

                target (`int`): 群号或好友 QQ 号。

                rename_to (`str`): 新文件名。
            """

    @overload
    def file_rename(self) -> __FileRenameProxy:
        """重命名文件。"""

    @overload
    async def file_rename(
        self, id: str, target: int, rename_to: str
    ) -> Response:
        """重命名文件。

            id (`str`): 欲重命名的文件 id。

            target (`int`): 群号或好友 QQ 号。

            rename_to (`str`): 新文件名。
        """

    # FileUpload

    class __FileUploadProxy():
        async def set(
            self,
            type: Literal['group'],
            target: int,
            file: Union[str, Path],
            path: str = ''
        ) -> FileProperties:
            """文件上传。（暂时不可用）

                type (`Literal['group']`): 上传的文件类型。

                target (`int`): 群号。

                file (`Union[str,Path]`): 上传的文件的本地路径。

                path (`str = ''`): 上传目录的 id，空串为上传到根目录。
            """

    @overload
    def file_upload(self) -> __FileUploadProxy:
        """文件上传。（暂时不可用）"""

    @overload
    async def file_upload(
        self,
        type: Literal['group'],
        target: int,
        file: Union[str, Path],
        path: str = ''
    ) -> FileProperties:
        """文件上传。（暂时不可用）

            type (`Literal['group']`): 上传的文件类型。

            target (`int`): 群号。

            file (`Union[str,Path]`): 上传的文件的本地路径。

            path (`str = ''`): 上传目录的 id，空串为上传到根目录。
        """

    # FriendList

    class __FriendListProxy():
        async def get(self) -> FriendListResponse:
            """获取好友列表。"""

    @overload
    def friend_list(self) -> __FriendListProxy:
        """获取好友列表。"""

    @overload
    async def friend_list(self) -> FriendListResponse:
        """获取好友列表。"""

    # FriendProfile

    class __FriendProfileProxy():
        async def get(self, target: int) -> ProfileResponse:
            """获取好友资料。

                target (`int`): 好友 QQ 号。
            """

    @overload
    def friend_profile(self) -> __FriendProfileProxy:
        """获取好友资料。"""

    @overload
    async def friend_profile(self, target: int) -> ProfileResponse:
        """获取好友资料。

            target (`int`): 好友 QQ 号。
        """

    # GroupConfig

    class __GroupConfigProxy():
        async def get(
            self,
            target: int,
            config: Union[GroupConfigModel, None] = None
        ) -> GroupConfigModel:
            """获取或修改群设置。

                target (`int`): 群号。

                config (`Union[GroupConfigModel,None] = None`): 仅修改时可用。群设置。
            """

        async def set(
            self,
            target: int,
            config: Union[GroupConfigModel, None] = None
        ) -> Response:
            """获取或修改群设置。

                target (`int`): 群号。

                config (`Union[GroupConfigModel,None] = None`): 仅修改时可用。群设置。
            """

    @overload
    def group_config(self) -> __GroupConfigProxy:
        """获取或修改群设置。"""

    @overload
    async def group_config(
        self,
        target: int,
        config: Union[GroupConfigModel, None] = None
    ) -> GroupConfigModel:
        """获取或修改群设置。

            target (`int`): 群号。

            config (`Union[GroupConfigModel,None] = None`): 仅修改时可用。群设置。
        """

    # GroupList

    class __GroupListProxy():
        async def get(self) -> GroupListResponse:
            """获取群列表。"""

    @overload
    def group_list(self) -> __GroupListProxy:
        """获取群列表。"""

    @overload
    async def group_list(self) -> GroupListResponse:
        """获取群列表。"""

    # Kick

    class __KickProxy():
        async def set(
            self, target: int, member_id: int, msg: str = ''
        ) -> Response:
            """移出群成员。

                target (`int`): 指定群的群号。

                member_id (`int`): 指定群成员的 QQ 号。

                msg (`str = ''`): 可选。信息。
            """

    @overload
    def kick(self) -> __KickProxy:
        """移出群成员。"""

    @overload
    async def kick(
        self, target: int, member_id: int, msg: str = ''
    ) -> Response:
        """移出群成员。

            target (`int`): 指定群的群号。

            member_id (`int`): 指定群成员的 QQ 号。

            msg (`str = ''`): 可选。信息。
        """

    # MemberInfo

    class __MemberInfoProxy():
        async def get(
            self,
            target: int,
            member_id: int,
            info: Union[MemberInfoModel, None] = None
        ) -> MemberInfoModel:
            """获取或修改群成员资料。

                target (`int`): 群号。

                member_id (`int`): 指定群成员的 QQ 号。

                info (`Union[MemberInfoModel,None] = None`): 仅修改时可用。群成员资料。
            """

        async def set(
            self,
            target: int,
            member_id: int,
            info: Union[MemberInfoModel, None] = None
        ) -> Response:
            """获取或修改群成员资料。

                target (`int`): 群号。

                member_id (`int`): 指定群成员的 QQ 号。

                info (`Union[MemberInfoModel,None] = None`): 仅修改时可用。群成员资料。
            """

    @overload
    def member_info(self) -> __MemberInfoProxy:
        """获取或修改群成员资料。"""

    @overload
    async def member_info(
        self,
        target: int,
        member_id: int,
        info: Union[MemberInfoModel, None] = None
    ) -> MemberInfoModel:
        """获取或修改群成员资料。

            target (`int`): 群号。

            member_id (`int`): 指定群成员的 QQ 号。

            info (`Union[MemberInfoModel,None] = None`): 仅修改时可用。群成员资料。
        """

    # MemberList

    class __MemberListProxy():
        async def get(self, target: int) -> MemberListResponse:
            """获取群成员列表。

                target (`int`): 指定群的群号。
            """

    @overload
    def member_list(self) -> __MemberListProxy:
        """获取群成员列表。"""

    @overload
    async def member_list(self, target: int) -> MemberListResponse:
        """获取群成员列表。

            target (`int`): 指定群的群号。
        """

    # MemberProfile

    class __MemberProfileProxy():
        async def get(self, target: int, member_id: int) -> ProfileResponse:
            """获取群成员资料。

                target (`int`): 指定群的群号。

                member_id (`int`): 指定群成员的 QQ 号。
            """

    @overload
    def member_profile(self) -> __MemberProfileProxy:
        """获取群成员资料。"""

    @overload
    async def member_profile(
        self, target: int, member_id: int
    ) -> ProfileResponse:
        """获取群成员资料。

            target (`int`): 指定群的群号。

            member_id (`int`): 指定群成员的 QQ 号。
        """

    # MessageFromId

    class __MessageFromIdProxy():
        async def get(self, id: int) -> MessageFromIdResponse:
            """通过 message_id 获取消息。

                id (`int`): 获取消息的 message_id。
            """

    @overload
    def message_from_id(self) -> __MessageFromIdProxy:
        """通过 message_id 获取消息。"""

    @overload
    async def message_from_id(self, id: int) -> MessageFromIdResponse:
        """通过 message_id 获取消息。

            id (`int`): 获取消息的 message_id。
        """

    # Mute

    class __MuteProxy():
        async def set(
            self, target: int, member_id: int, time: int
        ) -> Response:
            """禁言群成员。

                target (`int`): 指定群的群号。

                member_id (`int`): 指定群成员的 QQ 号。

                time (`int`): 禁言时间，单位为秒，最多30天，默认为0。
            """

    @overload
    def mute(self) -> __MuteProxy:
        """禁言群成员。"""

    @overload
    async def mute(self, target: int, member_id: int, time: int) -> Response:
        """禁言群成员。

            target (`int`): 指定群的群号。

            member_id (`int`): 指定群成员的 QQ 号。

            time (`int`): 禁言时间，单位为秒，最多30天，默认为0。
        """

    # MuteAll

    class __MuteAllProxy():
        async def set(self, target: int) -> Response:
            """全体禁言。

                target (`int`): 指定群的群号。
            """

    @overload
    def mute_all(self) -> __MuteAllProxy:
        """全体禁言。"""

    @overload
    async def mute_all(self, target: int) -> Response:
        """全体禁言。

            target (`int`): 指定群的群号。
        """

    # Quit

    class __QuitProxy():
        async def set(self, target: int) -> Response:
            """退出群聊。

                target (`int`): 指定群的群号。
            """

    @overload
    def quit(self) -> __QuitProxy:
        """退出群聊。"""

    @overload
    async def quit(self, target: int) -> Response:
        """退出群聊。

            target (`int`): 指定群的群号。
        """

    # Recall

    class __RecallProxy():
        async def set(self, target: int) -> Response:
            """撤回消息。

                target (`int`): 需要撤回的消息的 message_id。
            """

    @overload
    def recall(self) -> __RecallProxy:
        """撤回消息。"""

    @overload
    async def recall(self, target: int) -> Response:
        """撤回消息。

            target (`int`): 需要撤回的消息的 message_id。
        """

    # RespBotInvitedJoinGroupRequestEvent

    class __RespBotInvitedJoinGroupRequestEventProxy():
        async def set(
            self, event_id: int, from_id: int, group_id: int,
            operate: Union[int, RespOperate], message: str
        ) -> MiraiBaseModel:
            """响应被邀请入群申请。

                event_id (`int`): 响应申请事件的标识。

                from_id (`int`): 事件对应申请人 QQ 号。

                group_id (`int`): 事件对应申请人的群号，可能为0。

                operate (`Union[int,RespOperate]`): 响应的操作类型。

                message (`str`): 回复的信息。
            """

    @overload
    def resp_bot_invited_join_group_request_event(
        self
    ) -> __RespBotInvitedJoinGroupRequestEventProxy:
        """响应被邀请入群申请。"""

    @overload
    async def resp_bot_invited_join_group_request_event(
        self, event_id: int, from_id: int, group_id: int,
        operate: Union[int, RespOperate], message: str
    ) -> MiraiBaseModel:
        """响应被邀请入群申请。

            event_id (`int`): 响应申请事件的标识。

            from_id (`int`): 事件对应申请人 QQ 号。

            group_id (`int`): 事件对应申请人的群号，可能为0。

            operate (`Union[int,RespOperate]`): 响应的操作类型。

            message (`str`): 回复的信息。
        """

    # RespMemberJoinRequestEvent

    class __RespMemberJoinRequestEventProxy():
        async def set(
            self, event_id: int, from_id: int, group_id: int,
            operate: Union[int, RespOperate], message: str
        ) -> MiraiBaseModel:
            """响应用户入群申请。

                event_id (`int`): 响应申请事件的标识。

                from_id (`int`): 事件对应申请人 QQ 号。

                group_id (`int`): 事件对应申请人的群号。

                operate (`Union[int,RespOperate]`): 响应的操作类型。

                message (`str`): 回复的信息。
            """

    @overload
    def resp_member_join_request_event(
        self
    ) -> __RespMemberJoinRequestEventProxy:
        """响应用户入群申请。"""

    @overload
    async def resp_member_join_request_event(
        self, event_id: int, from_id: int, group_id: int,
        operate: Union[int, RespOperate], message: str
    ) -> MiraiBaseModel:
        """响应用户入群申请。

            event_id (`int`): 响应申请事件的标识。

            from_id (`int`): 事件对应申请人 QQ 号。

            group_id (`int`): 事件对应申请人的群号。

            operate (`Union[int,RespOperate]`): 响应的操作类型。

            message (`str`): 回复的信息。
        """

    # RespNewFriendRequestEvent

    class __RespNewFriendRequestEventProxy():
        async def set(
            self, event_id: int, from_id: int, group_id: int,
            operate: Union[int, RespOperate], message: str
        ) -> MiraiBaseModel:
            """响应添加好友申请。

                event_id (`int`): 响应申请事件的标识。

                from_id (`int`): 事件对应申请人 QQ 号。

                group_id (`int`): 事件对应申请人的群号，可能为0。

                operate (`Union[int,RespOperate]`): 响应的操作类型。

                message (`str`): 回复的信息。
            """

    @overload
    def resp_new_friend_request_event(
        self
    ) -> __RespNewFriendRequestEventProxy:
        """响应添加好友申请。"""

    @overload
    async def resp_new_friend_request_event(
        self, event_id: int, from_id: int, group_id: int,
        operate: Union[int, RespOperate], message: str
    ) -> MiraiBaseModel:
        """响应添加好友申请。

            event_id (`int`): 响应申请事件的标识。

            from_id (`int`): 事件对应申请人 QQ 号。

            group_id (`int`): 事件对应申请人的群号，可能为0。

            operate (`Union[int,RespOperate]`): 响应的操作类型。

            message (`str`): 回复的信息。
        """

    # SendFriendMessage

    class __SendFriendMessageProxy():
        async def set(
            self,
            target: int,
            message_chain: Union[MessageChain, Iterable[Union[MessageComponent,
                                                              str]], str],
            quote: Union[int, None] = None
        ) -> MessageResponse:
            """发送好友消息。

                target (`int`): 发送消息目标好友的 QQ 号。

                message_chain (`Union[MessageChain,Iterable[Union[MessageComponent,str]],str]`): 消息链。

                quote (`Union[int,None] = None`): 可选。引用一条消息的 message_id 进行回复。
            """

    @overload
    def send_friend_message(self) -> __SendFriendMessageProxy:
        """发送好友消息。"""

    @overload
    async def send_friend_message(
        self,
        target: int,
        message_chain: Union[MessageChain, Iterable[Union[MessageComponent,
                                                          str]], str],
        quote: Union[int, None] = None
    ) -> MessageResponse:
        """发送好友消息。

            target (`int`): 发送消息目标好友的 QQ 号。

            message_chain (`Union[MessageChain,Iterable[Union[MessageComponent,str]],str]`): 消息链。

            quote (`Union[int,None] = None`): 可选。引用一条消息的 message_id 进行回复。
        """

    # SendGroupMessage

    class __SendGroupMessageProxy():
        async def set(
            self,
            target: int,
            message_chain: Union[MessageChain, Iterable[Union[MessageComponent,
                                                              str]], str],
            quote: Union[int, None] = None
        ) -> MessageResponse:
            """发送群消息。

                target (`int`): 发送消息目标群的群号。

                message_chain (`Union[MessageChain,Iterable[Union[MessageComponent,str]],str]`): 消息链。

                quote (`Union[int,None] = None`): 可选。引用一条消息的 message_id 进行回复。
            """

    @overload
    def send_group_message(self) -> __SendGroupMessageProxy:
        """发送群消息。"""

    @overload
    async def send_group_message(
        self,
        target: int,
        message_chain: Union[MessageChain, Iterable[Union[MessageComponent,
                                                          str]], str],
        quote: Union[int, None] = None
    ) -> MessageResponse:
        """发送群消息。

            target (`int`): 发送消息目标群的群号。

            message_chain (`Union[MessageChain,Iterable[Union[MessageComponent,str]],str]`): 消息链。

            quote (`Union[int,None] = None`): 可选。引用一条消息的 message_id 进行回复。
        """

    # SendNudge

    class __SendNudgeProxy():
        async def set(
            self, target: int, subject: int, kind: Literal['Friend', 'Group',
                                                           'Stranger']
        ) -> Response:
            """发送头像戳一戳消息。

                target (`int`): 戳一戳的目标 QQ 号，可以为 bot QQ 号。

                subject (`int`): 戳一戳接受主体（上下文），戳一戳信息会发送至该主体，为群号或好友 QQ 号。

                kind (`Literal['Friend','Group','Stranger']` 上下文类型，可选值 `Friend`, `Group`, `Stranger`):。
            """

    @overload
    def send_nudge(self) -> __SendNudgeProxy:
        """发送头像戳一戳消息。"""

    @overload
    async def send_nudge(
        self, target: int, subject: int, kind: Literal['Friend', 'Group',
                                                       'Stranger']
    ) -> Response:
        """发送头像戳一戳消息。

            target (`int`): 戳一戳的目标 QQ 号，可以为 bot QQ 号。

            subject (`int`): 戳一戳接受主体（上下文），戳一戳信息会发送至该主体，为群号或好友 QQ 号。

            kind (`Literal['Friend','Group','Stranger']` 上下文类型，可选值 `Friend`, `Group`, `Stranger`):。
        """

    # SendTempMessage

    class __SendTempMessageProxy():
        async def set(
            self,
            qq: int,
            group: int,
            message_chain: Union[MessageChain, Iterable[Union[MessageComponent,
                                                              str]], str],
            quote: Union[int, None] = None
        ) -> MessageResponse:
            """发送临时消息。

                qq (`int`): 临时会话对象 QQ 号。

                group (`int`): 临时会话对象群号。

                message_chain (`Union[MessageChain,Iterable[Union[MessageComponent,str]],str]`): 消息链。

                quote (`Union[int,None] = None`): 可选。引用一条消息的 message_id 进行回复。
            """

    @overload
    def send_temp_message(self) -> __SendTempMessageProxy:
        """发送临时消息。"""

    @overload
    async def send_temp_message(
        self,
        qq: int,
        group: int,
        message_chain: Union[MessageChain, Iterable[Union[MessageComponent,
                                                          str]], str],
        quote: Union[int, None] = None
    ) -> MessageResponse:
        """发送临时消息。

            qq (`int`): 临时会话对象 QQ 号。

            group (`int`): 临时会话对象群号。

            message_chain (`Union[MessageChain,Iterable[Union[MessageComponent,str]],str]`): 消息链。

            quote (`Union[int,None] = None`): 可选。引用一条消息的 message_id 进行回复。
        """

    # SessionInfo

    class __SessionInfoProxy():
        async def get(self) -> SessionInfoResponse:
            """获取机器人信息。"""

    @overload
    def session_info(self) -> __SessionInfoProxy:
        """获取机器人信息。"""

    @overload
    async def session_info(self) -> SessionInfoResponse:
        """获取机器人信息。"""

    # SetEssence

    class __SetEssenceProxy():
        async def set(self, target: int) -> Response:
            """设置群精华消息。

                target (`int`): 精华消息的 message_id。
            """

    @overload
    def set_essence(self) -> __SetEssenceProxy:
        """设置群精华消息。"""

    @overload
    async def set_essence(self, target: int) -> Response:
        """设置群精华消息。

            target (`int`): 精华消息的 message_id。
        """

    # Unmute

    class __UnmuteProxy():
        async def set(self, target: int, member_id: int) -> Response:
            """解除群成员禁言。

                target (`int`): 指定群的群号。

                member_id (`int`): 指定群成员的 QQ 号。
            """

    @overload
    def unmute(self) -> __UnmuteProxy:
        """解除群成员禁言。"""

    @overload
    async def unmute(self, target: int, member_id: int) -> Response:
        """解除群成员禁言。

            target (`int`): 指定群的群号。

            member_id (`int`): 指定群成员的 QQ 号。
        """

    # UnmuteAll

    class __UnmuteAllProxy():
        async def set(self, target: int) -> Response:
            """解除全体禁言。

                target (`int`): 指定群的群号。
            """

    @overload
    def unmute_all(self) -> __UnmuteAllProxy:
        """解除全体禁言。"""

    @overload
    async def unmute_all(self, target: int) -> Response:
        """解除全体禁言。

            target (`int`): 指定群的群号。
        """

    # UploadImage

    class __UploadImageProxy():
        async def set(
            self, type: Literal['friend', 'group', 'temp'], img: Union[str,
                                                                       Path]
        ) -> Image:
            """图片文件上传。

                type (`Literal['friend','group','temp']`): 上传的图片类型。

                img (`Union[str,Path]`): 上传的图片的本地路径。
            """

    @overload
    def upload_image(self) -> __UploadImageProxy:
        """图片文件上传。"""

    @overload
    async def upload_image(
        self, type: Literal['friend', 'group', 'temp'], img: Union[str, Path]
    ) -> Image:
        """图片文件上传。

            type (`Literal['friend','group','temp']`): 上传的图片类型。

            img (`Union[str,Path]`): 上传的图片的本地路径。
        """

    # UploadVoice

    class __UploadVoiceProxy():
        async def set(
            self, type: Literal['group'], voice: Union[str, Path]
        ) -> Voice:
            """语音文件上传。

                type (`Literal['group']`): 上传的语音类型。

                voice (`Union[str,Path]`): 上传的语音的本地路径。
            """

    @overload
    def upload_voice(self) -> __UploadVoiceProxy:
        """语音文件上传。"""

    @overload
    async def upload_voice(
        self, type: Literal['group'], voice: Union[str, Path]
    ) -> Voice:
        """语音文件上传。

            type (`Literal['group']`): 上传的语音类型。

            voice (`Union[str,Path]`): 上传的语音的本地路径。
        """
