<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-motion-dark.svg">
  <img src="./assets/banner-motion.svg" alt="Caden · EE → CS · From signals to systems, one layer deeper" width="100%">
</picture>

<p align="right">
  <a href="./README.md">中文</a> &nbsp; / &nbsp; <strong>English</strong>
</p>

<p align="center">
  <strong>Communication Engineering student · Embedded · Linux · Edge AI</strong><br>
  From capturing a signal to making a task run reliably.
</p>

## 👋 Hi, I'm Caden

I'm a Communication Engineering student finding my way into computer systems. I started with microcontrollers and peripherals, then moved into multiprocess applications and edge inference on Linux. My curiosity has grown from getting a feature to work to understanding the scheduling, communication, and resource management underneath it.

I like following a problem one layer deeper. Where is the data waiting? Why does an old result arrive after cancellation? What happens to the rest of the system when a process exits? Embedded work made me attentive to timing, memory, and hardware constraints; now I want to understand the software side just as well.

🎯 **My main line right now is computer systems.** EE gave me an intuition for signals, timing, and hardware constraints; CS is where I want to put that back into the system view. I'm building up the foundations and testing what I learn through projects; longer term I'd like to work on GPUs and systems software.

## 🛠️ Projects · From boards to systems

These projects trace my path from peripherals and task scheduling to interprocess communication and task runtimes.

### [NexWeave](https://github.com/Caden-1224/nexweave)

<sub>🚧 <b>In development</b> &nbsp; / &nbsp; C++17 · Linux · ZeroMQ · CMake / CTest</sub>

A task framework for Linux edge devices. It brings session lifecycles, streaming data, cancellation, and backend integration under explicit execution contracts so models and devices can work together.

- **What I'm working through:** bounded buffering, cross-process cancellation, stale-result isolation, and cleanup when a task ends.
- **Current scope:** a Linux multiprocess pipeline validated with deterministic fake backends. Real models, audio devices, and RK3576 integration are not complete yet.

[Source](https://github.com/Caden-1224/nexweave) &nbsp; · &nbsp; [Status and roadmap](https://github.com/Caden-1224/nexweave#status)

### [VoxOrchestra](https://github.com/Caden-1224/voxorchestra-system)

<sub>✅ <b>Validated on hardware</b> &nbsp; / &nbsp; C++17 · TCP / ZeroMQ · RK3576 · Offline inference</sub>

An offline voice system validated on the RK3576-based Taishan Pi 3M, connecting **ASR → local retrieval / RAG → LLM → TTS** across multiple processes. Beyond the models, the work focuses on separate control and data planes, session orchestration, and failure boundaries.

- **What the repository records:** replaceable backends, protocol and deployment documentation, and 30 runs through the real hardware pipeline.
- **Current limits:** microphone capture uses a fixed duration; inference speed and cancellation responsiveness remain constrained by the backends.

[Source](https://github.com/Caden-1224/voxorchestra-system) &nbsp; · &nbsp; [Hardware validation](https://github.com/Caden-1224/voxorchestra-system/blob/main/docs/benchmark.md)

### [STM32 Polled Scheduler](https://github.com/Caden-1224/stm32-polled-scheduler)

<sub>📦 <b>Reusable template</b> &nbsp; / &nbsp; C · STM32F407 · HAL · Bare metal</sub>

A bare-metal template shaped by my microcontroller projects. Lightweight cooperative polling organizes periodic tasks, while **Core / Components / APP** layers separate peripheral drivers, reusable components, and application logic.

- **Practices included:** DMA, ring buffers, nonblocking state machines, and modules such as dual-axis SimpleFOC control.
- **Where it fits:** small embedded projects that need clear task organization and direct control of the hardware.

[Source and usage guide](https://github.com/Caden-1224/stm32-polled-scheduler)

## 📚 Learning · Connecting the foundations

| Area | Questions I want to understand |
| --- | --- |
| C++ and concurrency | Who owns a resource, how threads cooperate, and how cancellation and shutdown finish |
| Linux and operating systems | How processes, I/O, communication, and scheduling support applications |
| Architecture and performance | How data moves through memory and processors, and how to locate bottlenecks |
| GPUs and systems software | A longer-term direction to explore as those foundations grow |

I tend to start with a small runnable slice, then use tests, logs, and documentation to record what I learn. These repositories hold both the projects and the process of understanding them.

## 🧰 Tools I work with

<!-- Theme-aware SVG assets are stored in this repository. -->
<div align="center">

<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-0-en-night.svg"><img src="./assets/chips/label-0-en.svg" alt="Languages &amp; Systems" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/c-night.svg"><img src="./assets/chips/c.svg" alt="C" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/cplusplus-night.svg"><img src="./assets/chips/cplusplus.svg" alt="C++" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/python-night.svg"><img src="./assets/chips/python.svg" alt="Python" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/gnubash-night.svg"><img src="./assets/chips/gnubash.svg" alt="Shell" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/linux-night.svg"><img src="./assets/chips/linux.svg" alt="Linux" height="30"></picture>
<br/>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-1-en-night.svg"><img src="./assets/chips/label-1-en.svg" alt="Embedded" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/stmicroelectronics-night.svg"><img src="./assets/chips/stmicroelectronics.svg" alt="STM32" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/arm-night.svg"><img src="./assets/chips/arm.svg" alt="ARM" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/rtos-night.svg"><img src="./assets/chips/rtos.svg" alt="RTOS" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/bus-night.svg"><img src="./assets/chips/bus.svg" alt="Serial Bus" height="30"></picture>
<br/>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-2-en-night.svg"><img src="./assets/chips/label-2-en.svg" alt="Build &amp; Runtime" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/cmake-night.svg"><img src="./assets/chips/cmake.svg" alt="CMake" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/zeromq-night.svg"><img src="./assets/chips/zeromq.svg" alt="ZeroMQ" height="30"></picture>
<br/>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-3-en-night.svg"><img src="./assets/chips/label-3-en.svg" alt="Engineering &amp; Collaboration" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/git-night.svg"><img src="./assets/chips/git.svg" alt="Git" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/docker-night.svg"><img src="./assets/chips/docker.svg" alt="Docker" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/githubactions-night.svg"><img src="./assets/chips/githubactions.svg" alt="GitHub Actions" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/claude-night.svg"><img src="./assets/chips/claude.svg" alt="Claude Code" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/modelcontextprotocol-night.svg"><img src="./assets/chips/modelcontextprotocol.svg" alt="MCP" height="30"></picture>

<br/>
<sub>Also exploring: </sub> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/opencv-night.svg"><img src="./assets/chips/opencv.svg" alt="OpenCV" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/ros-night.svg"><img src="./assets/chips/ros.svg" alt="ROS 2" height="30"></picture>

</div>

<br/>

<!-- ============ Sky ============ -->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/sky-night.svg" />
    <img src="./assets/sky.svg" width="100%" alt="" />
  </picture>
</div>

## 📊 On the record

<!-- Public owned, non-fork repositories; refreshed by profile-assets.yml. -->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/stats-dark.svg" />
    <img width="460" src="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/stats.svg" alt="Caden-1224's public non-fork repositories: total stars and repository count" />
  </picture>
</div>

<p align="center"><sub>Owned, public, non-fork repositories only. Scheduled every 10 minutes; the card shows its actual update time.<br><a href="https://github.com/Caden-1224/Caden-1224/actions/workflows/profile-assets.yml">View sync status</a></sub></p>

<!-- Contribution animation is published independently from the stats card. -->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/github-contribution-grid-snake-dark.svg" />
    <img width="100%" alt="Animated GitHub contribution calendar for the past year" src="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/github-contribution-grid-snake.svg" />
  </picture>
</div>

---

💬 If you're also learning about systems, tinkering with embedded hardware, or making your own move from EE to CS, feel free to say hi.

[Email](mailto:seekercaden@outlook.com) &nbsp; · &nbsp; [GitHub](https://github.com/Caden-1224)
