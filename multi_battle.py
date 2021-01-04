# 基于类class以及类的继承实现的多人对战小游戏

import time
import random


class WeGame(object):
    def __init__(self, username, sex, boold_num=2000, money=800, agg=0, pre=0):
        self.username = username
        self.sex = sex
        self.boold_num = boold_num
        self.money = money
        self.agg = agg
        self.pre = pre
        self.room = None
        self.Sword_info = []
        self.Sword()

    # def __new__(cls, *args, **kwargs):
    #     return cls.Come_game(cls)

    # 初始金币
    def Come_game(self):
        print("答题得金币，题号有【1、2、3】")
        _num = input("请输入你想答得题目（谨慎选择！！！）：")
        if _num == '1':
            print("斐波拉契数列的第20位是多少？")
            tmp1 = input("你的答案：")
            if tmp1 == '6765':
                self.money += 600
            else:
                self.money += 0
                print("回答错误，答案是6765")
            print("你的金币为：", self.money)
            return self.Sword()

        elif _num == '2':
            print("英雄联盟中召唤师峡谷的战役中，双方都分有几个位置？")
            tmp2 = input("你的答案：")
            if tmp2 == '5':
                self.money += 600
            else:
                self.money += 0
                print("回答错误，答案是5")
            print("你的金币为：", self.money)
            return self.Sword()

        elif _num == '3':
            print("1+1等于几？")
            tmp3 = input("你的答案：")
            if tmp3 == '2':
                self.money += 600
            else:
                print("你没救了！")
                self.money -= 600
            print("你的金币为：", self.money)
            return self.Sword()

    # 武器装备信息
    def Sword(self):
        print('_' * 50)
        print('*' * 50)
        print("剑铺：2019/1/13剑铺开张！（七剑下天山）\n"
              "武器信息：\n"
              "莫问剑：【功】：90，【守】：15，【价】：800￥\n"
              "游龙剑：【功】：95，【守】：5 ，【价】：700￥\n"
              "青干剑：【功】：70，【守】：20，【价】：600￥\n"
              "竞星剑：【功】：80，【守】：10，【价】：600￥\n"
              "日月剑：【功】：85，【守】：5 ，【价】：600￥\n"
              "舍神剑：【功】：85，【守】：5 ，【价】：600￥\n"
              "天瀑剑：【功】：90，【守】：0 ，【价】：600￥\n")
        print('_' * 50)
        print('*' * 50)

        """
        进入剑铺购买相关的武器，金币足够可以购买多把武器
        按e退出剑铺
        """
        while True:
            print("-"*50)
            print("$_$金币足够可以购买多把武器按e或者exit退出剑铺$_$")
            ret = input("$你$想$购$买$的$武$器$是$：")
            print("-"*50)
            if ret == '莫问剑':
                if self.money >= 800:
                    self.agg += 90
                    self.pre += 15
                    self.money -= 800
                    print(f"背包：攻击力《{self.agg}》|防御力《{self.pre}》|血量《{self.boold_num}》|金币《{self.money}》")
                    self.Sword_info.append(ret)


                else:
                    print("金币不足！！！，可按1进入答题充值")
                    ret2 = input("输入1进入答题，输入exit退出：")
                    if ret2 == '1':
                        self.Come_game()
                    elif ret2 == 'exit' or 'e':
                        exit()


            elif ret == '游龙剑':
                if self.money >= 700:
                    self.agg = 95
                    self.pre = 5
                    self.money -= 700
                    print("背包：攻击力《{}》|防御力《{}》|血量《{}》|金币《{}》".format(self.agg, self.pre, self.boold_num, self.money))
                    self.Sword_info.append(ret)
                else:
                    print("金币不足！！！，可按1进入答题充值")
                    ret2 = input("输入1进入答题，输入exit退出：")
                    if ret2 == '1':
                        self.Come_game()
                    elif ret2 == 'exit' or 'e':
                        print()
                        exit()

            elif ret == '青干剑':
                if self.money >= 600:
                    self.agg += 70
                    self.pre += 20
                    self.money -= 600
                    print(f"背包：攻击力《{self.agg}》|防御力《{self.pre}》|血量《{self.boold_num}》|金币《{self.money}》")
                    self.Sword_info.append(ret)
                else:
                    print("金币不足！！！，可按1进入答题充值")
                    ret2 = input("输入1进入答题，输入exit退出：")
                    if ret2 == '1':
                        self.Come_game()
                    elif ret2 == 'exit':
                        exit()

            elif ret == '竞星剑':
                if self.money >= 600:
                    self.agg += 80
                    self.pre += 10
                    self.money -= 600
                    print(f"背包：攻击力《{self.agg}》|防御力《{self.pre}》|血量《{self.boold_num}》|金币《{self.money}》")
                    self.Sword_info.append(ret)
                else:
                    print("金币不足！！！，可按1进入答题充值")
                    ret2 = input("输入1进入答题，输入exit退出：")
                    if ret2 == '1':
                        self.Come_game()
                    elif ret2 == 'exit':
                        exit()

            elif ret == '日月剑':
                if self.money >= 600:
                    self.agg += 85
                    self.pre += 5
                    self.money -= 600
                    print(f"背包：攻击力《{self.agg}》|防御力《{self.pre}》|血量《{self.boold_num}》|金币《{self.money}》")
                    self.Sword_info.append(ret)
                else:
                    print("金币不足！！！，可按1进入答题充值")
                    ret2 = input("输入1进入答题，输入exit退出：")
                    if ret2 == '1':
                        self.Come_game()
                    elif ret2 == 'exit':
                        exit()

            elif ret == '舍神剑':
                if self.money >= 600:
                    self.agg += 85
                    self.pre += 5
                    self.money -= 600
                    print(f"背包：攻击力《{self.agg}》|防御力《{self.pre}》|血量《{self.boold_num}》|金币《{self.money}》")
                    self.Sword_info.append(ret)
                else:
                    print("金币不足！！！，可按1进入答题充值")
                    ret2 = input("输入1进入答题，输入exit退出：")
                    if ret2 == '1':
                        self.Come_game()
                    elif ret2 == 'exit':
                        exit()

            elif ret == '天瀑剑':
                if self.money >= 600:
                    self.agg = 90
                    self.pre = 5
                    self.money -= 600
                    print(f"背包：攻击力《{self.agg}》|防御力《{self.pre}》|血量《{self.boold_num}》|金币《{self.money}》")
                    self.Sword_info.append(ret)
                else:
                    print("金币不足！！！，可按1进入答题充值")
                    ret2 = input("输入1进入答题，输入exit退出：")
                    if ret2 == '1':
                        self.Come_game()
                    elif ret2 == 'exit':
                        exit()

            elif ret == 'e':
                print("本次购买完毕，退出剑铺！")
                break

            else:
                print("没有这把剑，真j!")
                continue

            all_sword = [i for i in self.Sword_info]
            print("||{}||:你的武器库中有{}把剑：{}".format(self.username, len(self.Sword_info), all_sword))

    # 战斗
    # def Battle(self, obj1):
    def Battle(self, obj):
        if self.room != None and self.room == obj.room:
            obj.boold_num = obj.boold_num - self.agg + obj.pre
            time.sleep(random.randint(1, 2))

            print("++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            print(f"{self.username})-=>{obj.username}|{self.username}血量:{self.boold_num}|{obj.username}血量:{obj.boold_num}\n")
            print("+" * 50)

        else:
            print("两个人不在同一个房间")

#####################################################################
# _____________________________________________________________________
#####################################################################

class Room(object):
    MAX = 2

    def __init__(self, room_name, ):
        # self.room_id = "0"
        self.room_name = room_name
        self.room_users = {}

        # key => username, value => user_object instance

    # 这里是玩家加入，加入房间后记录相关信息，存入字典中
    def join(self, user_obj):
        self.room_users[user_obj.username] = user_obj
        print(self.room_users)
        user_obj.room = self.room_name

        # 当玩家数达到房间上限时，自动启动游戏开始的方法
        if len(self.room_users) == Room.MAX:
            print("房间已满！")
            self.Game_start()

        # 设置满员后，禁止再有玩家加入
        # 在room_users字典中删除，使得长度为2，可调用游戏开始Game_start的方法
        elif len(self.room_users) == Room.MAX + 1:
            print("房间已满！禁止加入")
            self.room_users.pop(user_obj.username)

    # 游戏开始：
    def Game_start(self):
        user1 = list(self.room_users.values())[0]
        user2 = list(self.room_users.values())[1]


        """进入到游戏开始方法时：可在输入框输入【y或者n】来控制是否开始战斗
        y:开始战斗
        n:退出游戏"""
        ret = input("是否开始战斗？y:开始，n:退出").upper()
        if ret == 'Y':
            while True:
                if user1.boold_num > 0 and user2.boold_num > 0:

                    """设置两人对战随机进攻的机制，
                    导入random模块，
                    随机出现单数和双数来决定是谁来攻击谁"""
                    if random.randint(1, 4) % 2 == 0:
                        user1.Battle(user2)
                        # print(f"{p1.username})->{p2.username}---{p2.username}血量剩余{p2.boold_num}")
                    elif random.randint(1, 4) % 2 == 1:
                        user2.Battle(user1)
                        # print(f"{p1.username})->{p2.username}---{p2.username}血量剩余{p2.boold_num}")

                # 当有一方的血量小于等于0时，则游戏结束
                else:
                    if user1.boold_num <= 0:
                        print(f"{user2.username}赢得范闲！")

                    if user2.boold_num <= 0:
                        print(f"{user1.username}赢得范闲！")
                    break

        elif ret == 'N':
            exit()
        else:
            print("输入有误，重新输入！")
            self.Game_start()


if __name__ == '__main__':
    import random

    p1 = WeGame('林婉儿', 'm')
    room1 = Room("醉仙居")
    room1.join(p1)
    print("所在房间：", p1.room)
    print("&" * 50)

    p2 = WeGame('司理理', 'm')
    room1.join(p2)
    print("所在房间：", p2.room)
    print("&" * 50)
