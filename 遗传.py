import 基因, 配置
from random import randrange
from random import choice
from random import getrandbits

def 翻译(基因序列):
    处理后基因序列 = 基因序列[0:len(基因序列)//3*3]
    氨基酸序列 = ''
    for 序号 in range(0, len(处理后基因序列)//3*3, 3):
        密码子 = 基因序列[序号] + 基因序列[序号 + 1] + 基因序列[序号 + 2]
        氨基酸序列 += 基因.遗传密码[密码子]
    return 氨基酸序列

def 繁殖(亲代基因序列):
    子代基因序列组 = [亲代基因序列] * 配置.子代个数
    for 序号 in range(0, 配置.子代个数):
        子代基因序列 = list(子代基因序列组[序号])
        碱基位置 = randrange(0, len(子代基因序列))
        子代基因序列[碱基位置] = choice('OX'.replace(子代基因序列[碱基位置], ''))
        子代基因序列组[序号] = ''.join(子代基因序列)
        if len(子代基因序列组[序号]) > 3:
            if getrandbits(1):
                随机位置 = randrange(0, len(子代基因序列组[序号]) + 1)
                子代基因序列组[序号] = 子代基因序列组[序号][:随机位置] + choice('OX') + 子代基因序列组[序号][随机位置:]
            else:
                子代基因序列 = list(子代基因序列组[序号])
                del 子代基因序列[randrange(0,len(子代基因序列组[序号]))]
                子代基因序列组[序号] = ''.join(子代基因序列)
        else:
            随机位置 = randrange(0, len(子代基因序列组[-1]) + 1)
            子代基因序列组[-1] = 子代基因序列组[-1][:随机位置] + choice('OX') + 子代基因序列组[-1][随机位置:]
    return 子代基因序列组


def 差异检测(氨基酸序列):
    产物 = 0
    for 底物 in range(1,101):
        产物 += abs(基因.蛋白质(底物, 氨基酸序列) - 配置.目标蛋白质(底物))
    return 产物 / 100

def 比较(差异值组):
    最小值 = 0
    相同组 = []
    for 序号 in range(len(差异值组) - 1):
        if not 序号:
            最小值 = 差异值组[序号]
            相同组.append(序号)
        if 差异值组[序号] > 差异值组[序号 + 1] and 差异值组[序号 + 1] < 最小值:
            最小值 = 差异值组[序号 + 1]
            相同组 = [序号 + 1]
        elif 差异值组[序号] > 差异值组[序号 + 1] and 差异值组[序号 + 1] == 最小值:
            相同组.append(序号 + 1)
        elif 差异值组[序号] == 差异值组[序号 + 1] and 差异值组[序号 + 1] == 最小值:
            相同组.append(序号 + 1)
    return 相同组, 最小值
