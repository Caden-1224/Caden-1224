<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-motion-dark.svg">
  <img src="./assets/banner-motion.svg" alt="Caden · EE → CS · 从信号到系统，继续往下看一层" width="100%">
</picture>

<p align="right">
  <strong>中文</strong> &nbsp; / &nbsp; <a href="./README.en.md">English</a>
</p>

<p align="center">
  <strong>通信工程在读 · 嵌入式 · Linux · 端侧 AI</strong><br>
  从一个信号如何被采集，到一项任务如何被可靠地执行。
</p>

## 👋 你好，我是 Caden

我从通信工程出发，正在一步步走向计算机系统。最早和单片机、外设打交道，后来开始在 Linux 上做多进程和端侧推理项目。兴趣也从“让一个功能跑起来”，延伸到它背后的调度、通信和资源管理。

我喜欢顺着问题往下看一层：数据在哪里等待？取消之后，旧结果为什么还会回来？一个进程退出，会影响系统的哪一部分？嵌入式的经历让我对时序、内存和硬件约束比较敏感，现在想把软件这一侧也弄明白。

🎯 **现在的主线是计算机系统。** EE 给了我信号、时序和硬件约束的直觉，CS 让我想把这些放回系统里看。一边补基础，一边把理解放进项目里验证；长期想往 GPU 与系统软件方向走。

## 🛠️ 项目 · 从板端到系统

这三个项目记录了我从外设与任务调度，走向多进程通信、再到任务运行时的过程。

### [NexWeave](https://github.com/Caden-1224/nexweave)

<sub>🚧 <b>持续开发</b> &nbsp; / &nbsp; C++17 · Linux · ZeroMQ · CMake / CTest</sub>

面向 Linux 边缘设备的任务框架。把会话生命周期、流式数据、取消和后端接入放进一套明确的执行契约，让模型与设备能够协同工作。

- **关注的问题**：有界缓冲、跨进程取消、旧结果隔离，以及任务结束后的资源清理。
- **目前的边界**：已用确定性模拟后端验证 Linux 多进程链路；真实模型、音频设备与 RK3576 适配尚未完成。

[查看源码](https://github.com/Caden-1224/nexweave) &nbsp; · &nbsp; [当前进展与路线图](https://github.com/Caden-1224/nexweave#status)

### [VoxOrchestra](https://github.com/Caden-1224/voxorchestra-system)

<sub>✅ <b>板端已验证</b> &nbsp; / &nbsp; C++17 · TCP / ZeroMQ · RK3576 · 离线推理</sub>

在 RK3576 泰山派 3M 上验证的全离线语音系统，将 **ASR → 本地检索 / RAG → LLM → TTS** 串成多进程链路。模型之外，重点是控制面与数据面的分离、会话编排和故障边界。

- **留下的工程记录**：可替换后端、协议与部署文档，以及 30 轮全真实链路验证。
- **目前的边界**：麦克风采用固定时长采集，模型推理速度与取消响应仍受后端约束。

[查看源码](https://github.com/Caden-1224/voxorchestra-system) &nbsp; · &nbsp; [板端验证记录](https://github.com/Caden-1224/voxorchestra-system/blob/main/docs/benchmark.md)

### [STM32 Polled Scheduler](https://github.com/Caden-1224/stm32-polled-scheduler)

<sub>📦 <b>可复用模板</b> &nbsp; / &nbsp; C · STM32F407 · HAL · 裸机</sub>

从单片机开发中整理出来的裸机工程模板。用轻量的协作式轮询组织周期任务，按 **Core / Components / APP** 分层，把外设驱动、可复用组件和业务逻辑分开。

- **包含的实践**：DMA、环形缓冲、非阻塞状态机，以及 SimpleFOC 双轴控制等模块。
- **适用的场景**：希望保留裸机可控性，又需要清晰组织多个任务的小型嵌入式项目。

[查看源码与使用说明](https://github.com/Caden-1224/stm32-polled-scheduler)

## 📚 学习 · 把基础连成系统

| 方向 | 想弄明白的问题 |
| --- | --- |
| C++ 与并发 | 资源由谁持有，线程如何协作，取消与退出怎样收尾 |
| Linux 与操作系统 | 进程、I/O、通信和调度如何支撑上层应用 |
| 体系结构与性能 | 数据怎样流过内存与处理器，瓶颈该如何定位 |
| GPU 与系统软件 | 长期探索方向，从上述基础逐步向下深入 |

我习惯先做一个可以运行的小切片，再用测试、日志和文档记录结论。这里既放项目，也留下理解这些问题的过程。

## 🧰 手边的工具

<!-- Theme-aware SVG assets are stored in this repository. -->
<div align="center">

<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-0-night.svg"><img src="./assets/chips/label-0.svg" alt="Languages &amp; Systems" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/c-night.svg"><img src="./assets/chips/c.svg" alt="C" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/cplusplus-night.svg"><img src="./assets/chips/cplusplus.svg" alt="C++" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/python-night.svg"><img src="./assets/chips/python.svg" alt="Python" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/gnubash-night.svg"><img src="./assets/chips/gnubash.svg" alt="Shell" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/linux-night.svg"><img src="./assets/chips/linux.svg" alt="Linux" height="30"></picture>
<br/>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-1-night.svg"><img src="./assets/chips/label-1.svg" alt="Embedded" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/stmicroelectronics-night.svg"><img src="./assets/chips/stmicroelectronics.svg" alt="STM32" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/arm-night.svg"><img src="./assets/chips/arm.svg" alt="ARM" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/rtos-night.svg"><img src="./assets/chips/rtos.svg" alt="RTOS" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/bus-night.svg"><img src="./assets/chips/bus.svg" alt="Serial Bus" height="30"></picture>
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
    <img width="460" src="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/stats.svg" alt="Caden-1224 的公开非 fork 仓库：Star 总数与仓库数" />
  </picture>
</div>

<p align="center"><sub>仅统计本人名下的公开非 fork 仓库；计划每 10 分钟刷新，实际更新时间见卡片。<br><a href="https://github.com/Caden-1224/Caden-1224/actions/workflows/profile-assets.yml">查看同步状态</a></sub></p>

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
