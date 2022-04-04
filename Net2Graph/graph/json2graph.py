import os
import json


# 用于高亮打印的颜色
def color_str(txt, foreground = 37, background = 40, font = 1):
    """ 用于设置字符串的样式
        样式选择:
            默认 0   加粗 1  
            划线 4   反显 7
        前景色, 也即字体的颜色:
            黑色 30  红色 31  绿色 32
            黄色 33  蓝色 34  梅色 35
            青色 36  白色 37
        背景色与前景色相差10, 上述数值+10即可得到背景色, 终端彩色字体打印参考博客: 
        https://www.cnblogs.com/huchong/p/7516712.html?msclkid=33069935b37511ecbdb740efceecb354
    """
    C_LT = "\033[{};{};{}m".format(font, foreground, background)
    C_RT = "\033[0m"    
    return str(C_LT + txt + C_RT)


# 相当于C/C++宏定义
CS = color_str
RED, GREEN, YELLOW = 31, 32, 33


# 类别的编号 0 ~ 999
def print_edge(idx):
    ret  = []
    with open("../ag/ag-{}.json".format(idx)) as ag:
        ag_dict = json.load(ag)
    print(CS("│类聚合文件: ag-{}.json".format(idx), RED, font = 7))
    print(CS("│", RED))
    for i, (layer, channel_on_this_layer) in enumerate(ag_dict.items()):
        print(CS(str("┼--当前层: " + layer), RED))
        for channel in channel_on_this_layer:
            
            curr_channel =  channel["channel"]
            prev_channel_list  = channel["prev_channels"]

            branch_prompt = CS("│  " if i!=len(ag_dict) - 1 else "   ", RED)
            print(branch_prompt, CS("│__当前通道: {:>03d}, Page Rank 得分 : {:.5f}, "\
                .format(curr_channel, channel["pagerank"]), GREEN), end = " 连边: ")
            
 
            for prev_chennel in prev_channel_list:
                v = curr_channel
                u = prev_chennel["prev_channel"]
                w = prev_chennel["inf"]
                ret.append((u,v,w))
                print(CS("({:>03d},{:>03d},{:>03d})".format(u, v, w), YELLOW), end = " ")
                
            if len(prev_channel_list) == 0 :
                print(CS("Empty", YELLOW), end = " ")
            print()
        print(CS("│" if i != len(ag_dict) - 1 else "\0", RED))
    return ret



# 获取拿到连边并写入相应文件
def write_edge(idx, edges):
    filename = "../in/in-{}.txt".format(idx)
    with open(filename, "w") as wf:
        wf.write("{}\n".format(len(edges)))
        for (u, v, w) in edges:
           wf.write("{} {} {}\n".format(u,v,w))



# 写入数据的格式: 
# 第一行 连边的数量
# 接下来的每一行是由:  起点, 终点, 权重(连边的影响力) 构成的三元组
if __name__ == "__main__":
    for i in range(1000):
        ag_json_file = "../ag/ag-{}.json".format(i) 
        if os.path.exists(ag_json_file):
            write_edge(i, print_edge(i))

# 如果需要对比受到对抗攻击前后同一个类别的两个特征表达图(Attribution graph)之间的差异,
# 读取两份数据, 建图, 离散化处理, 然后建图, 比较图编辑距离即可!

