# Powered By @AdityaHalder

from typing import Union, List
from pyrogram import filters
from SankiMusic.utilities.config import COMMAND_PREFIXES


#   𝙲𝚘𝚌𝚔𝚃𝚊𝚒𝙻 𝚇 𝙼𝚞𝚜𝚒𝙲
# 0:35 ━❍──────── -5:32
# ↻     ⊲  Ⅱ  ⊳     ↺
#  VOLUME: ▁▂▃▄▅▆▇ 100%

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
