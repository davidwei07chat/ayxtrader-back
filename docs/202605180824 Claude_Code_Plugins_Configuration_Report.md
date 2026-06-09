# 202605180824 Claude_Code_Plugins_Configuration_Report.md

## 1. 元数据与文档记录 / Metadata & Document Records

### 1.1 创建与更新历史 / Creation & Update History
* **创建记录 (Creation Record)**:
  * **创建日期 (Creation Date)**: 2026-05-18
  * **创建时间 (Creation Time)**: 08:24:00 (UTC+8)
  * **创建人 (Author)**: Antigravity (AI pair programmer)
  * **文档路径 (Path)**: `docs/202605180824 Claude_Code_Plugins_Configuration_Report.md`
* **更新历史 (Update History)**:
  * **2026-05-18 08:24** | Antigravity | First draft of the Claude Code Plugins complete configuration report / 首次草拟 Claude Code 插件完整配置报告。

### 1.2 技术栈与平台信息 / Tech Stack & Platform Info
* **技术栈 (Tech Stack)**:
  * **框架系统 (Framework)**: Claude Code Plugins System (MCP 1.0, Custom Skills Schema, Command Scripts)
  * **核心依赖 (Core Dependencies)**: Model Context Protocol (MCP) v1.0.0, Node.js v18.17.0+, Python v3.10.0+
* **平台信息 (Platform Info)**:
  * **开发平台 (Dev Platform)**: Linux OS (Ubuntu 22.04 LTS), VSCode 1.85.0
  * **部署平台 (Deployment Platform)**: Claude Code CLI / Claude Agent Environment
  * **构建工具 (Build Tools)**: Git, GitHub Actions

### 1.3 项目结构树 / Project Structure Tree
```text
/tmp/claude-plugins-official
  ├── .claude-plugin/            # 插件市场核心配置 / Plugin marketplace core configs
  │   └── marketplace.json       # 市场定义文件 / Marketplace definition registry
  ├── plugins/                   # 官方开发并维护的内部插件 / Internal plugins maintained by Anthropic
  │   ├── agent-sdk-dev/
  │   ├── code-modernization/
  │   ├── frontend-design/
  │   └── [Other internal plugins...]
  ├── external_plugins/          # 第三方及社区贡献插件 / Third-party & community plugins
  │   ├── playwright/
  │   ├── github/
  │   ├── asana/
  │   └── [Other external plugins...]
  └── README.md                  # 说明文档 / Documentation
```

### 1.4 存放与命名约束 / Storage & Naming Constraints
* **统一路径 (Unified Path)**: `docs/`
* **命名规范 (Naming Rule)**: 精确到分的时间戳 + 空格 + 英文名 (`202605180824 Claude_Code_Plugins_Configuration_Report.md`)
* **语言限制 (Language Constraint)**: 文件名严禁使用中文 (English file name only).

---

## 2. 概述 / Overview
* **中文**：本报告是 Anthropic 官方的 **Claude Code 插件系统**的完整配置、属性和技能（Skills）报告。该系统允许通过精选的插件和外部模型上下文协议（MCP）服务，大幅扩展 Claude 终端助手的代码生成、辅助开发、项目管理及集成测试能力。
* **English**: This report is a comprehensive configuration, properties, and skills report for the official **Claude Code Plugin System** by Anthropic. This ecosystem allows the extensive expansion of the Claude terminal assistant's code generation, developer operations, project management, and automated testing capabilities through curated internal plugins and external Model Context Protocol (MCP) servers.

---

## 3. 官方内部插件配置详情 / Official Internal Plugins Details

### 3.1 Plugin: `agent-sdk-dev`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/agent-sdk-dev](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/agent-sdk-dev) 
* **Description / 描述**:
  * **English**: Development kit for working with the Claude Agent SDK
  * **中文**: 开发 Claude Agent SDK 的开发套件工具。

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/new-sdk-app` | Create and setup a new Claude Agent SDK application | `None` |

---

### 3.2 Plugin: `clangd-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: C/C++ language server (clangd) for code intelligence
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `clangd` | `clangd` | `--background-index` | `.c, .h, .cpp, .cc, .cxx, .hpp, .hxx, .C, .H` |

---

### 3.3 Plugin: `claude-code-setup`
* **Category / 类别**: `productivity`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup) 
* **Description / 描述**:
  * **English**: Analyze codebases and recommend tailored Claude Code automations such as hooks, skills, MCP servers, and subagents.
  * **中文**: 分析当前项目代码库，并智能推荐适合本项目的 Claude Code 自动化配置，包括 Hooks、Skills、MCP 服务及子代理解决方案。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `claude-automation-recommender` | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use. | `plugins/claude-code-setup/skills/claude-automation-recommender` |

---

### 3.4 Plugin: `claude-md-management`
* **Category / 类别**: `productivity`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management) 
* **Description / 描述**:
  * **English**: Tools to maintain and improve CLAUDE.md files - audit quality, capture session learnings, and keep project memory current.
  * **中文**: 维护与提升 CLAUDE.md 文件的质量审计工具。可捕获对话中习得的最新经验，并在会话中对 CLAUDE.md 进行智能修补。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `claude-md-improver` | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization". | `plugins/claude-md-management/skills/claude-md-improver` |

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/revise-claude-md` | Update CLAUDE.md with learnings from this session | `Read, Edit, Glob` |

---

### 3.5 Plugin: `code-modernization`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-modernization) 
* **Description / 描述**:
  * **English**: Modernize legacy codebases (COBOL, legacy Java/C++, monolith web apps) with a structured assess / map / extract-rules / reimagine / transform / harden workflow and specialist review agents
  * **中文**: 遗产系统代码现代化升级。支持 COBOL、遗留 Java/C++ 及单体应用的解耦，涵盖从评估、设计、规则提取、重构到硬化运行的完整流程。

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/modernize-harden` | Security vulnerability scan with a reviewable remediation patch — OWASP, CWE, CVE, secrets, injection | `None` |
| `/modernize-map` | Dependency & topology mapping — call graphs, data lineage, batch flows, rendered as navigable diagrams | `None` |
| `/modernize-assess` | Full discovery & portfolio analysis of a legacy system — inventory, complexity, debt, effort estimation | `None` |
| `/modernize-reimagine` | Multi-agent greenfield rebuild — extract specs from legacy, design AI-native, scaffold & validate with HITL | `None` |
| `/modernize-transform` | Transform one legacy module to the target stack — idiomatic rewrite with behavior-equivalence tests | `None` |
| `/modernize-brief` | Generate a phased Modernization Brief — the approved plan that transformation agents will execute against | `None` |
| `/modernize-extract-rules` | Mine business logic from legacy code into testable, human-readable rule specifications | `None` |

---

### 3.6 Plugin: `code-review`
* **Category / 类别**: `productivity`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/code-review](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/code-review) 
* **Description / 描述**:
  * **English**: Automated code review for pull requests using multiple specialized agents with confidence-based scoring to filter false positives
  * **中文**: 基于多代理解析架构的拉取请求（PR）自动代码审查工具，支持可信度评分与自信度控制。

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/code-review` | Code review a pull request | `Bash(gh issue view:*), Bash(gh search:*), Bash(gh issue list:*), Bash(gh pr comment:*), Bash(gh pr diff:*), Bash(gh pr view:*), Bash(gh pr list:*)` |

---

### 3.7 Plugin: `code-simplifier`
* **Category / 类别**: `productivity`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier) 
* **Description / 描述**:
  * **English**: Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality. Focuses on recently modified code.
  * **中文**: 专用于简化和提炼代码以获得更高可读性、一致性和可维护性的重构助手，同时确保功能无损。

---

### 3.8 Plugin: `commit-commands`
* **Category / 类别**: `productivity`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/commit-commands](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/commit-commands) 
* **Description / 描述**:
  * **English**: Commands for git commit workflows including commit, push, and PR creation
  * **中文**: 集成 Git 流，快捷进行代码提交、推送到远端以及自动化创建 Pull Request。

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/clean_gone` | Cleans up all git branches marked as [gone] (branches that have been deleted on the remote but still exist locally), including removing associated worktrees. | `None` |
| `/commit-push-pr` | Commit, push, and open a PR | `Bash(git checkout --branch:*), Bash(git add:*), Bash(git status:*), Bash(git push:*), Bash(git commit:*), Bash(gh pr create:*)` |
| `/commit` | Create a git commit | `Bash(git add:*), Bash(git status:*), Bash(git commit:*)` |

---

### 3.9 Plugin: `csharp-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: C# language server for code intelligence
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `csharp-ls` | `csharp-ls` | `` | `.cs` |

---

### 3.10 Plugin: `cwc-makers`
* **Category / 类别**: `productivity`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://claude.com/cwc-makers](https://claude.com/cwc-makers) 
* **Description / 描述**:
  * **English**: Onboard a Code-with-Claude Makers Cardputer with one /maker-setup command — clones the build-with-claude repo, flashes UIFlow firmware, and installs the Claude Buddy app bundle.
  * **中文**: Code-with-Claude Cardputer 硬件快捷配置工具，克隆仓库、烧录 UIFlow 固件并写入助手应用包。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `m5-onboard` | End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash UIFlow 2.0 firmware, and install the Claude Buddy MicroPython app bundle. Use whenever the user plugs in or wants to flash/provision/reset an M5Stack or ESP32 board, or says "m5-onboard go". | `plugins/cwc-makers/skills/m5-onboard` |
| `cardputer-buddy` | Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command. Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /maker-setup. | `plugins/cwc-makers/skills/cardputer-buddy` |

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/maker-setup` | Onboard a Code-with-Claude Makers Cardputer — fetch the build-with-claude repo, flash firmware, and install the Claude Buddy apps. | `None` |

---

### 3.11 Plugin: `example-plugin`
* **Category / 类别**: `general`
* **Author / 作者**: Unknown
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: 
  * **中文**: 示范级插件实现，提供所有的扩展特性展示，包括指令、MCP 和技能注入。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `example-skill` | This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating Claude Code plugin skills. | `plugins/example-plugin/skills/example-skill` |
| `example-command` | An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout | `plugins/example-plugin/skills/example-command` |

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/example-command` | An example slash command that demonstrates command frontmatter options (legacy format) | `[Read, Glob, Grep, Bash]` |

---

### 3.12 Plugin: `explanatory-output-style`
* **Category / 类别**: `learning`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/explanatory-output-style](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/explanatory-output-style) 
* **Description / 描述**:
  * **English**: Adds educational insights about implementation choices and codebase patterns (mimics the deprecated Explanatory output style)
  * **中文**: 添加教育性见解，为生成代码和设计模式提供知识普及。

---

### 3.13 Plugin: `feature-dev`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/feature-dev](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/feature-dev) 
* **Description / 描述**:
  * **English**: Comprehensive feature development workflow with specialized agents for codebase exploration, architecture design, and quality review
  * **中文**: 全功能需求特征开发工作流插件，通过多个子代理完成架构审查、代码实现和质量检验。

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/feature-dev` | Guided feature development with codebase understanding and architecture focus | `None` |

---

### 3.14 Plugin: `frontend-design`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/frontend-design](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/frontend-design) 
* **Description / 描述**:
  * **English**: Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code that avoids generic AI aesthetics.
  * **中文**: 精细化前端界面构建与美学打磨工具，产出超高美感度及响应式的现代前端交互界面。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `frontend-design` | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics. | `plugins/frontend-design/skills/frontend-design` |

---

### 3.15 Plugin: `gopls-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Go language server for code intelligence and refactoring
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `gopls` | `gopls` | `` | `.go` |

---

### 3.16 Plugin: `hookify`
* **Category / 类别**: `productivity`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/hookify](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/hookify) 
* **Description / 描述**:
  * **English**: Easily create custom hooks to prevent unwanted behaviors by analyzing conversation patterns or from explicit instructions. Define rules via simple markdown files.
  * **中文**: 创建用于拦截和防范对话中不安全或错误指令的拦截器工具。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `writing-hookify-rules` | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns. | `plugins/hookify/skills/writing-rules` |

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/list` | List all configured hookify rules | `["Glob", "Read", "Skill"]` |
| `/configure` | Enable or disable hookify rules interactively | `["Glob", "Read", "Edit", "AskUserQuestion", "Skill"]` |
| `/help` | Get help with the hookify plugin | `["Read"]` |
| `/hookify` | Create hooks to prevent unwanted behaviors from conversation analysis or explicit instructions | `["Read", "Write", "AskUserQuestion", "Task", "Grep", "TodoWrite", "Skill"]` |

---

### 3.17 Plugin: `jdtls-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Java language server (Eclipse JDT.LS) for code intelligence
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `jdtls` | `jdtls` | `` | `.java` |

---

### 3.18 Plugin: `kotlin-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Kotlin language server for code intelligence
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `kotlin-lsp` | `kotlin-lsp` | `--stdio` | `.kt, .kts` |

---

### 3.19 Plugin: `learning-output-style`
* **Category / 类别**: `learning`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/learning-output-style](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/learning-output-style) 
* **Description / 描述**:
  * **English**: Interactive learning mode that requests meaningful code contributions at decision points (mimics the unshipped Learning output style)
  * **中文**: 交互式教学模式插件，允许 Claude 在关键代码设计决策节点主动请求用户的思考输入。

---

### 3.20 Plugin: `lua-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Lua language server for code intelligence
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `lua` | `lua-language-server` | `` | `.lua` |

---

### 3.21 Plugin: `math-olympiad`
* **Category / 类别**: `math`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-olympiad](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-olympiad) 
* **Description / 描述**:
  * **English**: Solve competition math (IMO, Putnam, USAMO) with adversarial verification that catches what self-verification misses. Fresh-context verifiers attack proofs with specific failure patterns. Calibrated abstention over bluffing.
  * **中文**: 面向高难度数学竞赛题（IMO、Putnam）的求解插件，通过对抗式校验和精细化的弃权逻辑防范大模型幻觉。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `math-olympiad` |  | `plugins/math-olympiad/skills/math-olympiad` |

---

### 3.22 Plugin: `mcp-server-dev`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev) 
* **Description / 描述**:
  * **English**: Skills for designing and building MCP servers that work seamlessly with Claude. Guides you through deployment models (remote HTTP, MCPB, local), tool design patterns, auth, and interactive MCP apps.
  * **中文**: 开发和设计 Model Context Protocol (MCP) 服务的全流程向导插件，包含工具设计、安全规范及远程部署开发模版。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `build-mcpb` | This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up. | `plugins/mcp-server-dev/skills/build-mcpb` |
| `build-mcp-app` | This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets. | `plugins/mcp-server-dev/skills/build-mcp-app` |
| `build-mcp-server` | This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills. | `plugins/mcp-server-dev/skills/build-mcp-server` |

---

### 3.23 Plugin: `php-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: PHP language server (Intelephense) for code intelligence
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `intelephense` | `intelephense` | `--stdio` | `.php` |

---

### 3.24 Plugin: `playground`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/playground](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/playground) 
* **Description / 描述**:
  * **English**: Creates interactive HTML playgrounds — self-contained single-file explorers with visual controls, live preview, and prompt output with copy button. Includes templates for design playgrounds, data explorers, concept maps, and document critique.
  * **中文**: 生成交互式单文件 HTML 演练场（Playground），包含可视化调试表单及快速复制输出组件。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `playground` | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic. | `plugins/playground/skills/playground` |

---

### 3.25 Plugin: `plugin-dev`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/plugin-dev](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/plugin-dev) 
* **Description / 描述**:
  * **English**: Comprehensive toolkit for developing Claude Code plugins. Includes 7 expert skills covering hooks, MCP integration, commands, agents, and best practices. AI-assisted plugin creation and validation.
  * **中文**: 官方提供的 Claude 插件开发套件，可直接从命令行构建 agents、skills、commands 和 hooks。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `mcp-integration` | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration. | `plugins/plugin-dev/skills/mcp-integration` |
| `agent-development` | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins. | `plugins/plugin-dev/skills/agent-development` |
| `plugin-structure` | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices. | `plugins/plugin-dev/skills/plugin-structure` |
| `skill-development` | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins. | `plugins/plugin-dev/skills/skill-development` |
| `plugin-settings` | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content. | `plugins/plugin-dev/skills/plugin-settings` |
| `command-development` | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code. | `plugins/plugin-dev/skills/command-development` |
| `hook-development` | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API. | `plugins/plugin-dev/skills/hook-development` |

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/create-plugin` | Guided end-to-end plugin creation workflow with component design, implementation, and validation | `` |

---

### 3.26 Plugin: `pr-review-toolkit`
* **Category / 类别**: `productivity`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/pr-review-toolkit](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/pr-review-toolkit) 
* **Description / 描述**:
  * **English**: Comprehensive PR review agents specializing in comments, tests, error handling, type design, code quality, and code simplification
  * **中文**: 合并请求（PR）评审核心工具箱，细化在边界安全、测试完整度、类型设计及代码简化等方面的专门审查代理。

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/review-pr` | "Comprehensive PR review using specialized agents" | `["Bash", "Glob", "Grep", "Read", "Task"]` |

---

### 3.27 Plugin: `pyright-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Python language server (Pyright) for type checking and code intelligence
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `pyright` | `pyright-langserver` | `--stdio` | `.py, .pyi` |

---

### 3.28 Plugin: `ralph-loop`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/ralph-loop](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/ralph-loop) 
* **Description / 描述**:
  * **English**: Interactive self-referential AI loops for iterative development, implementing the Ralph Wiggum technique. Claude works on the same task repeatedly, seeing its previous work, until completion.
  * **中文**: 实施 Ralph Wiggum 循环技术的自助脚本，使 Claude 在 while-true 机制下连续循环重试直到任务达成。

#### 支持斜杠命令 / Custom Slash Commands
| Command / 命令 | Description / 描述 | Allowed Tools / 允许调用的核心工具 |
| --- | --- | --- |
| `/cancel-ralph` | "Cancel active Ralph Loop" | `["Bash(test -f .claude/ralph-loop.local.md:*)", "Bash(rm .claude/ralph-loop.local.md)", "Read(.claude/ralph-loop.local.md)"]` |
| `/help` | "Explain Ralph Loop plugin and available commands" | `None` |
| `/ralph-loop` | "Start Ralph Loop in current session" | `["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/setup-ralph-loop.sh:*)"]` |

---

### 3.29 Plugin: `ruby-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Ruby language server for code intelligence and analysis
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `ruby-lsp` | `ruby-lsp` | `` | `.rb, .rake, .gemspec, .ru, .erb` |

---

### 3.30 Plugin: `rust-analyzer-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Rust language server for code intelligence and analysis
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `rust-analyzer` | `rust-analyzer` | `` | `.rs` |

---

### 3.31 Plugin: `security-guidance`
* **Category / 类别**: `security`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/plugins/security-guidance](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/security-guidance) 
* **Description / 描述**:
  * **English**: Security reminder hook that warns about potential security issues when editing files, including command injection, XSS, and unsafe code patterns
  * **中文**: 代码审计拦截钩子，在每次编辑文件时，若检测出命令注入、XSS、硬编码密钥等安全性风险，会弹框提示警报。

---

### 3.32 Plugin: `session-report`
* **Category / 类别**: `productivity`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report) 
* **Description / 描述**:
  * **English**: Generate an explorable HTML report of Claude Code session usage — tokens, cache efficiency, subagents, skills, and the most expensive prompts — from local ~/.claude/projects transcripts.
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `session-report` | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts. | `plugins/session-report/skills/session-report` |

---

### 3.33 Plugin: `skill-creator`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator) 
* **Description / 描述**:
  * **English**: Create new skills, improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, or benchmark skill performance with variance analysis.
  * **中文**: 技能（Skills）编辑器。专用于构建新 Skill、优化现有 Skill 和对系统 Prompt 性能进行统计基准评估。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `skill-creator` | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy. | `plugins/skill-creator/skills/skill-creator` |

---

### 3.34 Plugin: `swift-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Swift language server (SourceKit-LSP) for code intelligence
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `sourcekit-lsp` | `sourcekit-lsp` | `` | `.swift` |

---

### 3.35 Plugin: `typescript-lsp`
* **Category / 类别**: `development`
* **Author / 作者**: Anthropic (support@anthropic.com)
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: TypeScript/JavaScript language server for enhanced code intelligence
  * **中文**: 该插件可直接加载并注入到 Claude 的交互上下文中提供自动化增效支持。

#### LSP 语言服务器配置 / Language Server Configurations
| Server Name / 服务名 | Command / 启动命令 | Args / 参数 | Extensions / 支持后缀 |
| --- | --- | --- | --- |
| `typescript` | `typescript-language-server` | `--stdio` | `.ts, .tsx, .js, .jsx, .mts, .cts, .mjs, .cjs` |

---

## 4. 社区第三方插件配置详情 (MCP 驱动) / Community & Third-Party Plugins Details (MCP-Powered)

### 4.1 Plugin: `asana`
* **Category / 类别**: `productivity`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/asana](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/asana) 
* **Description / 描述**:
  * **English**: Asana project management integration. Create and manage tasks, search projects, update assignments, track progress, and integrate your development workflow with Asana's work management platform.
  * **中文**: Asana 项目任务管理系统连接器。支持创建、查询及更新任务状态。

---

### 4.2 Plugin: `context7`
* **Category / 类别**: `development`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/context7](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/context7) 
* **Description / 描述**:
  * **English**: Upstash Context7 MCP server for up-to-date documentation lookup. Pull version-specific documentation and code examples directly from source repositories into your LLM context.
  * **中文**: Upstash Context7 缓存集成，用于抓取实时仓库、版本信息文档。

---

### 4.3 Plugin: `discord`
* **Category / 类别**: `productivity`
* **Author / 作者**: Unknown
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Discord messaging bridge with built-in access control. Manage pairing, allowlists, and policy via /discord:access.
  * **中文**: Discord 聊天频道适配器，支持终端授权控制双向消息发送。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `configure` | Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status. | `external_plugins/discord/skills/configure` |
| `access` | Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Discord channel. | `external_plugins/discord/skills/access` |

---

### 4.4 Plugin: `fakechat`
* **Category / 类别**: `development`
* **Author / 作者**: Unknown
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Localhost web chat for testing the channel notification flow. No tokens, no access control, no third-party service.
  * **中文**: 本地极简测试版 iMessage-style 测试沙盒。

---

### 4.5 Plugin: `firebase`
* **Category / 类别**: `database`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/firebase](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/firebase) 
* **Description / 描述**:
  * **English**: Google Firebase MCP integration. Manage Firestore databases, authentication, cloud functions, hosting, and storage. Build and manage your Firebase backend directly from your development workflow.
  * **中文**: Google Firebase 平台 MCP。可管理 Firestore、托管和 Cloud Functions 云函数开发。

---

### 4.6 Plugin: `github`
* **Category / 类别**: `productivity`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github) 
* **Description / 描述**:
  * **English**: Official GitHub MCP server for repository management. Create issues, manage pull requests, review code, search repositories, and interact with GitHub's full API directly from Claude Code.
  * **中文**: 官方 GitHub 仓库管理器。可直接读写 Issue、提 PR、审计文件或访问 Git API 接口。

---

### 4.7 Plugin: `gitlab`
* **Category / 类别**: `productivity`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/gitlab](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/gitlab) 
* **Description / 描述**:
  * **English**: GitLab DevOps platform integration. Manage repositories, merge requests, CI/CD pipelines, issues, and wikis. Full access to GitLab's comprehensive DevOps lifecycle tools.
  * **中文**: GitLab CI/CD 与项目托管一站式集成开发连接器。

---

### 4.8 Plugin: `greptile`
* **Category / 类别**: `development`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/greptile](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/greptile) 
* **Description / 描述**:
  * **English**: AI-powered codebase search and understanding. Query your repositories using natural language to find relevant code, understand dependencies, and get contextual answers about your codebase architecture.
  * **中文**: 提供 Greptile AI 代码级问答与代码合并请求（PR）在线审查工具。

---

### 4.9 Plugin: `imessage`
* **Category / 类别**: `productivity`
* **Author / 作者**: Unknown
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: iMessage messaging bridge with built-in access control. Reads chat.db directly, sends via AppleScript. Manage pairing, allowlists, and policy via /imessage:access.
  * **中文**: iMessage 通道适配，通过读取 chat.db 自动检测信息并通过 AppleScript 发送信息。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `configure` | Check iMessage channel setup and review access policy. Use when the user asks to configure iMessage, asks "how do I set this up" or "who can reach me," or wants to know why texts aren't reaching the assistant. | `external_plugins/imessage/skills/configure` |
| `access` | Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the iMessage channel. | `external_plugins/imessage/skills/access` |

---

### 4.10 Plugin: `laravel-boost`
* **Category / 类别**: `development`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/laravel-boost](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/laravel-boost) 
* **Description / 描述**:
  * **English**: Laravel development toolkit MCP server. Provides intelligent assistance for Laravel applications including Artisan commands, Eloquent queries, routing, migrations, and framework-specific code generation.
  * **中文**: Laravel 专属开发增强套件，提供 Artisan 命令、Eloquent 生成和数据迁移向导。

---

### 4.11 Plugin: `linear`
* **Category / 类别**: `productivity`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/linear](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/linear) 
* **Description / 描述**:
  * **English**: Linear issue tracking integration. Create issues, manage projects, update statuses, search across workspaces, and streamline your software development workflow with Linear's modern issue tracker.
  * **中文**: Linear 项目与研发生命周期追踪器。提供极简、超快的 Bug、Issue 面板互通工具。

---

### 4.12 Plugin: `playwright`
* **Category / 类别**: `testing`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/playwright](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/playwright) 
* **Description / 描述**:
  * **English**: Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, click elements, and perform automated browser testing workflows.
  * **中文**: 微软官方浏览器端到端交互自动化测试 MCP。Claude 可控制真实浏览器页面进行元素点击、爬虫及截图验证。

---

### 4.13 Plugin: `serena`
* **Category / 类别**: `development`
* **Author / 作者**: Unknown
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/serena](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/serena) 
* **Description / 描述**:
  * **English**: Semantic code analysis MCP server providing intelligent code understanding, refactoring suggestions, and codebase navigation through language server protocol integration.
  * **中文**: Serena 语义代码分析与代码导航平台。

---

### 4.14 Plugin: `telegram`
* **Category / 类别**: `productivity`
* **Author / 作者**: Unknown
* **Homepage / 主页**: []() 
* **Description / 描述**:
  * **English**: Telegram messaging bridge with built-in access control. Manage pairing, allowlists, and policy via /telegram:access.
  * **中文**: Telegram 消息通道，内置远程终端会话配对和安全过滤策略。

#### 注入技能 / Injected Skills
| Skill Name / 技能名称 | Description / 技能描述 | Path / 相对路径 |
| --- | --- | --- |
| `configure` | Set up the Telegram channel — save the bot token and review access policy. Use when the user pastes a Telegram bot token, asks to configure Telegram, asks "how do I set this up" or "who can reach me," or wants to check channel status. | `external_plugins/telegram/skills/configure` |
| `access` | Manage Telegram channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Telegram channel. | `external_plugins/telegram/skills/access` |

---

### 4.15 Plugin: `terraform`
* **Category / 类别**: `development`
* **Author / 作者**: HashiCorp (support@hashicorp.com)
* **Homepage / 主页**: [https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/terraform](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/terraform) 
* **Description / 描述**:
  * **English**: The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.
  * **中文**: Terraform 基础设施即代码（IaC）自动化配置与状态验证插件。

---

## 5. 其他远程已注册插件摘要 / Registered Remote Plugins Summary

| Name / 插件名 | Category / 分类 | Description / 描述 |
| --- | --- | --- |
| `42crunch-api-security-testing` | `security` | Automate API security directly in Claude Code with 42Crunch - automatically audit OpenAPI specs, detect vulnerabilities aligned with OWASP API Security risks (including BOLA/BFLA), and apply AI-powered fixes. Designed for AI-assisted development workflows, it provides continuous guardrails through an audit->scan->remediate->validate loop, ensuring APIs meet enterprise security standards before deployment. |
| `adobe-for-creativity` | `design` | Harness Adobe's creative AI-powered tools to edit images, automate design workflows, and bring creative visions to life — from background removal to vectorization and professional retouching. |
| `agentforce-adlc` | `development` | Agentforce Agent Development Life Cycle — author, discover, scaffold, deploy, test, and optimize .agent files |
| `ai-plugins` | `general` | Set up endorctl and use Endor Labs to scan, prioritize, and fix security risks across your software supply chain |
| `aikido` | `general` | Aikido Security scanning for Claude Code — SAST, secrets, and IaC vulnerability detection powered by the Aikido MCP server. |
| `airtable` | `productivity` | Airtable is the database and operations layer for your agents — whether running product, marketing, sales, ops, HR, or a custom business app. It combines structured data with multiplayer visual surfaces (grid, kanban, calendar, gallery, timeline) humans and agents share — plus sync integrations to Jira, Salesforce, Zendesk, Google Drive, Databricks, and the rest of your stack, all backed by enterprise governance. This plugin makes Claude fluent in Airtable: creating bases and schema, working with records, and sharing UI for collaboration. Bundles the official Airtable MCP server. |
| `alloydb` | `database` | Create, connect, and interact with an AlloyDB for PostgreSQL database and data. |
| `amazon-location-service` | `location` | Guide developers through adding maps, places search, geocoding, routing, and other geospatial features with Amazon Location Service, including authentication setup, SDK integration, and best practices. |
| `amplitude` | `monitoring` | Use Amplitude as an expert analyst — instrument Amplitude, discover product opportunities, analyze charts, create dashboards, manage experiments, and understand users and accounts. |
| `apollo` | `productivity` | Prospect, enrich leads, load outreach sequences, and query sales analytics with Apollo.io — one-click MCP server integration for Claude Code and Cowork. |
| `astronomer-data-agents` | `development` | Data engineering for Apache Airflow and Astronomer. Author DAGs with best practices, debug pipeline failures, trace data lineage, profile tables, migrate Airflow 2 to 3, and manage local and cloud deployments. |
| `atlan` | `general` | Atlan data catalog plugin for Claude Code. Search, explore, govern, and manage your data assets through natural language. Powered by the Atlan MCP server with semantic search, lineage traversal, glossary management, data quality rules, and more. |
| `atlassian` | `productivity` | Connect to Atlassian products including Jira and Confluence. Search and create issues, access documentation, manage sprints, and integrate your development workflow with Atlassian's collaboration tools. |
| `atomic-agents` | `development` | Comprehensive development workflow for building AI agents with the Atomic Agents framework. Includes specialized agents for schema design, architecture planning, code review, and tool development. Features guided workflows, progressive-disclosure skills, and best practice validation. |
| `auth0` | `security` | Add authentication to any app with Auth0. This plugin detects your framework, scaffolds the right Auth0 SDK integration, and guides you through login, logout, sessions, and protected routes — using current SDK patterns. |
| `aws-agents` | `development` | Build, deploy, and operate AI agents on AWS. Skills for scaffolding agents with Amazon Bedrock AgentCore, connecting tools, memory, policies, evaluation, debugging, and production hardening. |
| `aws-amplify` | `development` | Build full-stack apps with AWS Amplify Gen 2 using guided workflows for authentication, data models, storage, GraphQL APIs, and Lambda functions. |
| `aws-core` | `development` | Build, deploy, and operate applications on AWS. Skills to author infrastructure-as-code, use core services, and complete common tasks. |
| `aws-data-analytics` | `development` | Data lake, analytics, and ETL workflows with S3 Tables, AWS Glue, and Athena. |
| `aws-dev-toolkit` | `development` | AWS development toolkit — 34 skills, 11 agents, and 3 MCP servers for building, migrating, and performing architecture reviews on AWS. |
| `aws-serverless` | `development` | Design, build, deploy, test, and debug serverless applications with AWS Serverless services. |
| `azure` | `deployment` | Transform Claude into an Azure expert. This plugin integrates the Azure MCP server and specialized Azure skills to move beyond generic advice. It enables Claude to perform real-world tasks: listing resources, validating deployments, diagnosing infrastructure issues, and optimizing costs across 50+ Azure services. |
| `azure-cosmos-db-assistant` | `database` | Expert assistant for Azure Cosmos DB — data modeling, query optimization, performance tuning, and best practices. |
| `base44` | `development` | Build and deploy Base44 full-stack apps with CLI project management and JavaScript/TypeScript SDK development skills |
| `bigdata-com` | `database` | Official Bigdata.com plugin providing financial research, analytics, and intelligence tools powered by Bigdata MCP. |
| `box` | `productivity` | Work with your Box content directly from Claude Code — search files, organize folders, collaborate with your team, and use Box AI to answer questions, summarize documents, and extract data without leaving your workflow. |
| `brightdata-plugin` | `general` | Web scraping, Google search, structured data extraction, and MCP server integration powered by Bright Data. Includes 7 skills: scrape any webpage as markdown (with bot detection/CAPTCHA bypass), search Google with structured JSON results, extract data from 40+ websites (Amazon, LinkedIn, Instagram, TikTok, YouTube, and more), orchestrate Bright Data's 60+ MCP tools, built-in best practices for Web Unlocker, SERP API, Web Scraper API, and Browser API, Python SDK best practices for the brightda... |
| `carta-cap-table` | `productivity` | Carta Cap Table plugin — skills and hooks for querying cap tables, grants, SAFEs, 409A valuations, waterfall scenarios, and more |
| `cds-mcp` | `development` | AI-assisted development of SAP Cloud Application Programming Model (CAP) projects. Search CDS models and CAP documentation. |
| `chrome-devtools-mcp` | `development` | Control and inspect a live Chrome browser from your coding agent. Record performance traces, analyze network requests, check console messages with source-mapped stack traces, and automate browser actions with Puppeteer. |
| `circleback` | `productivity` | Circleback conversational context integration. Search and access meetings, emails, calendar events, and more. |
| `clickhouse` | `database` | Connect Claude to your ClickHouse Cloud databases. Browse organizations, services, databases, and table schemas. Run read-only SQL queries against your data and get instant analytical answers. Monitor service backups, review billing costs, and inspect ClickPipe configurations - all through natural conversation. |
| `cloud-sql-postgresql` | `database` | Create, connect, and interact with a Cloud SQL for PostgreSQL database and data. |
| `cloudflare` | `deployment` | Skills for the Cloudflare developer platform: Workers, Durable Objects, Agents SDK, MCP servers, Wrangler CLI, and web performance. |
| `cloudinary` | `general` | Use Cloudinary directly in Claude. Manage assets, apply transformations, optimize media, and more through natural conversation. |
| `cockroachdb` | `database` | Connect Claude Code directly to your CockroachDB clusters for hands-on database work — explore schemas, write optimized SQL, debug queries, and manage distributed database clusters. This plugin provides 14 tools across two active MCP backends (self-hosted MCP Toolbox and managed CockroachDB Cloud MCP Server), three specialized agents (DBA, Developer, Operator), 32 skills across 6 operational domains, and built-in safety hooks. |
| `coderabbit` | `productivity` | Your code review partner. CodeRabbit provides external validation using a specialized AI architecture and 40+ integrated static analyzers—offering a different perspective that catches bugs, security vulnerabilities, logic errors, and edge cases. Context-aware analysis via AST parsing and codegraph relationships. Automatically incorporates CLAUDE.md and project coding guidelines into reviews. Useful after writing or modifying code, before commits, when implementing complex or security-sensitive logic, or when a second opinion would increase confidence in the changes. Returns specific findings with suggested fixes that can be applied immediately. Free to use. |
| `crowdstrike-falcon-foundry` | `security` | CrowdStrike Falcon Foundry development skills for building cybersecurity applications on the Falcon platform. Includes UI development, collections, functions, workflows, API integration, security patterns, and debugging workflows. |
| `dash0` | `monitoring` | OpenTelemetry observability for Claude Code sessions. Captures tool calls, LLM invocations, token usage, and errors as OTel traces. Send telemetry to Dash0 or any OpenTelemetry-compatible backend. |
| `data` | `development` | Data engineering for Apache Airflow and Astronomer. Author DAGs with best practices, debug pipeline failures, trace data lineage, profile tables, migrate Airflow 2 to 3, and manage local and cloud deployments. |
| `data-agent-kit-starter-pack` | `development` | This plugin provides a specialized suite of skills for data engineers and database practitioners working on Google Cloud. It acts as an expert assistant, allowing you to use natural language prompts in your preferred coding agent to architect complex data pipelines, transform data with dbt, write Spark and BigQuery SQL notebooks, and orchestrate end-to-end workflows across GCP's data ecosystem. |
| `data-engineering` | `general` | Data engineering plugin - warehouse exploration, pipeline authoring, Airflow integration |
| `databases-on-aws` | `database` | Expert database guidance for the AWS database portfolio. Design schemas, execute queries, handle migrations, and choose the right database for your workload. |
| `datadog` | `monitoring` | Use Datadog directly in Claude Code through a preconfigured Datadog MCP server. Query logs, metrics, traces, dashboards, and more through natural conversation. This plugin is in preview. |
| `datarobot-agent-skills` | `development` | DataRobot skills for AI/ML workflows — model training, deployment, predictions, feature engineering, monitoring, explainability, data preparation, App Framework CI/CD, and external agent monitoring. |
| `dataverse` | `database` | Agent skills for building on, analyzing, and managing Microsoft Dataverse — with Dataverse MCP, PAC CLI, and Python SDK. |
| `deploy-on-aws` | `deployment` | Deploy applications to AWS with architecture recommendations, cost estimates, and IaC deployment. |
| `desktop-commander` | `productivity` | MCP server for terminal commands, process management, and file operations across text, code, PDF, DOCX, Excel, images, and structured data. |
| `exa` | `productivity` | Exa AI web search, deep research, and content extraction. Provides MCP tools and research skills for comprehensive web search, people discovery, company research, academic papers, and more. |
| `expo` | `development` | Official Expo skills for building, deploying, upgrading, and debugging React Native apps with Expo. Covers UI development with Expo Router, SwiftUI and Jetpack Compose components, Tailwind CSS setup, API routes, data fetching, CI/CD workflows, App Store and Play Store deployment, SDK upgrades, DOM components, and dev client distribution. |
| `fastly-agent-toolkit` | `general` | Fastly development tools and platform skills |
| `fiftyone` | `general` | Build high-quality datasets and computer vision models. Visualize datasets, analyze models, find duplicates, run inference, evaluate predictions, and develop custom plugins. |
| `figma` | `design` | Figma design platform integration. Access design files, extract component information, read design tokens, and translate designs into code. Bridge the gap between design and development workflows. |
| `firecrawl` | `development` | Web scraping and crawling powered by Firecrawl. Turn any website into clean, LLM-ready markdown or structured data. Scrape single pages, crawl entire sites, search the web, and extract structured information. Includes an AI agent for autonomous multi-source data gathering - just describe what you need and it finds, navigates, and extracts automatically. |
| `fullstory` | `monitoring` | Connect Claude to Fullstory to query behavioral analytics, session replays, and customer experience insights. |
| `huggingface-skills` | `development` | Build, train, evaluate, and use open source AI models, datasets, and spaces. |
| `intercom` | `productivity` | Intercom integration for Claude Code. Search conversations, analyze customer support patterns, look up contacts and companies, and install the Intercom Messenger. Connect your Intercom workspace to get real-time insights from customer data. |
| `jfrog` | `security` | Use the JFrog Platform from Claude Code: Artifactory repos and artifacts, security findings and exposures, Catalog package safety and downloads, workflows across the SDLC, and platform administration. |
| `legalzoom` | `productivity` | Attorney guidance and legal tools for business and personal needs. AI-powered document review identifies critical risks and important clauses, advises when to engage an attorney, and routes to LegalZoom's network when professional expertise is needed. |
| `liquid-lsp` | `development` | LSP integration for Shopify Liquid templates via the Shopify CLI theme language server. |
| `liquid-skills` | `development` | Liquid language fundamentals, CSS/JS/HTML coding standards, and WCAG accessibility patterns for Shopify themes |
| `logfire` | `monitoring` | Add Logfire observability to Python applications with auto-instrumentation for FastAPI, httpx, asyncpg, SQLAlchemy, and more |
| `mercadopago` | `development` | Mercado Pago full-product integration toolkit. Covers online checkout (Pro, Bricks, API), in-store (QR, Point), subscriptions, marketplace, wallet, money-out, security (3DS, PCI), reporting, SDKs, and specialized integrations. Hybrid architecture: 13 skills provide stable integration intelligence, MCP provides live API data. |
| `microsoft-docs` | `development` | Access official Microsoft documentation, API references, and code samples for Azure, .NET, Windows, and more. |
| `mintlify` | `development` | Build beautiful documentation sites with Mintlify. Convert non-markdown files into properly formatted MDX pages, add and modify content with correct component use, and automate documentation updates. |
| `miro` | `design` | Secure access to Miro boards. Enables AI to read board context, create diagrams, and generate code with enterprise-grade security. |
| `mongodb` | `database` | Official Claude plugin for MongoDB (MCP Server + Skills). Connect to databases, explore data, manage collections, optimize queries, generate reliable code, implement best practices, develop advanced features, and more. |
| `neon` | `database` | Manage your Neon projects and databases with the neon-postgres agent skill and the Neon MCP Server. |
| `netlify-skills` | `development` | Netlify platform skills for Claude Code — functions, edge functions, blobs, database, image CDN, forms, config, CLI, frameworks, caching, AI gateway, and deployment. |
| `netsuite-suitecloud` | `development` | NetSuite agent skills from Oracle — authoring guidance for SuiteCloud Development Framework (SDF) objects and UIF single-page-app components, plus runtime guidance for the NetSuite AI Service Connector. |
| `nightvision` | `general` | Skills for working with NightVision, a DAST and API Discovery platform that finds exploitable vulnerabilities in web applications and REST APIs |
| `nimble` | `general` | Nimble web data toolkit — search, extract, map, crawl the web and work with structured data agents |
| `notion` | `productivity` | Notion workspace integration. Search pages, create and update documents, manage databases, and access your team's knowledge base directly from Claude Code for seamless documentation workflows. |
| `oracle-ai-data-platform-workbench-spark-connectors` | `development` | Oracle AI Data Platform Workbench Spark connectors for Claude Code. 18 connector skills covering every data source workbench customers commonly need: Oracle Autonomous DB family (ALH/ADW/ATP) via wallet/IAM-DB-Token/API-key, ExaCS, Fusion ERP REST, Fusion BICC, EPM Cloud Planning, Essbase 21c, OCI Streaming (Kafka), OCI Object Storage, Apache Iceberg, plus external systems (PostgreSQL, MySQL/HeatWave, SQL Server, Snowflake, Azure ADLS Gen2, AWS S3, generic REST, custom JDBC, Excel). Live-validated on the workbench `tpcds` cluster (Spark 3.5.0): 17 PASS / 4 ship-as-is out of 21 test rows. |
| `outputai` | `development` | Output.ai workflow development toolkit for Claude Code. Adds 5 specialist agents (planner, builder, debugger, prompt writer, quality reviewer), 40+ slash-command skills covering scaffolding, debugging, evaluation, and credential management, plus a SessionStart hook that auto-loads Output SDK conventions so Claude understands the framework before the first prompt. |
| `pagerduty` | `monitoring` | Enhance code quality and security through PagerDuty risk scoring and incident correlation. Score pre-commit diffs against historical incident data and surface deployment risk before you ship. |
| `pigment` | `productivity` | Analyze business data and build custom Pigment models, metrics, and boards through natural language. |
| `pinecone` | `database` | Pinecone vector database integration. Streamline your Pinecone development with powerful tools for managing vector indexes, querying data, and rapid prototyping. Use slash commands like /quickstart to generate AGENTS.md files and initialize Python projects and /query to quickly explore indexes. Access the Pinecone MCP server for creating, describing, upserting and querying indexes with Claude. Perfect for developers building semantic search, RAG applications, recommendation systems, and other vector-based applications with Pinecone. |
| `planetscale` | `database` | An authenticated hosted MCP server that accesses your PlanetScale organizations, databases, branches, schema, and Insights data. Query against your data, surface slow queries, and get organizational and account information. |
| `posthog` | `monitoring` | Access PostHog analytics, feature flags, experiments, error tracking, and insights directly from Claude Code. |
| `postiz` | `general` | Social media automation CLI for scheduling posts, managing integrations, uploading media, and tracking analytics across 28+ platforms including X, LinkedIn, Reddit, YouTube, TikTok, Instagram, and more |
| `postman` | `development` | Full API lifecycle management for Claude Code. Sync collections, generate client code, discover APIs, run tests, create mocks, publish docs, and audit security. Powered by the Postman MCP Server. |
| `prisma` | `general` | Prisma MCP integration for Postgres database management, schema migrations, SQL queries, and connection string management. Provision Prisma Postgres databases, run migrations, and interact with your data directly. |
| `pydantic-ai` | `development` | Write accurate Pydantic AI code from the start. Up-to-date patterns, decision trees, and common gotchas for agents, tools, structured output, streaming, and multi-agent apps. |
| `qdrant-skills` | `database` | Agent skills for Qdrant vector search covering scaling, performance optimization, search quality, monitoring, deployment, model migration, version upgrades, and SDK usage across Python, TypeScript, Rust, Go, .NET, and Java. |
| `qodo-skills` | `development` | Qodo Skills provides a curated library of reusable AI agent capabilities that extend Claude's functionality for software development workflows. Each skill is designed to integrate seamlessly into your development process, enabling tasks like code quality checks, automated testing, security scanning, and compliance validation. Skills operate across your entire SDLC—from IDE to CI/CD—ensuring consistent standards and catching issues early. |
| `qt-development-skills` | `development` | Agentic engineering skills for Qt software development — Qt C++/QML code review, QML coding, and Qt C++/QML code documentation. |
| `quarkus-agent` | `development` | MCP server for AI coding agents to create, manage, and interact with Quarkus applications. Provides tools for project scaffolding, dev mode lifecycle, extension skills, Dev MCP proxy, and documentation search. |
| `railway` | `deployment` | Deploy and manage apps, databases, and infrastructure on Railway. Covers project setup, deploys, environment configuration, networking, troubleshooting, and monitoring. |
| `rc` | `development` | Configure RevenueCat projects, apps, products, entitlements, and offerings directly from Claude Code. Manage your in-app purchase backend without leaving your development workflow. |
| `remember` | `general` | Continuous memory for Claude Code. Extracts, summarizes, and compresses conversations into tiered daily logs. Claude remembers what you did yesterday. |
| `revenuecat` | `development` | Configure RevenueCat projects, apps, products, entitlements, and offerings directly from Claude Code. Manage your in-app purchase backend without leaving your development workflow. |
| `sanity` | `development` | Sanity content platform integration with MCP server, agent skills, and slash commands. Query and author content, build and optimize GROQ queries, design schemas, and set up Visual Editing. |
| `sap-cds-mcp` | `development` | AI-assisted development of SAP Cloud Application Programming Model (CAP) projects. Search CDS models and CAP documentation. |
| `sap-fiori-mcp-server` | `development` | MCP server for SAP Fiori development tools for Claude Code. Build and modify SAP Fiori applications with AI assistance. |
| `sap-mdk-server` | `development` | MCP server for SAP Mobile Development Kit (MDK). Build and modify MDK applications with AI assistance — schema lookups, action validation, rule editing, and project scaffolding. |
| `semgrep` | `security` | Semgrep catches security vulnerabilities in real-time and guides Claude to write secure code from the start. |
| `sentry` | `monitoring` | Sentry error monitoring integration. Access error reports, analyze stack traces, search issues by fingerprint, and debug production errors directly from your development environment. |
| `servicenow-sdk` | `development` | Create, edit, and deploy ServiceNow applications with the Fluent SDK effortlessly through Claude AI. |
| `shopify` | `development` | Shopify developer tools for Claude Code — search Shopify docs, generate and validate GraphQL, Liquid, and UI extension code |
| `shopify-ai-toolkit` | `development` | Shopify's AI Toolkit provides 18 development skills for building on the Shopify platform, covering documentation search, API schema access, GraphQL and Liquid code validation, Hydrogen storefronts, Polaris UI extensions, store management via CLI, and onboarding guidance for both developers and merchants. |
| `slack` | `productivity` | Slack workspace integration. Search messages, access channels, read threads, and stay connected with your team's communications while coding. Find relevant discussions and context quickly. |
| `snowflake-cortex-code` | `development` | Automatically route Snowflake prompts from Claude Code to Cortex Code for execution. Provides slash commands for code review and task delegation, plus skills for routing, run, and setup. |
| `sonarqube` | `security` | Automatically enforce SonarQube code quality and security in the agent coding loop — 7,000+ rules, secrets scanning, agentic analysis, and quality gates across 40+ languages. PostToolUse hooks run analysis after every file edit. Pre-tool secrets scanning prevents 450+ patterns from reaching the LLM. Slash commands give on-demand access to quality gate status, coverage, duplication, and dependency risks. Includes SonarQube CLI, MCP Server, skills, hooks, and slash commands. |
| `sonatype-guide` | `security` | Sonatype Guide MCP server for software supply chain intelligence and dependency security. Analyze dependencies for vulnerabilities, get secure version recommendations, and check component quality metrics. |
| `sourcegraph` | `development` | Code search and understanding across codebases. Search, read, and trace references across repositories; analyze refactor impact; investigate incidents via commit and diff search; run targeted security sweeps. |
| `spotify-ads-api` | `productivity` | Manage Spotify ad campaigns with natural language. Create campaigns, ad sets, ads, pull reports, and handle OAuth — all through conversation. |
| `stripe` | `development` | Stripe development plugin for Claude |
| `sumup` | `development` | SumUp payment integrations across terminal and online checkout flows. Build Android and iOS POS apps with SumUp card readers, online checkout with server SDKs and the checkout widget, and control card readers remotely via Cloud API. |
| `supabase` | `database` | Supabase MCP integration for database operations, authentication, storage, and real-time subscriptions. Manage your Supabase projects, run SQL queries, and interact with your backend directly. |
| `superpowers` | `development` | Superpowers teaches Claude brainstorming, subagent driven development with built in code review, systematic debugging, and red/green TDD. Additionally, it teaches Claude how to author and test new skills. |
| `twilio-developer-kit` | `development` | Twilio Skills provide procedural knowledge for AI coding agents — which APIs to use, in what order, and what to avoid. Covers SMS, Voice, WhatsApp, Verify, SendGrid, Compliance, and 30+ products. |
| `ui5` | `development` | SAPUI5 / OpenUI5 plugin for Claude. Create and validate UI5 projects, access API documentation, run UI5 linter, get development guidelines and best practices for UI5 development. |
| `ui5-typescript-conversion` | `development` | SAPUI5 / OpenUI5 plugin for Claude. Convert JavaScript based UI5 projects to TypeScript. |
| `vanta-mcp-plugin` | `security` | The Vanta plugin connects Claude Code to Vanta's security and compliance platform through the Vanta MCP server. It combines Vanta's test-specific remediation intelligence with your local repository context to help you fix compliance failures faster. |
| `vercel` | `deployment` | Vercel deployment platform integration. Manage deployments, check build status, access logs, configure domains, and control your frontend infrastructure directly from Claude Code. |
| `windsor-ai` | `productivity` | Connect Claude Code to 325+ business data sources via Windsor.ai. Query marketing, sales, CRM, ecommerce, finance, and analytics data from Google Ads, Meta, HubSpot, Salesforce, Shopify, Stripe, and hundreds more — directly from your terminal. |
| `wix` | `development` | Build, manage, and deploy Wix sites and apps. CLI development skills for dashboard extensions, backend APIs, site widgets, and service plugins with the Wix Design System, plus MCP server for site management. |
| `wordpress.com` | `general` | Uses Claude Code to create and edit WordPress sites with WordPress Studio before deploying changes to your WordPress.com site. |
| `youdotcom-agent-skills` | `productivity` | You.com agent skills for web search, research with citations, and content extraction. Guided integrations for Vercel AI SDK, Claude Agent SDK, OpenAI Agents SDK, crewAI, LangChain, Microsoft Teams.ai, direct REST API, and bash CLI. |
| `zapier` | `productivity` | Connect 8,000+ apps to your AI workflow. Discover, enable, and execute Zapier actions directly from your client. |
| `zilliz` | `database` | Zilliz Cloud management plugin with 14 skills covering cluster lifecycle, collection schema, vector search, index tuning, bulk import, RBAC, backups, and monitoring. |
| `zoom-plugin` | `development` | Claude plugin for planning, building, and debugging Zoom integrations across REST APIs, SDKs, webhooks, bots, and MCP workflows. |
| `zscaler` | `security` | Manage Zscaler cloud security platform including ZPA (private access), ZIA (internet access), ZDX (digital experience), ZCC (client connector), EASM (attack surface), and Z-Insights (analytics). Create and manage policies, troubleshoot connectivity, audit security configurations, and investigate incidents across the full Zscaler ecosystem. |


---

*End of Report. Generated by Antigravity AI.*