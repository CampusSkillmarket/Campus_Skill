# 📊 数据分析专家 (Data Analyst Pro)

## 技能描述
专为大学生和创业者设计的数据分析技能。无论是毕业论文数据分析、市场调研报告还是创业数据看板，都能提供专业级的数据清洗、统计分析、可视化和洞察报告。

## 核心能力

### 1. 数据清洗
- 缺失值处理
- 异常值检测
- 数据格式转换
- 重复值处理
- 数据标准化

### 2. 统计分析
- 描述性统计
- 假设检验
- 相关分析
- 回归分析
- 方差分析

### 3. 数据可视化
- 基础图表（柱状图、折线图、饼图）
- 高级图表（热力图、箱线图、小提琴图）
- 交互式图表（Plotly、ECharts）
- 仪表板设计

### 4. 洞察报告
- 数据解读
- 趋势分析
- 对比分析
- 建议输出

## 常用工具

### Python 库
```python
# 数据处理
import pandas as pd
import numpy as np

# 可视化
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 统计分析
from scipy import stats
from statsmodels.formula.api import ols
```

### Excel
- 数据透视表
- 条件格式
- 图表工具
- 分析工具库

### SQL
```sql
-- 基础查询
SELECT column, COUNT(*) 
FROM table 
GROUP BY column 
HAVING COUNT(*) > 10;

-- 连接查询
SELECT a.*, b.* 
FROM table_a a 
JOIN table_b b ON a.id = b.a_id;

-- 窗口函数
SELECT name, score, 
       RANK() OVER (ORDER BY score DESC) as rank
FROM students;
```

## 使用示例

### 示例 1：毕业论文数据分析
```
用户：我有 200 份问卷数据，帮我分析

数据字段：
- 性别、年龄、专业
- 满意度评分 (1-5 分)
- 使用频率
- 推荐意愿

我会提供：

📊 分析流程

1. 数据清洗
   - 检查缺失值
   - 处理异常值
   - 编码分类变量

2. 描述性统计
   - 样本构成（性别/年龄/专业分布）
   - 各变量均值、标准差

3. 差异分析
   - 不同性别满意度差异 (t 检验)
   - 不同专业满意度差异 (ANOVA)

4. 相关分析
   - 满意度与推荐意愿相关性
   - 使用频率与满意度关系

5. 回归分析
   - 影响满意度的关键因素

📈 可视化输出
- 样本分布饼图
- 满意度分布直方图
- 性别对比箱线图
- 相关性热力图
- 回归拟合图

📝 报告输出
包含：
- 研究方法
- 数据描述
- 分析结果
- 结论建议
```

### 示例 2：电商销售数据分析
```
用户：分析店铺销售数据，找出增长机会

数据：订单表（日期、产品、数量、金额、地区）

我会提供：

🔍 分析维度

1. 整体表现
   - 总销售额、订单量
   - 日均销售、客单价
   - 同比/环比增长率

2. 时间趋势
   - 月度销售趋势
   - 周度销售趋势
   - 日销售时段分布

3. 产品分析
   - 畅销产品 TOP10
   - 滞销产品识别
   - ABC 分类

4. 地区分析
   - 各地区销售占比
   - 增长最快地区
   - 潜力地区识别

5. 用户分析
   - 新老用户占比
   - 复购率
   - RFM 分层

📊 核心图表
- 销售趋势折线图
- 产品销量帕累托图
- 地区销售热力图
- 用户分层饼图

💡 洞察建议
- 加大畅销品库存
- 针对潜力地区投放广告
- 设计复购激励活动
```

### 示例 3：创业数据看板
```
用户：帮我设计一个创业项目的数据看板

项目类型：知识付费平台

我会设计：

📋 核心指标体系

一级指标（北极星指标）
├── 月经常性收入 (MRR)

二级指标
├── 用户获取
│   ├── 新增用户数
│   ├── 获客成本 (CAC)
│   └── 渠道转化率
├── 用户活跃
│   ├── DAU/MAU
│   ├── 日使用时长
│   └── 功能使用率
├── 用户留存
│   ├── 次日留存率
│   ├── 7 日留存率
│   └── 30 日留存率
└── 商业变现
    ├── 付费转化率
    ├── 客单价 (ARPPU)
    └── 用户生命周期价值 (LTV)

📊 看板设计
┌─────────────────────────────────────────────┐
│  MRR: ¥50,000  │  新增：+200  │  留存：45%  │
├─────────────────────────────────────────────┤
│                                             │
│  [MRR 趋势图 - 近 12 个月]                    │
│                                             │
├─────────────────────────────────────────────┤
│  [新增用户趋势]  │  [留存率曲线]            │
├─────────────────────────────────────────────┤
│  [渠道转化对比]  │  [付费用户分布]          │
└─────────────────────────────────────────────┘

📈 Python 实现代码
```python
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 创建 MRR 趋势图
def plot_mrr_trend(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['month'],
        y=df['mrr'],
        mode='lines+markers',
        name='MRR',
        line=dict(color='blue', width=3)
    ))
    fig.update_layout(
        title='MRR 趋势',
        xaxis_title='月份',
        yaxis_title='MRR (元)',
        template='plotly_white'
    )
    return fig

# 创建留存率曲线
def plot_retention_curve(df):
    fig = go.Figure()
    for cohort in df['cohort'].unique():
        cohort_data = df[df['cohort'] == cohort]
        fig.add_trace(go.Scatter(
            x=cohort_data['period'],
            y=cohort_data['retention'],
            name=f'{cohort}期',
            mode='lines+markers'
        ))
    fig.update_layout(
        title='留存率曲线',
        xaxis_title='周期',
        yaxis_title='留存率',
        template='plotly_white'
    )
    return fig
```
```

## 统计方法速查

### t 检验
```python
# 独立样本 t 检验
from scipy import stats
t_stat, p_val = stats.ttest_ind(group1, group2)
print(f"t={t_stat:.3f}, p={p_val:.4f}")
```

### 方差分析
```python
# 单因素方差分析
import statsmodels.api as sm
from statsmodels.formula.api import ols
model = ols('score ~ C(group)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
```

### 相关分析
```python
# Pearson 相关
correlation = df['x'].corr(df['y'])

# 相关矩阵热力图
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
```

### 回归分析
```python
# 线性回归
import statsmodels.api as sm
X = df[['x1', 'x2']]
y = df['y']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
```

## 可视化图表选择指南

| 分析目的 | 推荐图表 |
|----------|----------|
| 比较大小 | 柱状图、条形图 |
| 看趋势 | 折线图、面积图 |
| 看占比 | 饼图、环形图、树图 |
| 看分布 | 直方图、箱线图、小提琴图 |
| 看关系 | 散点图、气泡图、热力图 |
| 看流程 | 漏斗图、桑基图 |
| 看地理 | 地图、热力地图 |

## 报告模板

### 数据分析报告结构
```markdown
# [项目名称] 数据分析报告

## 1. 执行摘要
- 核心发现（3-5 点）
- 关键建议

## 2. 研究背景
- 分析目的
- 数据来源
- 样本说明

## 3. 数据概况
- 数据量
- 时间范围
- 变量说明

## 4. 分析结果
### 4.1 描述性分析
[图表 + 文字解读]

### 4.2 差异分析
[图表 + 文字解读]

### 4.3 相关/回归分析
[图表 + 文字解读]

## 5. 结论与建议
- 主要结论
- 行动建议
- 后续研究方向

## 附录
- 详细数据表
- 技术细节
```

## 使用提示

1. **提供数据文件**：Excel/CSV/数据库
2. **说明分析目的**：探索/验证/预测
3. **指定输出格式**：报告/图表/代码
4. **补充背景信息**：行业/业务场景

## 注意事项

- 数据隐私保护
- 异常值谨慎处理
- 相关≠因果
- 样本代表性
- 多重检验校正
