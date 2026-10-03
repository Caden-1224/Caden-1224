<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-motion-dark.svg">
  <img src="./assets/banner-motion.svg" alt="Caden · EE → CS · 从信号到系统，继续往下看一层" width="100%">
</picture>

<p align="right">
  <strong>中文</strong> &nbsp; / &nbsp; <a href="./README.en.md">English</a>
</p>

<p align="center">
  <strong>通信工程在读 · 嵌入式 · Linux · 端侧 AI</strong><br>
  从嵌入式走向计算机系统
</p>

## 👋 你好，我是 Caden

我读通信工程，从单片机和外设做起，现在主要在 Linux 上做多进程与端侧推理。把做过的东西摆在一起看，大致是一条线：先让一个功能在板子上跑起来，再去弄明白它背后的调度、通信和资源是怎么被安排的。

我喜欢顺着问题往下看一层：数据在哪里等？取消之后，旧结果为什么还会回来？一个进程退出，会影响系统的哪一部分？嵌入式的经历让我对时序、内存和硬件约束比较敏感，现在想把软件这一侧也弄明白——预算怎么算、边界画在哪、出错时谁能兜住。

🎯 **现在的主线是计算机系统。** EE 给了我信号、时序和硬件约束的直觉，CS 让我想把这些放回系统里看。一边补基础，一边把理解放进项目里验证；长期想往 GPU 与系统软件方向走。

我做事的习惯是先跑通一个小切片，再用测试、日志和文档把结论固定下来——包括没做到的部分。写过的东西都在这个账号的仓库里。

## 🧰 技术栈

**编程与系统**

- **C / C++17**：裸机与驱动层的 C（最近的工业终端项目自研约 1.5 万行）、C++17 的模块划分与接口设计
- **Linux 系统与网络编程**：多进程、epoll / Reactor 事件驱动、TCP / NDJSON、ZeroMQ 通信、跨进程取消与资源清理
- **Python / Shell**：脚本、构建与验证工具链

**嵌入式**

- **平台**：GD32F4xx（GD32F470VE）、STM32F4；Keil MDK，标准外设库与 HAL
- **外设与机制**：UART / RS485 / SPI / I²C、DMA 与环形缓冲、中断与非阻塞状态机、Timer / RTC、内部 Flash 与 SPI Flash
- **系统能力**：BootLoader 与 OTA（分区、CRC32、备份与回滚、向量表跳转）、参数掉电保存、协作式时间片调度
- **联调与部署**：寄存器级驱动、软硬件联调，Linux aarch64 板端部署（RK3576）

**工程与工具**

- CMake / CTest、Git、Docker、GitHub Actions
- MATLAB、OpenCV 几何视觉、ROS 2；深度学习基础与 PyTorch（基础）

**工作方式**

- 规格驱动 + 测试驱动：先把需求写成规格、接口契约与验收标准，再落实现与回归
- 用 AI 编程工具（Claude Code、MCP）做项目级上下文接入、代码阅读、方案拆解与补丁验证，留下可追溯的规格与变更记录

<!-- Theme-aware SVG assets are stored in this repository. -->
<div align="center">

<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-0-night.svg"><img src="./assets/chips/label-0.svg" alt="Languages &amp; Systems" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/c-night.svg"><img src="./assets/chips/c.svg" alt="C" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/cplusplus-night.svg"><img src="./assets/chips/cplusplus.svg" alt="C++" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/python-night.svg"><img src="./assets/chips/python.svg" alt="Python" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/gnubash-night.svg"><img src="./assets/chips/gnubash.svg" alt="Shell" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/linux-night.svg"><img src="./assets/chips/linux.svg" alt="Linux" height="30"></picture>
<br/>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-1-night.svg"><img src="./assets/chips/label-1.svg" alt="Embedded" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/gd32-night.svg"><img src="./assets/chips/gd32.svg" alt="GD32" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/stmicroelectronics-night.svg"><img src="./assets/chips/stmicroelectronics.svg" alt="STM32" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/arm-night.svg"><img src="./assets/chips/arm.svg" alt="ARM" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/rtos-night.svg"><img src="./assets/chips/rtos.svg" alt="RTOS" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/bus-night.svg"><img src="./assets/chips/bus.svg" alt="Serial Bus" height="30"></picture>
<br/>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-2-night.svg"><img src="./assets/chips/label-2.svg" alt="Build &amp; Runtime" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/cmake-night.svg"><img src="./assets/chips/cmake.svg" alt="CMake" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/zeromq-night.svg"><img src="./assets/chips/zeromq.svg" alt="ZeroMQ" height="30"></picture>
<br/>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-3-night.svg"><img src="./assets/chips/label-3.svg" alt="Engineering &amp; Collaboration" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/git-night.svg"><img src="./assets/chips/git.svg" alt="Git" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/docker-night.svg"><img src="./assets/chips/docker.svg" alt="Docker" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/githubactions-night.svg"><img src="./assets/chips/githubactions.svg" alt="GitHub Actions" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/claude-night.svg"><img src="./assets/chips/claude.svg" alt="Claude Code" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/modelcontextprotocol-night.svg"><img src="./assets/chips/modelcontextprotocol.svg" alt="MCP" height="30"></picture>

<br/>
<sub>其他探索：</sub> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/opencv-night.svg"><img src="./assets/chips/opencv.svg" alt="OpenCV" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/ros-night.svg"><img src="./assets/chips/ros.svg" alt="ROS 2" height="30"></picture>

</div>

<br/>

<!-- ============ Sky ============ -->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/sky-night.svg" />
    <img src="./assets/sky.svg" width="100%" alt="" />
  </picture>
</div>

## 📊 公开的记录

<!-- Public owned, non-fork repositories; refreshed by profile-assets.yml. -->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/stats-dark.svg" />
    <img width="640" src="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/stats.svg" alt="Caden-1224 的公开非 fork 仓库：Star 总数、本人 commit 数与仓库数" />
  </picture>
</div>

<p align="center"><sub>仅统计本人名下的公开非 fork 仓库；commit 数为各仓库当前默认分支历史中本人提交的累计数量。<br>计划每 10 分钟刷新，实际更新时间见卡片。<br><a href="https://github.com/Caden-1224/Caden-1224/actions/workflows/profile-assets.yml">查看同步状态</a></sub></p>

<!-- Contribution animation is published independently from the stats card. -->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/github-contribution-grid-snake-dark.svg" />
    <img width="100%" alt="GitHub 最近一年的贡献日历动画" src="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/github-contribution-grid-snake.svg" />
  </picture>
</div>

---

💬 如果你也在学系统、折腾嵌入式，或者同样在从 EE 往 CS 走，欢迎来聊聊。

[Email](mailto:seekercaden@outlook.com) &nbsp; · &nbsp; [GitHub](https://github.com/Caden-1224)
