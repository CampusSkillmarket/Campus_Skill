# 🌐 网页开发助手 (Web Dev Assistant)

## 技能描述
专为大学生和创业初学者设计的网页开发技能。无论是课程项目、个人作品集还是创业 MVP，都能快速生成完整网站代码，让想法快速上线。

## 核心能力

### 1. 完整网站生成
- 单页作品集网站
- 企业官网
- 电商 Landing Page
- 博客系统
- 后台管理系统

### 2. 技术栈推荐
- 前端：React/Vue/Next.js/原生 HTML
- 样式：Tailwind CSS/Bootstrap/原生 CSS
- 后端：Node.js/Python/Go
- 数据库：MySQL/PostgreSQL/MongoDB

### 3. UI/UX 设计
- 响应式布局
- 现代化设计
- 配色方案
- 交互动效

### 4. 部署指南
- Vercel/Netlify 前端部署
- Railway/Render 后端部署
- 域名配置
- HTTPS 证书

## 快速生成模板

### 模板 1：个人作品集网站
```
技术栈：React + Tailwind CSS + Framer Motion

页面结构：
┌─────────────────────────────┐
│   Navigation (固定顶部)     │
├─────────────────────────────┤
│   Hero Section              │
│   - 头像 + 自我介绍         │
│   - CTA 按钮                │
├─────────────────────────────┤
│   About Me                  │
│   - 个人简介                │
│   - 技能标签                │
├─────────────────────────────┤
│   Projects                  │
│   - 项目卡片 (3-6 个)        │
├─────────────────────────────┤
│   Contact                   │
│   - 联系方式                │
│   - 社交媒体链接            │
├─────────────────────────────┤
│   Footer                    │
└─────────────────────────────┘
```

### 模板 2：创业 Landing Page
```
技术栈：Next.js + Tailwind CSS

转化漏斗设计：
1. Hero → 吸引注意
2. Problem → 戳中痛点
3. Solution → 展示方案
4. Features → 核心功能
5. Social Proof → 用户评价
6. Pricing → 价格方案
7. FAQ → 消除疑虑
8. CTA → 促成转化
```

### 模板 3：博客系统
```
技术栈：Next.js + MDX + Tailwind CSS

功能模块：
- 文章列表页（分页/搜索/标签）
- 文章详情页（目录/评论/分享）
- 关于页面
- RSS 订阅
- SEO 优化
- 深色模式
```

## 使用示例

### 示例 1：生成个人作品集
```
用户：帮我生成一个前端工程师的作品集网站

我会生成：

📁 项目结构
portfolio/
├── public/
│   ├── images/
│   └── resume.pdf
├── src/
│   ├── components/
│   │   ├── Navbar.jsx
│   │   ├── Hero.jsx
│   │   ├── Projects.jsx
│   │   └── Contact.jsx
│   ├── pages/
│   │   └── index.jsx
│   └── styles/
│       └── globals.css
├── package.json
└── tailwind.config.js

📝 核心代码 (Hero Section)
```jsx
function Hero() {
  return (
    <section className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-500 to-purple-600">
      <div className="text-center text-white">
        <img 
          src="/images/avatar.jpg" 
          className="w-40 h-40 rounded-full mx-auto mb-6 border-4 border-white"
        />
        <h1 className="text-5xl font-bold mb-4">
          你好，我是张三
        </h1>
        <p className="text-xl mb-8">
          前端工程师 | React 爱好者 | 开源贡献者
        </p>
        <div className="space-x-4">
          <button className="bg-white text-purple-600 px-8 py-3 rounded-full font-semibold hover:bg-opacity-90 transition">
            查看作品
          </button>
          <button className="border-2 border-white px-8 py-3 rounded-full font-semibold hover:bg-white hover:text-purple-600 transition">
            联系我
          </button>
        </div>
      </div>
    </section>
  )
}
```

🎨 配色方案
- 主色：#3B82F6 (蓝色)
- 辅色：#8B5CF6 (紫色)
- 背景：渐变 from-blue-500 to-purple-600

🚀 部署步骤
1. 代码上传到 GitHub
2. 登录 Vercel.com
3. Import 项目
4. 自动部署完成
```

### 示例 2：生成电商 Landing Page
```
用户：我要卖一个时间管理课程，帮我生成 Landing Page

我会生成：

📝 核心代码 (转化优化版)
```jsx
function LandingPage() {
  return (
    <div>
      {/* Hero - 吸引注意 */}
      <section className="py-20 bg-gray-900 text-white">
        <div className="container mx-auto text-center">
          <h1 className="text-5xl font-bold mb-6">
            30 天，告别拖延症
          </h1>
          <p className="text-xl mb-8 text-gray-300">
            10000+ 学员验证的时间管理方法
            <br/>
            让你每天多出 2 小时自由时间
          </p>
          <button className="bg-orange-500 hover:bg-orange-600 text-white px-10 py-4 rounded-full text-xl font-bold transition">
            立即报名 - 限时优惠 ¥299
          </button>
          <p className="mt-4 text-sm text-gray-400">
            ⏰ 优惠倒计时 24 小时 | 📚 已有 10000+ 学员加入
          </p>
        </div>
      </section>

      {/* Problem - 戳中痛点 */}
      <section className="py-16">
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            这些困扰，你中了几条？
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              { icon: '📱', text: '刷手机停不下来，一天就过去了' },
              { icon: '😴', text: '总是熬夜赶工，第二天没精神' },
              { icon: '📋', text: '待办清单越列越长，完成的没几个' },
            ].map((item, i) => (
              <div key={i} className="text-center p-6 bg-red-50 rounded-xl">
                <div className="text-4xl mb-4">{item.icon}</div>
                <p className="text-lg">{item.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Social Proof - 用户评价 */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            学员反馈
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              { name: '小李', role: '大学生', content: '学完后效率提升 3 倍，GPA 从 2.5 到 3.8！' },
              { name: '小王', role: '职场新人', content: '终于不用加班了，有时间发展副业' },
              { name: '小张', role: '创业者', content: '团队效率整体提升，业绩翻倍' },
            ].map((item, i) => (
              <div key={i} className="bg-white p-6 rounded-xl shadow">
                <div className="flex items-center mb-4">
                  <div className="w-12 h-12 bg-blue-500 rounded-full mr-4"></div>
                  <div>
                    <div className="font-bold">{item.name}</div>
                    <div className="text-sm text-gray-500">{item.role}</div>
                  </div>
                </div>
                <p className="text-gray-600">{item.content}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing - 价格方案 */}
      <section className="py-16">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl font-bold mb-12">
            选择适合你的方案
          </h2>
          <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
            {/* 基础版 */}
            <div className="border-2 border-gray-200 rounded-2xl p-8">
              <h3 className="text-xl font-bold mb-2">基础版</h3>
              <div className="text-4xl font-bold mb-6">¥299</div>
              <ul className="text-left space-y-3 mb-8">
                <li>✅ 10 节视频课程</li>
                <li>✅ 配套练习册</li>
                <li>❌ 社群答疑</li>
                <li>❌ 1v1 辅导</li>
              </ul>
              <button className="w-full border-2 border-blue-500 text-blue-500 py-3 rounded-full font-bold hover:bg-blue-50 transition">
                选择基础版
              </button>
            </div>
            {/* 进阶版 - 推荐 */}
            <div className="border-2 border-blue-500 rounded-2xl p-8 relative bg-blue-50">
              <div className="absolute -top-4 left-1/2 -translate-x-1/2 bg-blue-500 text-white px-4 py-1 rounded-full text-sm">
                🌟 最受欢迎
              </div>
              <h3 className="text-xl font-bold mb-2">进阶版</h3>
              <div className="text-4xl font-bold mb-6">¥599</div>
              <ul className="text-left space-y-3 mb-8">
                <li>✅ 10 节视频课程</li>
                <li>✅ 配套练习册</li>
                <li>✅ 社群答疑</li>
                <li>❌ 1v1 辅导</li>
              </ul>
              <button className="w-full bg-blue-500 text-white py-3 rounded-full font-bold hover:bg-blue-600 transition">
                选择进阶版
              </button>
            </div>
            {/* VIP 版 */}
            <div className="border-2 border-gray-200 rounded-2xl p-8">
              <h3 className="text-xl font-bold mb-2">VIP 版</h3>
              <div className="text-4xl font-bold mb-6">¥1999</div>
              <ul className="text-left space-y-3 mb-8">
                <li>✅ 10 节视频课程</li>
                <li>✅ 配套练习册</li>
                <li>✅ 社群答疑</li>
                <li>✅ 30 分钟 1v1 辅导</li>
              </ul>
              <button className="w-full border-2 border-blue-500 text-blue-500 py-3 rounded-full font-bold hover:bg-blue-50 transition">
                选择 VIP 版
              </button>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
```
```

### 示例 3：生成后台管理系统
```
用户：帮我生成一个用户管理后台

我会生成：

📁 技术栈推荐
- 前端：React + Ant Design
- 状态管理：Zustand
- 请求库：Axios
- 图表：Recharts

📝 核心功能
- 用户列表（表格 + 分页 + 搜索）
- 用户详情（弹窗展示）
- 添加/编辑用户（表单）
- 删除用户（确认对话框）
- 数据统计（图表看板）

📊 数据看板设计
┌─────────────────────────────────────┐
│  总用户数  │  今日新增  │  活跃用户  │
│   10,234  │    +156   │   5,678   │
├─────────────────────────────────────┤
│                                     │
│  [用户增长趋势折线图]                │
│                                     │
├─────────────────────────────────────┤
│  [用户分布饼图]  │  [用户来源柱状图] │
└─────────────────────────────────────┘
```

## 响应式设计规范

### 断点设置
```css
/* 手机 */
@media (max-width: 640px) { }

/* 平板 */
@media (min-width: 641px) and (max-width: 1024px) { }

/* 桌面 */
@media (min-width: 1025px) { }
```

### 移动端优先
```jsx
// 默认移动端样式
<div className="flex flex-col">
  {/* 桌面端覆盖 */}
  <div className="md:flex md:flex-row md:space-x-4">
    ...
  </div>
</div>
```

## 部署指南

### Vercel 部署（前端）
```bash
# 1. 安装 Vercel CLI
npm i -g vercel

# 2. 登录
vercel login

# 3. 部署
vercel

# 4. 生产环境
vercel --prod
```

### Netlify 部署
```bash
# 1. 安装 Netlify CLI
npm i -g netlify-cli

# 2. 登录
netlify login

# 3. 初始化
netlify init

# 4. 部署
netlify deploy --prod
```

## 使用提示

1. **说明网站类型**：作品集/电商/博客/后台
2. **技术栈偏好**：React/Vue/原生
3. 设计风格：简约/商务/活泼
4. **功能需求**：列出核心功能
5. **部署环境**：Vercel/自有服务器

## 常用组件库

### React
- Ant Design（企业级）
- Material-UI（Material 风格）
- Chakra UI（快速开发）
- Tailwind UI（Tailwind 生态）

### Vue
- Element Plus
- Vuetify
- Naive UI
- Vant（移动端）

## 性能优化建议

1. 图片懒加载
2. 代码分割 (Code Splitting)
3. 静态资源 CDN
4. SSR/SSG (Next.js/Nuxt.js)
5. 缓存策略

## 注意事项

- 移动端优先设计
- 注意无障碍访问 (a11y)
- SEO 基础优化
- 表单验证
- 错误处理
