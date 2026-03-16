/**
 * Qwen Code Integration Skill (qwen-code-2-skills)
 * 
 * SkillHub Standard Skill Format
 * 
 * @package @skillhub/qwen-code-2-skills
 * @version 1.0.0
 * @author SkillHub
 * @license MIT
 * @see https://skillhub.com/skills/qwen-code-2-skills
 */

// Skill 配置
const skillConfig = {
  name: 'qwen-code-2-skills',
  displayName: 'Qwen Code Integration Skill',
  version: '1.0.0',
  category: 'skillhub',
  format: 'skillhub-standard',
  author: 'SkillHub',
  license: 'MIT',
  homepage: 'https://skillhub.com/skills/qwen-code-2-skills',
  repository: 'https://github.com/skillhub/skills'
};

/**
 * 处理用户请求
 * @param {input: string, context: object} params - 用户输入和上下文
 * @returns {response: string} AI 响应
 */
async function handleRequest({ input, context }) {
  // 读取 SKILL.md 中的技能定义
  const fs = require('fs');
  const path = require('path');
  
  const skillPath = path.join(__dirname, 'SKILL.md');
  const skillContent = fs.readFileSync(skillPath, 'utf-8');
  
  // 这里可以添加自定义逻辑
  // 目前直接返回 SKILL.md 内容供 AI 使用
  return {
    response: skillContent,
    metadata: skillConfig
  };
}

/**
 * 初始化技能
 */
async function init() {
  console.log(`🚀 初始化 ${skillConfig.displayName}...`);
  console.log(`📦 版本：${skillConfig.version}`);
  console.log(`🌐 主页：${skillConfig.homepage}`);
  return skillConfig;
}

// 导出
module.exports = {
  skillConfig,
  handleRequest,
  init
};

// 如果直接运行
if (require.main === module) {
  init().then(() => {
    console.log('✅ 技能已就绪，等待用户输入...');
  });
}
