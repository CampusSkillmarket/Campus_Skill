# SkillHub GitHub 上传指南

## ✅ 新的仓库结构

文件已准备好在：`/Users/blueblue/skillhub/github-restructure/`

新的目录结构：
```
skillhub-skills/
├── README.md              # 总览：介绍仓库用途、使用方式
├── LICENSE                # MIT 许可证
├── .gitignore             # Git 忽略文件
└── skills/                # 所有 Skill 文件夹
    ├── study-assistant-pro/
    │   ├── README.md      # 该 Skill 介绍 + 下载链接
    │   └── SKILL.md       # Skill 具体内容
    ├── business-plan-generator-pro/
    │   ├── README.md
    │   └── SKILL.md
    └── ... (共 32 个 Skill)
```

---

## 📝 上传步骤（3 步完成）

### 第 1 步：在 GitHub 创建仓库

1. 访问：**https://github.com/new**
2. 填写信息：
   - **Repository name**: `skillhub-skills`
   - **Description**: `SkillHub AI Skills - 专为大学生和年轻创业者设计的 AI 技能集合`
   - **Visibility**: 选择 **Public** (公开)
   - ❌ 不要勾选 "Initialize this repository with a README"
3. 点击 **"Create repository"**

---

### 第 2 步：推送代码到 GitHub

复制并执行以下命令（在终端中）：

```bash
# 进入新目录
cd /Users/blueblue/skillhub/github-restructure

# 替换 YOUR_USERNAME 为你的 GitHub 用户名
# 例如：https://github.com/zhangsan/skillhub-skills.git
git remote add origin https://github.com/YOUR_USERNAME/skillhub-skills.git

# 初始化 Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "feat: 初始版本 - 32 个 AI Skills"

# 推送到 GitHub
git branch -M main
git push -u origin main
```

**等待上传完成**（约 1-3 分钟）

---

### 第 3 步：验证上传 & 更新链接

上传完成后：

1. 刷新 GitHub 仓库页面
2. 确认所有文件都已上传：
   - ✅ README.md
   - ✅ LICENSE
   - ✅ skills/ 目录（32 个 Skill 文件夹）

3. **重要：更新下载链接**
   
   每个 Skill 的 README.md 中的下载链接使用的是占位符 `YOUR_USERNAME`，你需要：
   
   **方式 A：使用脚本批量替换（推荐）**
   ```bash
   cd /Users/blueblue/skillhub/github-restructure
   
   # 替换为你的 GitHub 用户名
   YOUR_GITHUB_USERNAME="你的用户名"
   
   # 批量替换所有 README.md 中的链接
   find skills -name "README.md" -exec sed -i '' "s/YOUR_USERNAME/$YOUR_GITHUB_USERNAME/g" {} \;
   
   # 同时更新总 README.md
   sed -i '' "s/YOUR_USERNAME/$YOUR_GITHUB_USERNAME/g" README.md
   
   # 重新提交
   git add .
   git commit -m "docs: 更新 GitHub 用户名"
   git push
   ```
   
   **方式 B：手动替换**
   - 用文本编辑器打开每个 README.md
   - 将 `YOUR_USERNAME` 替换为你的 GitHub 用户名
   - 保存后重新推送

---

## 🔗 获取下载链接

上传成功后，你的 Skill 文档链接格式为：

```
# 总览文档
https://github.com/YOUR_USERNAME/skillhub-skills/blob/main/README.md

# 单个 Skill 文档
https://github.com/YOUR_USERNAME/skillhub-skills/blob/main/skills/study-assistant-pro/README.md

# 单个 Skill 的 SKILL.md（直接复制使用）
https://github.com/YOUR_USERNAME/skillhub-skills/blob/main/skills/study-assistant-pro/SKILL.md
```

**示例：**
```bash
# 学业助手 Pro
https://github.com/zhangsan/skillhub-skills/blob/main/skills/study-assistant-pro/SKILL.md

# 商业计划书生成器
https://github.com/zhangsan/skillhub-skills/blob/main/skills/business-plan-generator-pro/SKILL.md

# 网页开发助手
https://github.com/zhangsan/skillhub-skills/blob/main/skills/web-dev-assistant/SKILL.md
```

---

## 📋 完整命令（一次性复制）

```bash
# 进入新目录
cd /Users/blueblue/skillhub/github-restructure

# 设置你的 GitHub 用户名
GITHUB_USER="YOUR_USERNAME"

# 初始化 Git
git init
git add .
git commit -m "feat: 初始版本 - 32 个 AI Skills"

# 添加远程仓库
git remote add origin https://github.com/${GITHUB_USER}/skillhub-skills.git

# 推送
git branch -M main
git push -u origin main

# 更新链接中的用户名（可选，如果上面已经设置）
# find skills -name "README.md" -exec sed -i '' "s/YOUR_USERNAME/$GITHUB_USER/g" {} \;
# sed -i '' "s/YOUR_USERNAME/$GITHUB_USER/g" README.md
# git add .
# git commit -m "docs: 更新 GitHub 用户名"
# git push

echo "✅ 上传完成！"
echo "📍 访问：https://github.com/${GITHUB_USER}/skillhub-skills"
```

---

## ⚠️ 常见问题

### Q1: 提示 "remote origin already exists"
```bash
# 解决方法：
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/skillhub-skills.git
```

### Q2: 推送失败，权限错误
- 检查 Repository name 是否正确
- 确认你是仓库所有者或有写入权限
- 检查网络连接

### Q3: 如何修改下载链接？

每个 Skill 的 README.md 中的链接格式为：
```markdown
https://github.com/YOUR_USERNAME/skillhub-skills/blob/main/skills/study-assistant-pro/SKILL.md
```

上传后，将 `YOUR_USERNAME` 替换为你的 GitHub 用户名即可。

---

## 🎯 下一步

上传完成后：

1. **访问仓库**：https://github.com/YOUR_USERNAME/skillhub-skills
2. **测试链接**：点击任意 Skill，确认可以查看 SKILL.md
3. **更新网站配置**：将新的 GitHub 链接配置到你的 SkillHub 网站

---

## 📞 需要帮助？

如果遇到问题，请告诉我：
1. 错误信息
2. 执行到哪一步
3. 你的 GitHub 用户名

我会帮你解决！
