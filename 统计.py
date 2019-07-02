import matplotlib.pyplot as plt #Matplotlib 是 Python 的绘图库，它可与 NumPy 一起使用,方便快捷完成绘图。
from matplotlib.ticker import FuncFormatter, MaxNLocator
from matplotlib.font_manager import FontProperties
list1 = []#各个省份211工程数量的统计列表

#统计211工程大学数量的函数定义
def tongji(s):#文件名作为参数传入函数内部
    file = open(s, 'r')#read模式读取s文件
    lines = file.readlines()#readlines() 读取后得到的是每行数据组成的列表，但是一行样本数据全部存储为一个字符串
    file.close()#关闭文件，取消与文件的关联
    row = []  # 定义行数组
    column = []  # 定义列数组
    for line in lines:
       row.append(line.split(','))#逐行数据加在row列表中，并用“，”隔开
    # 打印第二列数组
    for col in row:
        column.append(col[1])#将第二列数据加在column列表中
    n = 0#n用来记录每个省份（每个csv文件）中的211工程大学的数量
    for j in range(len(column)):#len函数用来得到列表的长度，range（）中的里面要是常数
#这里要注意：由于爬取的csv文件第二列中的211工程大学有三种格式，所以要有以下三个判断语句
        if column[j] == '"211工程':
            n += 1
        elif column[j] == '211工程\n':
            n += 1
        elif column[j] == '211工程，985高校\n':
            n += 1
    list1.append(n)#将本文件中的211工程大学数量加在list1列表后面
    print(list1)

#主函数
def main():
    province_list = ['北京市.csv', '上海市.csv', '江苏省.csv', '陕西省.csv', '湖北省.csv', '四川省.csv', '辽宁省.csv',
                     '黑龙江省.csv', '广东省.csv', '天津市.csv', '湖南省.csv', '安徽省.csv', '山东省.csv',
                     '新疆维吾尔自治区.csv', '重庆市.csv', '吉林省.csv', '福建省.csv', '河北省.csv', '山西省.csv', '内蒙古自治区.csv',
                     '浙江省.csv', '江西省.csv', '河南省.csv', '广西壮族自治区.csv', '云南省.csv', '贵州省.csv',
                     '甘肃省.csv', '海南省.csv', '宁夏回族自治区.csv', '青海省.csv', '西藏自治区.csv'
                     ]
    provincename_list = ['京', '沪', '苏', '陕', '鄂', '川', '辽',
                     '黑', '粤', '津', '湘', '皖', '鲁',
                     '新', '渝', '吉', '闽', '冀', '晋', '蒙',
                     '浙', '赣', '豫', '桂', '云', '贵',
                     '甘', '琼', '宁', '青', '藏'
                     ]#由于画图表避免字符重叠，故用省份简称
    for i in range(len(province_list)):
        tongji(province_list[i])  # 执行len(province_list)次"tongji函数"
# 至此第一部分即统计功能完成，统计的各省份211工程大学的数量存在list1列表中


# 以下是画图表算法：（用到matplotlib.pyplot库函数）
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）使下表中的lable汉化

    # 画柱形图
    def autolabel(rects):  # 定义自动计算注释间距的函数autolabel()
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2. - 0.2, 1.03 * height, '%s' % int(height))
            # text为matplotlib.pyplot添加文字信息函数

    plt.ylabel("数量")  # 设y轴即纵坐标的坐标名称
    plt.xlabel("省份")  # 设y轴即纵坐标的坐标名称
    plt.title("条形统计表")  # 设标题名称
    autolabel(plt.bar(range(len(list1)), list1, color='rgb', tick_label=provincename_list))  # 调用autolabel函数，为柱形图添加文字信息
    plt.show()  # 调用matplotlib.pyplot自带的显示图表函数show()，即可实现柱形图的可视化

    # 画饼状图
    plt.axes(aspect=1)  # 每个Axes对象都是一个拥有自己坐标系统的绘图区域
    plt.pie(x=list1, labels=provincename_list, autopct='%3.1f %%')  # pie函数是用来绘制饼状图的库函数
    plt.title('饼状统计图')  # 为饼状图添加标题的title函数
    plt.show()  # 调用matplotlib.pyplot自带的显示图表函数show()，即可实现饼状图的可视化


    # 折线图

    # 此处附上figure函数具体使用方法（由于我不会，第一次看了好久）
    # figure语法及操作：
    # figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
    # num: 图像编号或名称，数字为编号 ，字符串为名称
    # figsize: 指定figure的宽和高，单位为英寸；
    # dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80       1英寸等于2.5cm, A4纸是21 * 30cm的纸张 
    # facecolor: 背景颜色
    # edgecolor: 边框颜色
    # frameon: 是否显示边框

    fig = plt.figure(figsize=(8, 6))  # 设置画布尺寸
    ax = fig.add_subplot(111)  # 建立对象

    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'cc', 'd', 'e', 'f', 'g', 'h', '*%$', '20']

    def format_fn(tick_val, tick_pos):
        if int(tick_val) in provincename_list:
            return labels[int(tick_val)]
        else:
            return ''

    ax.xaxis.set_major_formatter(FuncFormatter(format_fn))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # 可指定计算机内的任意字体，size为字体大小
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)  # 给matplotlib添加中文字体，运用计算机内自带的字体
    plt.title(u"211工程大学分布折线统计图", fontproperties=font1)
    plt.xlabel(u"省份（同条形）", fontproperties=font1)
    plt.ylabel(u"数量", fontproperties=font1)

    plt.plot(provincename_list, list1, 'o-', label=u"线条")  # plot为matlab中二维线画图函数
    # legend函数的基本用法是：
    # legend(string1, string2, string3, ...)的作用是：
    # 分别将字符串1、字符串2、字符串3……标注到图中，每个字符串对应的图标为画图时的图标。
    ax.legend(prop=font1, loc="upper right")  # 通过ax对象调用legend函数
    plt.show()  # 调用matplotlib.pyplot自带的显示图表函数show()，即可实现饼状图的可视化
    plt.savefig("temp.png")  # 保存图片为"temp.png"

# 主函数运行
if __name__ == "__main__":
    main()
    import thanks               #调用同一文件夹里面的另一个绘图程序

