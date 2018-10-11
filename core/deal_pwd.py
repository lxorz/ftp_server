# -*- coding:utf-8 -*-
# Author: LiuXing 
# date: 9/28/2018 10:40 PM

import json
from conf import settings


def server_deal_pwd(self, *args):
    """ 用来处理客户端查看当前目录下的请求"""
    cmd_dic = args[0]
    msg_dic = {
        "current_path":self.current_path,
        "cmd_state":settings.LOGIN_STATE["cmd_right"]
    }
    self.request.send(json.dumps(msg_dic).encode())