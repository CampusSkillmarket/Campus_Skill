#!/usr/bin/env python3
"""
SkillHub GitHub 仓库结构生成器

生成符合以下结构的文件：
skillhub-skills/
├── README.md              # 总览文档
├── LICENSE
├── study-assistant-pro/   # 每个 Skill 独立文件夹
│   ├── README.md          # 该 Skill 介绍 + 下载链接
│   └── SKILL.md           # Skill 具体内容
└── ...
"""

import os
import shutil
import json
from pathlib import Path

# 源目录和目标目录
SKILLZIP_DIR = Path("/Users/blueblue/skillhub/skillzip")
OUTPUT_DIR = Path("/Users/blueblue/skillhub/github-restructure/skills")

# 32 个技能信息
SKILLS = [
    {"id": "study-assistant-pro", "name": "学业助手 Pro", "category": "学习", "icon": "📚"},
    {"id": "study-assistant", "name": "学业助手", "category": "学习", "icon": "📖"},
    {"id": "coursework-assistant", "name": "课程作业助手", "category": "学习", "icon": "📝"},
    {"id": "final-exam-crash", "name": "期末突击助手", "category": "学习", "icon": "⚡"},
    {"id": "thesis-assistant", "name": "毕业论文助手", "category": "学习", "icon": "🎓"},
    {"id": "cert-exam-prep", "name": "考证备考助手", "category": "学习", "icon": "📜"},
    {"id": "business-plan-generator-pro", "name": "商业计划书生成器", "category": "创业", "icon": "💼"},
    {"id": "business-plan-generator", "name": "商业计划书", "category": "创业", "icon": "📊"},
    {"id": "social-media-copywriter-pro", "name": "社交媒体爆款文案", "category": "创业", "icon": "📱"},
    {"id": "social-media-copywriter", "name": "社交媒体文案", "category": "创业", "icon": "✍️"},
    {"id": "idea-generator", "name": "创意脑暴伙伴", "category": "创业", "icon": "💡"},
    {"id": "campus-micro-startup", "name": "校园微创业助手", "category": "创业", "icon": "🏫"},
    {"id": "hobby-monetization", "name": "爱好变现助手", "category": "创业", "icon": "💰"},
    {"id": "social-media-startup", "name": "自媒体创业助手", "category": "创业", "icon": "🎬"},
    {"id": "career-coach", "name": "求职面试教练", "category": "求职", "icon": "🎯"},
    {"id": "resume-builder", "name": "简历优化师", "category": "求职", "icon": "📄"},
    {"id": "interview-prep", "name": "面试准备助手", "category": "求职", "icon": "🎤"},
    {"id": "job-search", "name": "求职搜索助手", "category": "求职", "icon": "🔍"},
    {"id": "career-planning", "name": "职业规划师", "category": "求职", "icon": "🗺️"},
    {"id": "internship-search", "name": "实习搜索助手", "category": "求职", "icon": "🏢"},
    {"id": "document-master", "name": "文档处理大师", "category": "效率", "icon": "📄"},
    {"id": "word-document-writer", "name": "Word 文档写作助手", "category": "效率", "icon": "📝"},
    {"id": "productivity-toolkit", "name": "效率工具集合", "category": "效率", "icon": "⚡"},
    {"id": "time-management", "name": "时间管理师", "category": "效率", "icon": "⏰"},
    {"id": "social-relationships", "name": "社交关系助手", "category": "效率", "icon": "🤝"},
    {"id": "finance-basics", "name": "理财入门助手", "category": "效率", "icon": "📈"},
    {"id": "web-dev-assistant", "name": "网页开发助手", "category": "开发", "icon": "💻"},
    {"id": "qwen-code-2-skills", "name": "Qwen Code 技能", "category": "开发", "icon": "🤖"},
    {"id": "qwen-code-skill-wrapper", "name": "Qwen Code 包装器", "category": "开发", "icon": "🔧"},
    {"id": "data-analyst-pro", "name": "数据分析专家", "category": "开发", "icon": "📊"},
    {"id": "global-business-assistant", "name": "跨境出海助手", "category": "营销", "icon": "🌍"},
    {"id": "personal-branding", "name": "个人品牌打造师", "category": "营销", "icon": "⭐"},
]


def generate_main_readme():
    """生成总 README.md"""
    
    # 按分类统计
    categories = {}
    for skill in SKILLS:
        cat = skill["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(skill)
    
    # 分类图标映射
    category_icons = {
        "学习": "📚",
        "创业": "🚀",
        "求职": "💼",
        "效率": "⚡",
        "开发": "💻",
        "营销": "📣",
    }
    
    readme_content = f"""# SkillHub AI Skills

> 专为大学生和年轻创业者设计的 AI 技能集合

## 📖 仓库介绍

本仓库包含 {len(SKILLS)} 个专业 AI 技能（Skill），覆盖学习、创业、求职、效率、开发等多个领域。每个 Skill 都是一个精心设计的 AI 助手配置，可以直接用于各种 AI 对话助手。

## 🎯 使用方式

### 方式一：直接复制使用（推荐）

1. 进入你想要下载的 Skill 文件夹（例如：`study-assistant-pro/`）
2. 打开 `SKILL.md` 文件
3. 复制全部内容
4. 粘贴到你的 AI 助手配置中
5. 保存后即可使用

### 方式二：下载整个仓库

1. 点击仓库首页的 "Code" 按钮
2. 选择 "Download ZIP"
3. 解压后根据需要复制 Skill 内容

### 方式三：克隆仓库

```bash
git clone https://github.com/YOUR_USERNAME/skillhub-skills.git
cd skillhub-skills
```

## 📚 技能分类

"""
    
    # 添加分类列表
    for category, skills in categories.items():
        icon = category_icons.get(category, "📁")
        readme_content += f"### {icon} {category}\n\n"
        readme_content += "| 技能 | 说明 | 文档 |\n"
        readme_content += "|------|------|------|\n"
        for skill in skills:
            readme_content += f"| {skill['icon']} [{skill['name']}](skills/{skill['id']}/) | 查看 {skill['name']} | [SKILL.md](skills/{skill['id']}/SKILL.md) |\n"
        readme_content += "\n"
    
    # 添加常见问题
    readme_content += """## ❓ 常见问题

### Q: 如何使用这些 Skill？

每个 Skill 文件夹中包含：
- `SKILL.md` - 主要的技能配置文件，复制内容到 AI 助手即可使用
- `README.md` - 该技能的详细说明和下载链接

### Q: 支持哪些 AI 助手？

本仓库的 Skill 适用于各种 AI 对话助手，包括：
- Qwen Code
- Claude
- ChatGPT
- 其他支持自定义配置的 AI 助手

### Q: 如何选择合适的 Skill？

1. 根据你的需求查看对应分类
2. 阅读 Skill 的 README.md 了解详细功能
3. 查看 SKILL.md 中的使用示例
4. 选择最适合你场景的 Skill

### Q: 可以修改 Skill 内容吗？

当然可以！本仓库采用 MIT 许可证，你可以：
- 自由修改 Skill 内容
- 分享给其他人
- 用于商业用途

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这些 Skill！

## 📞 联系方式

- 📧 Email: your-email@example.com
- 🐦 Twitter: @your-twitter
- 💬 GitHub Issues: [提问](https://github.com/YOUR_USERNAME/skillhub-skills/issues)

---

© 2026 SkillHub. All rights reserved.
"""
    
    return readme_content


def generate_skill_readme(skill, download_url_template):
    """生成单个 Skill 的 README.md"""
    
    skill_id = skill["id"]
    skill_name = skill["name"]
    category = skill["category"]
    icon = skill["icon"]
    
    # 下载链接
    raw_url = download_url_template.format(skill_id=skill_id)
    
    readme_content = f"""# {icon} {skill_name}

> {category} · SkillHub AI Skills

## 📖 技能介绍

本 Skill 专为{category.lower()}场景设计，提供专业的 AI 辅助功能。

## 📥 下载方式

### 方式一：在线查看（推荐）

1. 点击 [SKILL.md]({raw_url}) 查看完整内容
2. 复制全部内容
3. 粘贴到你的 AI 助手配置中

### 方式二：下载文件

1. 下载本仓库的 ZIP 文件
2. 解压后找到 `skills/{skill_id}/SKILL.md`
3. 复制内容到 AI 助手配置

### 方式三：直接克隆

```bash
git clone https://github.com/YOUR_USERNAME/skillhub-skills.git
cd skillhub-skills/skills/{skill_id}
```

## 📁 文件结构

```
{skill_id}/
├── README.md      # 本文件
└── SKILL.md       # 技能配置文件（复制此文件内容到 AI 助手）
```

## ⚡ 快速开始

1. **复制 Skill 内容**
   - 打开 [SKILL.md]({raw_url})
   - 全选并复制所有内容

2. **配置到 AI 助手**
   - 打开你的 AI 助手配置界面
   - 找到 Skill/技能配置区域
   - 粘贴内容并保存

3. **开始使用**
   - 按照 SKILL.md 中的说明使用

## 📋 使用示例

详见 [SKILL.md]({raw_url}) 中的使用示例部分。

## 🔗 相关链接

- [返回总览](../README.md)
- [查看 SKILL.md]({raw_url})
- [SkillHub 官网](https://skillhub.com)

## 📄 许可证

MIT License

---

© 2026 SkillHub. All rights reserved.
"""
    
    return readme_content


def copy_skill_files():
    """复制所有 Skill 文件到新结构"""
    
    # 下载链接模板（用户需要替换 YOUR_USERNAME）
    download_url_template = "https://github.com/YOUR_USERNAME/skillhub-skills/blob/main/skills/{skill_id}/SKILL.md"
    
    # 需要复制的文件列表
    files_to_copy = ["SKILL.md", "package.json", "index.js", "CHANGELOG.md"]
    
    # 为每个 Skill 创建文件夹
    for skill in SKILLS:
        skill_id = skill["id"]
        source_dir = SKILLZIP_DIR / skill_id
        target_dir = OUTPUT_DIR / skill_id
        
        if not source_dir.exists():
            print(f"⚠️  跳过：{skill_id} (源目录不存在)")
            continue
        
        # 创建目标目录
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # 复制文件
        for file_name in files_to_copy:
            src_file = source_dir / file_name
            dst_file = target_dir / file_name
            if src_file.exists():
                shutil.copy2(src_file, dst_file)
                print(f"✅ 复制：{skill_id}/{file_name}")
            else:
                print(f"⚠️  缺少：{skill_id}/{file_name}")
        
        # 生成新的 README.md
        skill_readme_content = generate_skill_readme(skill, download_url_template)
        skill_readme_dst = target_dir / "README.md"
        with open(skill_readme_dst, "w", encoding="utf-8") as f:
            f.write(skill_readme_content)
        print(f"✅ 生成：{skill_id}/README.md")
    
    # 生成总 README.md
    main_readme_content = generate_main_readme()
    main_readme_dst = OUTPUT_DIR.parent / "README.md"
    with open(main_readme_dst, "w", encoding="utf-8") as f:
        f.write(main_readme_content)
    print(f"✅ 生成：README.md")
    
    # 复制 LICENSE（如果存在）
    license_src = Path("/Users/blueblue/skillhub/LICENSE")
    license_dst = OUTPUT_DIR.parent / "LICENSE"
    if license_src.exists():
        shutil.copy2(license_src, license_dst)
    else:
        # 创建默认 MIT LICENSE
        mit_license = """MIT License

Copyright (c) 2026 SkillHub

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
        with open(license_dst, "w", encoding="utf-8") as f:
            f.write(mit_license)
        print(f"✅ 创建：LICENSE")
    
    # 创建 .gitignore
    gitignore_content = """# macOS
.DS_Store

# Editor
.vscode/
.idea/
*.swp
*.swo
*~

# Logs
*.log
npm-debug.log*

# Dependencies
node_modules/
"""
    gitignore_dst = OUTPUT_DIR.parent / ".gitignore"
    with open(gitignore_dst, "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    print(f"✅ 创建：.gitignore")
    
    print("\n✅ 所有文件生成完成！")
    print(f"📁 输出目录：{OUTPUT_DIR.parent}")


if __name__ == "__main__":
    copy_skill_files()
