# -*- encoding: utf-8 -*-
'''
   ____     __    _           ____    _____    ____     _                           __
  / __ \   / /   (_) _   __  / __ \  / ___/   / __ \   (_)   ____    ____ _ ____   / /_   ___    ____
 / / / /  / /   / / | | / / / / / /  \__ \   / / / /  / /   / __ \  / __ `//_  /  / __ \ / _ \  / __ \
/ /_/ /  / /   / /  | |/ / / /_/ /  ___/ /  / /_/ /  / /   / / / / / /_/ /  / /_ / / / //  __/ / / / /
\____/  /_/   /_/   |___/  \____/  /____/  /_____/  /_/   /_/ /_/  \__, /  /___//_/ /_/ \___/ /_/ /_/
                                                                  /____/
@File      :   OlivOSDingzhen.main.py
@Author    :   Cute_CAT
@Contact   :   2971504919@qq.com
'''
import json
import OlivOS
import OlivOSDingzhen
import requests


class Event(object):
    def init(plugin_event, Proc):
        pass

    def private_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)

    def group_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)

    def save(plugin_event, Proc):
        pass

def deleteBlank(str):
    str_list = list(filter(None,str.split(" ")))
    return str_list

def unity_reply(plugin_event, Proc):
    command_list = deleteBlank(plugin_event.data.message)
    if command_list[0] == '一眼丁真':
        try:
            Dingzhen_api = requests.get('https://api.aya1.top/randomdj?r=0')
            Dingzhen_json = json.loads(Dingzhen_api.text)
            plugin_event.reply('[OP:image,file=' + Dingzhen_json['url'] + ']')
        except Exception as e:
            plugin_event.reply('请求失败了喵')

