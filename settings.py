# -*- coding: utf-8 -*-
# @File  : settings.py
# @Author: AaronJny
# @Date  : 2019/10/29
# @Desc  :

# 训练epochs数量
EPOCHS = 3
# 训练批大小
BATCH_SIZE = 128
# 输入的连续时间序列长度
MAX_STEPS = 256
# 前区号码种类数
FRONT_VOCAB_SIZE = 33
# 后区号码种类数
BACK_VOCAB_SIZE = 16
# dropout随机失活比例
DROPOUT_RATE = 0.5
# 长短期记忆网络单元数
LSTM_UNITS = 64
# 前区需要选择的号码数量
FRONT_SIZE = 6
# 后区需要选择的号码数量
BACK_SIZE = 1
# 保存训练好的参数的路径
CHECKPOINTS_PATH = 'checkpoints'
# 预测下期号码时使用的训练好的模型参数的路径，默认使用完整数据集训练出的模型
PREDICT_MODEL_PATH = '{}/model_checkpoint_x'.format(CHECKPOINTS_PATH)
# 预测的时候，预测几注彩票,默认5注
PREDICT_NUM = 5
# 数据集路径
DATASET_PATH = 'lotto.csv'
# 数据集下载地址
LOTTO_DOWNLOAD_URL = "https://e.17500.cn/getData/ssq.TXT"
# 大乐透中奖及奖金规则（没有考虑浮动情况，税前）
AWARD_RULES = {
    (6, 1): 6000000,
    (6, 0): 250000,
    (5, 1): 3000,
    (4, 1): 200,
    (5, 0): 200,
    (4, 0): 10,
    (3, 1): 10,
    (0, 1): 5
}
