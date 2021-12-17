from random import choice
from cqhttp import CQHttp
import random

bot = CQHttp(api_root='http://127.0.0.1:5700/')

# print(bot.get_login_info())
# bot.send_private_msg(user_id=834421194, message='hello')


@bot.on_message
def handle_msg(event):
    if '拳师' in event['message']:
        cluster = [
            '拳师？我是拳师！我给你两拳！[CQ:face,id=11][CQ:face,id=11][CQ:face,id=11]', '拳师扎不多得勒']
        content = choice(cluster)
        bot.send(event, content)
        bot.set_group_ban(group_id = event['group_id'], user_id = event['user_id'], duration = 60)
        bot.send(event, '先送你一个禁言大礼包！')
    elif '呃呃' in event['message']:
        bot.send(event, '呃呃')
    elif event['message'] == '早':
        cluster = ['早', '懒狗[CQ:face,id=20]']
        content = choice(cluster)
        bot.send(event, content)
    elif '如何评价' in event['message']:
        cluster = ['不好评价', '我的评价是寄']
        content = choice(cluster)
        bot.send(event, content)
    elif ('晚安' in event['message']) or ('睡' in event['message']):
        cluster = ['晚安', '起来嗨！']
        content = choice(cluster)
        bot.send(event, content)
    elif ('67' in event['message']) or ('🦈' in event['message']):
        cluster = ['67是傻逼', '🦈指导是傻逼']
        content = choice(cluster)
        bot.send(event, content)
    elif '[CQ:face,id=26]' in event['message']:
        cluster = [
            '[CQ:face,id=26][CQ:face,id=26][CQ:face,id=26]', '[CQ:face,id=26]']
        content = choice(cluster)
        bot.send(event, content)
    elif '[CQ:face,id=5]' in event['message']:
        cluster = [
            '[CQ:face,id=5][CQ:face,id=5][CQ:face,id=5]', '[CQ:face,id=5]']
        content = choice(cluster)
        bot.send(event, content)
    elif '[CQ:face,id=20]' in event['message']:
        cluster = [
            '[CQ:face,id=20][CQ:face,id=20][CQ:face,id=20]', '[CQ:face,id=20]']
        content = choice(cluster)
        bot.send(event, content)
    elif ('a上去' in event['message']) or ('A上去' in event['message']):
        bot.send(event, '🐱指导快A上去！[CQ:at,qq=2385324155]')
    elif ('gn' in event['message']) or ('楠' in event['message']) or ('蝻' in event['message']) or ('国男' in event['message']):
        cluster = [
            'gn是这样的', '郭楠是这样的', '蝈蝻是这样的']
        content = choice(cluster)
        bot.send(event, content)
    elif '开导' in event['message']:
        bot.send(event, '积回去！')
    elif '好好好' in event['message']:
        cluster = [
            '好好好', '好好好！']
        content = choice(cluster)
        bot.send(event, content)
    elif '赢' in event['message']:
        bot.send(event, '真是秦始皇触电——赢麻了！')
    elif ('蚌' in event['message']) or ('绷' in event['message']):
        cluster = [
            '蚌', '绷', '蚌埠住了', '绷不住了']
        content = choice(cluster)
        bot.send(event, content)
    elif '破防' in event['message']:
        cluster = [
            '破你🐎', '破防啦']
        content = choice(cluster)
        bot.send(event, content)
    elif '想她' in event['message']:
        cluster = [
            '不如想我', '别想了，快睡吧']
        content = choice(cluster)
        bot.send(event, content)
    elif '真的' in event['message']:
        bot.send(event, '一眼顶针')
    elif '喜欢我' in event['message']:
        bot.send(event, '普信男🤢')
    elif '🤢' in event['message']:
        bot.send(event, '🤢🤢🤢')
    elif '捏' in event['message']:
        bot.send(event, event['message'])
    elif ('🐱' in event['message']) or ('猫' in event['message']):
        cluster = [
            '🐱就是典型的gn', '真下头🤢']
        content = choice(cluster)
        bot.send(event, content)
    elif ('细说' in event['message']) or ('细嗦' in event['message']) or ('细🔒' in event['message']):
        cluster = [
            '细说', '细嗦', '细🔒']
        content = choice(cluster)
        bot.send(event, content)
    elif '[CQ:face,id=193]' in event['message']:
        cluster = [
            '[CQ:face,id=193][CQ:face,id=76]', '[CQ:face,id=193][CQ:face,id=77]']
        content = choice(cluster)
        bot.send(event, content)
    elif ('我超' in event['message']) or ('我焯' in event['message']):
        cluster = [
            'supermarket你', '超市你']
        content = choice(cluster)
        bot.send(event, content)
    elif '🐟' in event['message']:
        bot.send(event, '🐟是大帅哥！[CQ:at,qq=all]')
    elif ('🤖' in event['message']) or ('机器人' in event['message']):
        bot.send(event, '喊你爹干嘛？')
        bot.send(event, '[CQ:face,id=326,type=sticker]')
    elif ('？' in event['message']) or ('?' in event['message']):
        cluster = [
            '？', '', '', '']
        content = choice(cluster)
        bot.send(event, content)
    return 0


bot.run(host='127.0.0.1', port=5701, debug=True)
