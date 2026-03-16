---
name: qwen-code
description: Wield Qwen Code CLI as a powerful auxiliary tool for code understanding, editing, workflow automation, and vision-based analysis. Use when tasks benefit from enhanced code parsing, large codebase handling, Git workflow automation, or image/diagram analysis. Also use when user requests Qwen operations.
allowed-tools:
  - Bash
  - Read
  - Write
  - Grep
  - Glob
---

# Qwen Code Integration Skill

This skill enables Claude Code to effectively orchestrate Qwen Code CLI with Qwen3-Coder for code understanding, editing, workflow automation, and specialized tasks.

## When to Use This Skill

### Ideal Use Cases

1. **Large Codebase Analysis**
   - Query and understand massive codebases beyond traditional context limits
   - Deep architecture investigation with enhanced parser
   - Cross-file dependency mapping optimized for Qwen-Coder

2. **Code Editing & Refactoring**
   - Intelligent code modifications and refactoring
   - Performance optimization suggestions
   - Code structure improvements

3. **Workflow Automation**
   - Git operations and pull request handling
   - Complex operational task automation
   - Repository management tasks

4. **Vision-Based Analysis**
   - Architecture diagram analysis
   - Screenshot and image understanding
   - Automatic vision-capable model switching

5. **Test Generation**
   - Enhanced test suite generation with optimized parser
   - Unit tests, integration tests
   - Coverage optimization

6. **Second Opinion / Cross-Validation**
   - Code review from different AI perspective
   - Alternative analysis for bug detection
   - Security audit with Qwen's enhanced understanding

### When NOT to Use

- Simple, quick tasks (overhead not worth it)
- Tasks requiring immediate response (rate limits cause delays)
- When context is already loaded and understood
- Interactive refinement requiring conversation
- Non-code tasks (Qwen Code is optimized for code)

## Core Instructions

### 1. Verify Installation

```bash
command -v qwen || which qwen
```

### 2. Basic Command Pattern

```bash
qwen "[prompt]" -o text 2>&1
```

Key flags:
- `-o text`: Human-readable output
- `-o json`: Structured output with stats
- `--list-sessions`: List all sessions
- `-r [index]`: Resume specific session
- `-c [tokens]`: Set conversation compression threshold

### 3. Critical Behavioral Notes

**Conversation Compression**: Qwen automatically compresses long conversations. Use `-c` flag to configure token threshold.

**Vision Mode**: Qwen automatically detects images and switches to vision-capable models. No manual flag needed.

**Rate Limits**: Same as Gemini CLI - 2,000 requests/day, 60/minute. CLI handles rate limiting gracefully with automatic backoff.

### 4. Output Processing

For JSON output (`-o json`), parse:
```json
{
  "response": "actual content",
  "stats": {
    "models": { "tokens": {...} },
    "tools": { "byName": {...} },
    "vision": { "enabled": true, "model": "qwen-vl" }
  }
}
```

## Quick Reference Commands

### Code Understanding
```bash
qwen "Explain this codebase structure in detail" -o text
```

### Code Editing
```bash
qwen "Refactor this function for better performance and readability" -o text
```

### Bug Detection
```bash
qwen "Find potential bugs in this code and suggest fixes" -o text
```

### Test Generation
```bash
qwen "Generate comprehensive unit tests for this module" -o text
```

### Workflow Automation
```bash
qwen "Help me create a pull request for these changes" -o text
```

### Git Operations
```bash
qwen "Handle this complex Git merge conflict" -o text
```

### Vision Analysis
```bash
qwen "Analyze this architecture diagram and suggest improvements" -o text
```

### Session Management
```bash
qwen --list-sessions
qwen -r 0 "Continue our previous discussion about refactoring"
```

## Error Handling

### Rate Limit Exceeded
- Free tier: 2,000 requests/day, 60/minute
- CLI auto-retries with exponential backoff
- Consider using conversation compression for long sessions

### Command Failures
- Check JSON output for detailed error stats
- Verify Qwen is authenticated: `qwen --version`
- Check `~/.qwen/settings.json` for config issues
- Ensure Node.js 20+ is installed

### Vision Model Issues
- Automatic detection usually works seamlessly
- Manually specify vision model if needed: `-m qwen-vl-max`
- Check image format compatibility

### Validation After Generation
Always verify Qwen's output:
- Check for security vulnerabilities (XSS, injection)
- Test functionality matches requirements
- Review code style consistency
- Verify dependencies are appropriate
- Validate Git workflow suggestions

## Integration Workflow

### Standard Code Understanding Cycle

```bash
# 1. Initial understanding
qwen "Explain this large codebase structure" -o text

# 2. Specific area investigation
qwen "Focus on the authentication module and its dependencies" -o text

# 3. Refactoring suggestions
qwen "Suggest improvements for the identified bottlenecks" -o text
```

### Workflow Automation

```bash
# Git operations
qwen "Create a feature branch and prepare for pull request" -o text

# Complex operations
qwen "Handle this rebase conflict and update CHANGELOG" -o text
```

### Vision Analysis

```bash
# Diagram understanding
qwen "Analyze this system architecture diagram" -o text

# Screenshot analysis
qwen "Review this UI mockup and suggest improvements" -o text
```

### Session Persistence

```bash
# Start long-running analysis
qwen "Analyze entire monorepo structure" -o text

# Resume later
qwen -r 0 "Continue analysis focusing on test coverage"
```

## Qwen's Unique Capabilities

These features are available only through Qwen Code:

1. **Enhanced Code Parser** - Optimized specifically for Qwen-Coder models
2. **Large Codebase Handling** - Beyond traditional context limits
3. **Vision Integration** - Automatic image detection and analysis
4. **Workflow Automation** - Git operations and PR management
5. **Conversation Compression** - Token-efficient long sessions

## Configuration

### Project Context (Optional)

Create `.qwen/QWEN.md` in project root for persistent context that Qwen will automatically read.

### Session Management

List sessions: `qwen --list-sessions`
Resume session: `qwen -r [index] -o text`

### Token Configuration

Set conversation compression: `qwen -c 4000 "[prompt]"`

## See Also

- `reference.md` - Complete command and flag reference
- `templates.md` - Prompt templates for common operations
- `patterns.md` - Advanced integration patterns
- `tools.md` - Qwen's built-in tools documentation
