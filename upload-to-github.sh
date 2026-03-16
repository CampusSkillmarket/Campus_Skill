#!/bin/bash

# SkillHub GitHub 上传向导（新版）
# 新的目录结构：每个 Skill 独立文件夹

echo "🚀 SkillHub GitHub 上传向导（新版）"
echo "=================================="
echo ""

# 脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "📁 当前目录：$SCRIPT_DIR"
echo ""

# 检查是否登录 GitHub
if ! gh auth status &> /dev/null; then
    echo "⚠️  检测到未登录 GitHub"
    echo ""
    echo "请选择登录方式："
    echo "1. 使用 GitHub CLI (gh) 登录"
    echo "2. 手动在网页创建仓库"
    echo ""
    read -p "请选择 (1/2): " choice

    if [ "$choice" = "1" ]; then
        echo "📝 正在登录 GitHub..."
        gh auth login
    else
        echo ""
        echo "📋 请按以下步骤操作："
        echo "1. 访问 https://github.com/new"
        echo "2. Repository name: skillhub-skills"
        echo "3. 选择 Public 或 Private"
        echo "4. 点击 Create repository"
        echo ""
        read -p "完成后按回车继续..."
    fi
fi

# 获取 GitHub 用户名
echo ""
read -p "请输入你的 GitHub 用户名：GITHUB_USERNAME"

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ 用户名不能为空"
    exit 1
fi

echo ""
echo "📦 准备上传到：https://github.com/${GITHUB_USERNAME}/skillhub-skills"
echo ""

# 检查仓库是否存在
if gh repo view ${GITHUB_USERNAME}/skillhub-skills &> /dev/null; then
    echo "⚠️  仓库已存在，将追加上传"
    if git remote get-url origin &> /dev/null; then
        git remote set-url origin https://github.com/${GITHUB_USERNAME}/skillhub-skills.git
    else
        git remote add origin https://github.com/${GITHUB_USERNAME}/skillhub-skills.git
    fi
else
    echo "✨ 创建新仓库..."
    gh repo create ${GITHUB_USERNAME}/skillhub-skills --public --source=. --remote=origin --push
    if [ $? -eq 0 ]; then
        echo "✅ 仓库创建成功"
        echo ""
        echo "🔄 更新下载链接中的用户名..."
        
        # 批量替换所有 README.md 中的 YOUR_USERNAME
        find skills -name "README.md" -exec sed -i '' "s/YOUR_USERNAME/${GITHUB_USERNAME}/g" {} \;
        sed -i '' "s/YOUR_USERNAME/${GITHUB_USERNAME}/g" README.md
        
        git add .
        git commit -m "docs: 更新 GitHub 用户名链接"
        git push
        
        echo ""
        echo "🎉 上传完成！"
        echo ""
        echo "📍 访问地址：https://github.com/${GITHUB_USERNAME}/skillhub-skills"
        echo ""
        exit 0
    fi
fi

# 初始化 Git（如果需要）
if [ ! -d ".git" ]; then
    echo "📦 初始化 Git 仓库..."
    git init
fi

# 添加文件
echo ""
echo "📦 添加文件..."
git add .

# 提交
echo "📝 提交更改..."
git commit -m "feat: 初始版本 - 32 个 AI Skills"

# 更新链接中的用户名
echo ""
echo "🔄 更新下载链接中的用户名..."
find skills -name "README.md" -exec sed -i '' "s/YOUR_USERNAME/${GITHUB_USERNAME}/g" {} \;
sed -i '' "s/YOUR_USERNAME/${GITHUB_USERNAME}/g" README.md

git add .
git commit -m "docs: 更新 GitHub 用户名链接"

# 推送到 GitHub
echo ""
echo "📤 正在上传文件..."
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 上传成功！"
    echo ""
    echo "📍 访问地址：https://github.com/${GITHUB_USERNAME}/skillhub-skills"
    echo ""
    echo "📝 下一步："
    echo "1. 访问上面的地址查看你的仓库"
    echo "2. 测试 Skill 文档链接是否正常"
    echo "3. 更新你的网站配置"
    echo ""
else
    echo ""
    echo "❌ 上传失败，请检查网络连接或 GitHub 设置"
    exit 1
fi
