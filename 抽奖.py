import random
#seed作为指定种子确保数据唯一性
#由当天日期+当天上证指数收盘/深成指数/创业板指小数点后两位+当天福彩3D号码共同决定
random.seed(20200808112233444)
print('代码编号(唯一值验证)',random.randint(111111111,999999999))
#生成从1-200的list序列，步长为1 [1,201)
list=list(range(1,201,1))
print('本次有效序号个数',len(list))
#将一个列表中的元素打乱,根据种子打乱顺序将唯一
random.shuffle(list)
#查询指定序号在随机排中的位置
l=112
print('查询的序号'+str(l)+'对应的位置',list.index(l)+1)
#结果展示
print('一等奖3个',sorted(list[0:3]))
print('二等奖10个',sorted(list[3:13]))
print('三等奖12个',sorted(list[13:25]))
print('四等奖25个',sorted(list[25:50]))
print('五等奖51个',sorted(list[50:101]))
print('本次抽奖的机排顺序:', list)
