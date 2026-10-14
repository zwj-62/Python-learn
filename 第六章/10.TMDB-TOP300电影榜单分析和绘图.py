import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

# 全局字体设置：使用黑体显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题


def load_data(path: str = 'data/movies.csv') -> pd.DataFrame:
    """读取电影数据，并对年份缺失做处理。

    只保留分析需要的列，年份强制转为支持空值的 Int64 类型，
    若年份缺失则从"上映时间"的前 4 位补齐。
    """
    data = pd.read_csv(
        path,
        usecols=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言"],
        dtype={'年份': 'Int64'}  # int64 不支持空值，Int64 支持空值
    )
    # 抓取的数据可能有年份丢失，用上映时间的年份补齐
    data['年份'] = data['年份'].fillna(data['上映时间'].str[0:4])
    return data


def plot_year_trend(ax: Axes, data: pd.DataFrame) -> None:
    """需求一：统计每年上映电影数量，用折线图表示。"""
    year_count = data.groupby('年份')['年份'].count()

    # 组装 x 轴（连续的年份区间）与 y 轴（对应数量，缺失年份补 0）
    min_year = int(year_count.index.min())
    max_year = int(year_count.index.max())
    x = [i for i in range(min_year, max_year + 1)]
    y = [year_count.get(i, 0) for i in x]

    ax.plot(x, y)
    ax.set_title('每年电影数量折现统计表', fontsize=15)
    ax.set_xlabel('年份', fontsize=15)
    ax.set_xticks(x[::5])
    ax.set_ylabel('数量（个）', fontsize=15)
    ax.set_yticks([i for i in range(0, 11, 1)])
    ax.grid(linestyle='--', alpha=0.5)


def plot_language_count(ax: Axes, data: pd.DataFrame) -> None:
    """需求二：统计对比不同语言的电影数量，用柱状图表示。"""
    language_count = data.groupby('语言')['语言'].count().sort_values(ascending=False)

    x_language = language_count.index.tolist()  # 索引（语言名）转列表
    y_language_count = language_count.values.tolist()  # 数据（数量）转列表

    ax.bar(x_language, y_language_count, color='green', width=0.5)
    ax.set_title('不同语言电影数量柱状图', fontsize=15)
    ax.set_xlabel('语言', fontsize=15)
    ax.set_ylabel('数量', fontsize=15)
    ax.set_yticks(range(0, 131, 10))
    ax.grid(linestyle='-.', alpha=0.5)
    ax.tick_params(axis='x', rotation=45)  # x 轴标签旋转 45°


def plot_type_count(ax: Axes, data: pd.DataFrame) -> None:
    """需求三：统计对比不同电影类型的数量，用柱状图表示。

    一部电影可能包含多个类型（逗号分隔），因此需要拆分后逐个累加计数。
    """
    type_count: dict[str, int] = {}
    for types in data['类型'].str.split(','):  # 例如 ['惊悚', '犯罪']
        for type_name in types:
            type_count[type_name] = type_count.get(type_name, 0) + 1

    x_types = type_count.keys()
    y_types = type_count.values()

    ax.bar(x_types, y_types, color='blue', width=0.5)
    ax.set_title('统计对比不同电影类型的数量', fontsize=15)
    ax.set_xlabel('类型', fontsize=15)
    ax.set_ylabel('数量', fontsize=15)
    ax.set_yticks(range(0, 40, 5))
    ax.grid(linestyle='-.', alpha=0.5)
    ax.tick_params(axis='x', rotation=45)


def plot_score_ratio(ax: Axes, data: pd.DataFrame) -> None:
    """需求四：统计对比各个评分的电影占比，用饼状图表示。"""
    score_count = data.groupby('评分')['评分'].count().sort_values()

    x_score = score_count.index.tolist()
    y_score_count = score_count.values.tolist()

    ax.pie(y_score_count, labels=x_score, autopct='%1.1f%%', startangle=90)
    ax.set_title('统计各个电影评分占比', fontsize=15)
    # loc 控制图例位置，ncol 控制一排展示几个，bbox_to_anchor 控制上下左右位置
    ax.legend(loc='lower center', ncol=8, bbox_to_anchor=(0.5, -0.3), fontsize=10)


def main() -> None:
    """组装 2×2 子图并依次绘制四项统计结果。"""
    data = load_data()

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(20, 15), dpi=100)
    fig.suptitle('TMDB-TOP300电影榜单分析', fontsize=30, x=0.5, y=0.95)
    fig.subplots_adjust(hspace=0.3, wspace=0.3)#这个是调整四个画布的间距之类的

    axes1: Axes = ax[0, 0]
    axes2: Axes = ax[0, 1]
    axes3: Axes = ax[1, 0]
    axes4: Axes = ax[1, 1]

    plot_year_trend(axes1, data)
    plot_language_count(axes2, data)
    plot_type_count(axes3, data)
    plot_score_ratio(axes4, data)

    plt.savefig('data/TMDB-TOP300.png')
    plt.show()


if __name__ == '__main__':
    main()
