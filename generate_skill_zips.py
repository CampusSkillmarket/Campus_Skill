#!/usr/bin/env python3
"""
为每个 skill 生成 zip 文件，并更新 README.md 中的下载链接
"""

import os
import zipfile
import re
from pathlib import Path

# 配置
SKILLS_DIR = Path(__file__).parent / "skills"
GITHUB_ORG = "CampusSkillmarket"
GITHUB_REPO = "skillhub-skills"

def get_all_skills():
    """获取所有 skill 文件夹"""
    skills = []
    for item in SKILLS_DIR.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            skills.append(item)
    return sorted(skills, key=lambda x: x.name)

def create_skill_zip(skill_path):
    """为单个 skill 创建 zip 文件"""
    zip_path = skill_path / f"{skill_path.name}.zip"
    
    # 创建 zip 文件
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in skill_path.iterdir():
            if file.is_file() and not file.name.startswith('.'):
                # 只添加非隐藏文件，不添加 zip 文件本身
                if not file.name.endswith('.zip'):
                    zipf.write(file, file.name)
    
    return zip_path

def update_skill_readme(skill_path):
    """更新 skill 的 README.md，添加 zip 下载链接"""
    readme_path = skill_path / "README.md"
    
    if not readme_path.exists():
        return None
    
    skill_name = skill_path.name
    
    # GitHub raw 内容链接
    raw_url = f"https://raw.githubusercontent.com/{GITHUB_ORG}/{GITHUB_REPO}/main/skills/{skill_name}/SKILL.md"
    # GitHub blob 链接
    blob_url = f"https://github.com/{GITHUB_ORG}/{GITHUB_REPO}/blob/main/skills/{skill_name}/SKILL.md"
    # ZIP 下载链接
    zip_url = f"https://github.com/{GITHUB_ORG}/{GITHUB_REPO}/raw/main/skills/{skill_name}/{skill_name}.zip"
    
    # 新的 README 内容
    new_content = f"""# {skill_name.replace('-', ' ').title()}

> SkillHub AI Skills

## 📖 技能介绍

本 Skill 专为大学生设计，提供 AI 辅助功能，帮助你解决学习、生活中的实际问题。

## 📥 下载方式

### 方式一：在线查看 SKILL.md（推荐）

1. 点击 [SKILL.md]({blob_url}) 查看完整内容
2. 复制全部内容
3. 粘贴到你的 AI 助手配置中

### 方式二：下载 ZIP 文件

1. 点击下载 [{skill_name}.zip]({zip_url})
2. 解压后打开 `SKILL.md`
3. 复制内容到 AI 助手配置

### 方式三：克隆整个仓库

```bash
git clone https://github.com/{GITHUB_ORG}/{GITHUB_REPO}.git
cd {GITHUB_REPO}/skills/{skill_name}
```

## 📁 文件结构

```
{skill_name}/
├── README.md              # 本文件
├── SKILL.md              # 技能配置文件（复制此文件内容到 AI 助手）
└── {skill_name}.zip      # 压缩包（包含 SKILL.md 和 README.md）
```

## ⚡ 快速开始

1. **复制 Skill 内容**
   - 打开 [SKILL.md]({blob_url})
   - 全选并复制所有内容

2. **配置到 AI 助手**
   - 打开你的 AI 助手配置界面
   - 找到 Skill/技能配置区域
   - 粘贴内容并保存

3. **开始使用**
   - 按照 SKILL.md 中的说明使用

## 🔗 相关链接

- [返回总览](../README.md)
- [查看 SKILL.md]({blob_url})
- [下载 ZIP]({zip_url})

## 📄 许可证

MIT License

---

© 2026 SkillHub. All rights reserved.
"""
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return readme_path

def main():
    skills = get_all_skills()
    print(f"找到 {len(skills)} 个 skill\n")
    
    for skill_path in skills:
        # 创建 zip
        zip_path = create_skill_zip(skill_path)
        print(f"✓ 创建 {skill_path.name}.zip")
        
        # 更新 README
        readme_path = update_skill_readme(skill_path)
        if readme_path:
            print(f"✓ 更新 {skill_path.name}/README.md")
        
        print()
    
    print("=" * 50)
    print("完成！所有 skill 的 zip 文件已生成，README.md 已更新")

if __name__ == "__main__":
    main()
