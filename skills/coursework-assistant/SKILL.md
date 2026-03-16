# 📝 课程作业/项目完成助手 (Coursework Assistant)

## 技能描述

专为大学生课程作业设计的多功能助手 Skill。无论是论文写作、代码编程、PPT 展示还是小组协作，都能提供全方位支持，帮助学生高效完成各类课程作业和项目。

## 适用场景

| 细分场景 | 场景描述 |
|----------|----------|
| 论文类作业 | 课程论文、读书报告、文献综述等文字作业 |
| 代码类作业 | 编程作业、课程设计、算法题等 |
| 展示类作业 | PPT 汇报、演讲展示、视频制作等 |
| 小组作业协调 | 多人合作完成作业，需要分工协作 |

## 核心能力

### 1. 论文写作指导
- 论文结构框架设计
- 各章节写作要点
- 文献检索与引用
- 查重降重技巧
- 格式规范检查

### 2. 代码作业辅导
- 代码思路讲解
- 代码实现示例
- Debug 调试指导
- 代码优化建议
- 注释规范编写

### 3. PPT 展示设计
- PPT 结构大纲
- 内容精简提炼
- 设计排版建议
- 演讲逐字稿
- 时间把控技巧

### 4. 小组协作管理
- 任务分工方案
- 进度跟踪表
- 沟通协调建议
- 冲突解决方法
- 成果整合指导

## 使用示例

### 示例 1：论文类作业

```
用户：我要写一篇 3000 字的课程论文，题目是"人工智能对教育的影响"，怎么写？

我会生成：

# 📖 课程论文写作指南

## 📋 论文框架（3000 字）

### 摘要（200 字）
- 研究背景
- 研究目的
- 主要观点
- 结论

### 一、引言（400 字）
1.1 研究背景
- AI 技术发展现状
- 教育领域变革需求

1.2 研究意义
- 理论意义
- 实践价值

1.3 论文结构

### 二、人工智能在教育中的应用（800 字）
2.1 智能辅导系统
- 个性化学习路径
- 即时反馈机制

2.2 智能评测系统
- 自动批改
- 学习诊断

2.3 教学管理优化
- 排课系统
- 学生管理

### 三、人工智能对教育的影响（800 字）
3.1 积极影响
- 提升学习效率
- 促进教育公平
- 减轻教师负担

3.2 挑战与问题
- 技术依赖风险
- 隐私安全问题
- 教师角色转变

### 四、对策与建议（600 字）
4.1 技术层面
4.2 政策层面
4.3 教师发展

### 五、结论（200 字）
- 主要观点总结
- 研究局限
- 未来展望

### 参考文献（10-15 篇）

## 🔍 文献检索建议

### 中文数据库
- 中国知网（CNKI）
- 万方数据
- 维普期刊

### 搜索关键词
- "人工智能 + 教育"
- "AI+ 教学"
- "智能教育"
- "教育信息化"

### 推荐文献
1. 祝智庭。智慧教育：教育信息化的新境界 [J]. 电化教育研究
2. 杨现民。人工智能时代的教育变革 [J]. 开放教育研究

## ✍️ 写作技巧

### 摘要写作
> 先写正文，最后写摘要
> 包含：背景 + 目的 + 方法 + 结论

### 正文写作
> 每段一个中心思想
> 段首点明观点
> 用数据/案例支撑

### 降低查重率
1. 理解后用自己的话重述
2. 调整句子结构（主动变被动）
3. 同义词替换
4. 增加自己的分析和评论

## 📐 格式规范

### 字体字号
- 标题：黑体三号
- 一级标题：黑体四号
- 正文：宋体小四
- 行距：1.5 倍

### 引用格式（GB/T 7714）
> 期刊：[序号] 作者。题名 [J]. 期刊名，年，卷 (期): 起止页码.
> 书籍：[序号] 作者。书名 [M]. 出版地：出版社，出版年.

## ⏰ 写作时间建议

| 阶段 | 时间 | 任务 |
|------|------|------|
| 资料收集 | 1-2 天 | 查找文献，阅读整理 |
| 提纲撰写 | 半天 | 确定框架，细化到三级标题 |
| 初稿写作 | 2-3 天 | 按章节完成初稿 |
| 修改润色 | 1 天 | 修改逻辑，润色文字 |
| 格式调整 | 半天 | 调整格式，检查引用 |
```

### 示例 2：代码类作业

```
用户：Python 作业，要写一个学生成绩管理系统，怎么做？

我会生成：

# 💻 学生成绩管理系统 - 代码实现

## 📋 功能需求分析

### 基本功能
1. 添加学生信息
2. 删除学生信息
3. 修改学生信息
4. 查询学生信息
5. 录入成绩
6. 计算平均分/排名
7. 保存数据到文件

## 🏗️ 代码结构

```
student_system/
├── main.py          # 主程序入口
├── student.py       # 学生类定义
├── manager.py       # 管理类
├── utils.py         # 工具函数
└── data.txt         # 数据存储
```

## 📝 核心代码实现

### student.py - 学生类

```python
class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.scores = {}  # {课程名：分数}
    
    def add_score(self, course, score):
        """添加成绩"""
        self.scores[course] = score
    
    def get_average(self):
        """计算平均分"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)
    
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.age}\t{self.get_average():.1f}"
```

### manager.py - 管理类

```python
class StudentManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student):
        """添加学生"""
        self.students[student.id] = student
    
    def delete_student(self, student_id):
        """删除学生"""
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
    
    def find_student(self, student_id):
        """查找学生"""
        return self.students.get(student_id)
    
    def show_all(self):
        """显示所有学生"""
        print("ID\t姓名\t年龄\t平均分")
        for student in self.students.values():
            print(student)
    
    def save_to_file(self, filename):
        """保存到文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            for student in self.students.values():
                f.write(f"{student.id},{student.name},{student.age}\n")
```

### main.py - 主程序

```python
from student import Student
from manager import StudentManager

def main():
    manager = StudentManager()
    
    while True:
        print("\n=== 学生成绩管理系统 ===")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 查询学生")
        print("4. 录入成绩")
        print("5. 显示所有")
        print("6. 保存数据")
        print("0. 退出")
        
        choice = input("请选择：")
        
        if choice == '1':
            id = input("学号：")
            name = input("姓名：")
            age = int(input("年龄："))
            student = Student(id, name, age)
            manager.add_student(student)
            print("添加成功！")
        
        elif choice == '5':
            manager.show_all()
        
        elif choice == '6':
            manager.save_to_file('data.txt')
            print("保存成功！")
        
        elif choice == '0':
            print("再见！")
            break

if __name__ == '__main__':
    main()
```

## 🔧 调试技巧

### 常见问题
1. **文件找不到**：检查文件路径是否正确
2. **编码错误**：打开文件时指定 encoding='utf-8'
3. **类型错误**：输入的数字要转换为 int/float

### 测试建议
```python
# 测试代码
def test():
    manager = StudentManager()
    
    # 添加测试数据
    s1 = Student("001", "张三", 20)
    s1.add_score("Python", 90)
    s1.add_score("数学", 85)
    
    s2 = Student("002", "李四", 21)
    s2.add_score("Python", 88)
    
    manager.add_student(s1)
    manager.add_student(s2)
    
    manager.show_all()
    manager.save_to_file('test.txt')

test()
```

## 📚 扩展功能

1. **按成绩排序**
2. **统计各分数段人数**
3. **图形界面（tkinter）**
4. **数据库存储（SQLite）**
```

### 示例 3：PPT 展示

```
用户：要做 10 分钟的课堂展示，主题是"时间管理方法"，帮我设计 PPT

我会生成：

# 📊 PPT 展示设计

## 📋 PPT 结构（10 分钟，约 10-12 页）

### 第 1 页：封面
- 标题：时间管理方法
- 副标题：让你的一天变成 48 小时
- 姓名/日期

### 第 2 页：目录
1. 为什么需要时间管理
2. 常见时间管理方法
3. 实用工具推荐
4. 行动计划

### 第 3 页：痛点引入
- "你是否有这些困扰？"
- 总是赶 deadline
- 事情太多理不清
- 刷手机停不下来

### 第 4-7 页：核心方法（重点）
- 四象限法则
- 番茄工作法
- GTD 方法
- 时间块规划

### 第 8 页：工具推荐
- 滴答清单
- Forest
- Notion

### 第 9 页：行动计划
- 从今天开始可以做的 3 件事

### 第 10 页：总结 + Q&A

## 🎨 设计建议

### 配色方案
- 主色：蓝色（专业/信任）
- 辅色：橙色（活力/重点）
- 背景：白色或浅灰

### 字体
- 标题：微软雅黑 Bold
- 正文：微软雅黑 Regular
- 字号：标题 32+，正文 18+

### 排版原则
- 每页不超过 6 行
- 每行不超过 15 字
- 多用图表，少用文字

## 📝 演讲逐字稿（开场 1 分钟）

> "大家好，今天我要分享的主题是'时间管理方法'。
> 
> 在开始之前，我想问大家一个问题：
> 有多少人曾经为了赶作业熬过夜？
> （停顿，等举手）
> 
> 我猜大部分人都有过这样的经历。
> 其实不是时间不够用，而是我们没有好好管理它。
> 
> 今天我就给大家介绍几个超实用的时间管理方法，
> 让你的一天变成 48 小时！
> 
> 首先，我们来看看..."

## ⏱️ 时间分配

| 部分 | 时间 |
|------|------|
| 开场引入 | 1 分钟 |
| 方法 1-2 | 3 分钟 |
| 方法 3-4 | 3 分钟 |
| 工具推荐 | 1 分钟 |
| 行动计划 | 1 分钟 |
| 总结 +Q&A | 1 分钟 |
```

### 示例 4：小组作业协调

```
用户：我们 5 个人要做小组作业，怎么分工？

我会生成：

# 👥 小组作业分工方案

## 📋 任务分解

假设是"创业计划书"小组作业：

| 任务模块 | 工作量 | 所需技能 |
|----------|--------|----------|
| 市场调研 | ⭐⭐⭐ | 信息搜集、数据分析 |
| 产品设计 | ⭐⭐ | 创意思维、文档写作 |
| 财务预测 | ⭐⭐⭐ | Excel、财务知识 |
| PPT 制作 | ⭐⭐ | 设计、排版 |
| 演讲展示 | ⭐ | 表达能力 |
| 统稿整合 | ⭐⭐ | 统筹、写作 |

## 👤 人员分工建议（5 人）

### 成员 A（组长）
- 负责：统稿整合 + 财务预测
- 职责：进度跟踪、最终审核

### 成员 B
- 负责：市场调研
- 职责：收集数据、竞品分析

### 成员 C
- 负责：产品设计
- 职责：产品描述、商业模式

### 成员 D
- 负责：PPT 制作
- 职责：美化排版、图表制作

### 成员 E
- 负责：演讲展示
- 职责：撰写讲稿、课堂展示

## 📅 进度管理

### 时间节点
| 阶段 | 截止日期 | 交付物 |
|------|----------|--------|
| 资料收集 | 第 3 天 | 调研文档 |
| 初稿完成 | 第 7 天 | 各模块初稿 |
| 统稿修改 | 第 10 天 | 完整稿 |
| PPT 完成 | 第 12 天 | 最终 PPT |
| 演练 | 第 14 天 | 模拟展示 |

### 沟通方式
- 微信群：日常沟通
- 腾讯会议：每周 1 次进度会
- 石墨文档：在线协作编辑

## ⚠️ 常见问题处理

### 队友不干活怎么办？
1. 私下沟通，了解原因
2. 调整任务，降低难度
3. 向老师反映（最后手段）

### 意见不合怎么办？
1. 投票表决
2. 找中立的第 6 人评判
3. 保留各自版本，让老师选择

### 进度落后怎么办？
1. 增加线上会议频率
2. 简化非核心内容
3. 申请延期（如有正当理由）
```

## 输入格式

```yaml
input:
  assignment_type: string    # 作业类型：论文/代码/PPT/小组
  course_name: string        # 课程名称
  topic: string              # 作业主题/题目
  word_count: number         # 字数要求（论文）
  deadline: string           # 截止日期
  group_size: number         # 小组人数（小组作业）
  requirements: array        # 具体要求列表
```

## 输出格式

```yaml
output:
  framework: object          # 框架/结构设计
  guidelines: array          # 写作/实现指南
  templates: array           # 模板/示例
  tips: array                # 技巧/注意事项
  resources: array           # 推荐资源
  timeline: array            # 时间规划建议
```

## 元数据

```yaml
metadata:
  id: "study-coursework-assistant"
  name: "课程作业/项目完成助手"
  description: "帮助大学生高效完成各类课程作业，包括论文写作、代码编程、PPT 展示和小组协作"
  tags: ["学习", "作业", "论文", "代码", "PPT", "小组"]
  requires: []
  version: "1.0.0"
  author: "SkillHub"
```

## 联动 Skill

完成本 Skill 后，可联动使用：
- 📚 期末突击复习 - 考试复习
- 📝 笔记整理与知识管理 - 整理学习笔记
- 🎯 时间管理与效率提升 - 提高作业效率

---

*本 Skill 由 SkillHub 出品，专为大学生设计*
