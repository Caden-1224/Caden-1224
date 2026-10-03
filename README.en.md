<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-motion-dark.svg">
  <img src="./assets/banner-motion.svg" alt="Caden · EE → CS · From signals to systems, one layer deeper" width="100%">
</picture>

<p align="right">
  <a href="./README.md">中文</a> &nbsp; / &nbsp; <strong>English</strong>
</p>

<p align="center">
  <strong>Communication Engineering student · Embedded · Linux · Edge AI</strong><br>
  From embedded systems to computer systems
</p>

## 👋 Hi, I'm Caden

I study Communication Engineering. I started with microcontrollers and peripherals, and these days I work mostly on multiprocess applications and edge inference on Linux. Put the projects side by side and they trace one line: first make a feature run on the board, then work out how the scheduling, communication and resources behind it are arranged.

I like following a problem one layer deeper. Where is the data waiting? Why does an old result arrive after cancellation? What happens to the rest of the system when a process exits? Embedded work made me attentive to timing, memory and hardware constraints; now I want to understand the software side just as well — how the budget is computed, where the boundary is drawn, and who catches the failure.

🎯 **My main line right now is computer systems.** EE gave me an intuition for signals, timing and hardware constraints; CS is where I want to put that back into the system view. I am building up the foundations and testing what I learn through projects; longer term I would like to work on GPUs and systems software.

My habit is to start with a small runnable slice, then pin the conclusions down with tests, logs and documentation — including the parts that did not work. What I have written lives in the repositories on this account.

## 🧰 Tech stack

**Languages and systems**

- **C / C++17**: bare-metal and driver-level C (about 15,200 lines written by me in the most recent industrial terminal), module boundaries and interface design in C++17
- **Linux systems and network programming**: multiprocess design, epoll / Reactor event loops, TCP / NDJSON, ZeroMQ messaging, cross-process cancellation and resource cleanup
- **Python / Shell**: scripting, build and verification tooling

**Embedded**

- **Platforms**: GD32F4xx (GD32F470VE), STM32F4; Keil MDK, standard peripheral library and HAL
- **Peripherals and mechanisms**: UART / RS485 / SPI / I²C, DMA with ring buffers, interrupts and nonblocking state machines, Timer / RTC, internal and SPI flash
- **System-level work**: BootLoader and OTA (partitions, CRC32, backup and rollback, vector-table jump), parameters that survive power loss, cooperative time-sliced scheduling
- **Bring-up and deployment**: register-level drivers, hardware/software bring-up, Linux aarch64 board deployment (RK3576)

**Engineering and tooling**

- CMake / CTest, Git, Docker, GitHub Actions
- MATLAB, OpenCV geometric vision, ROS 2; fundamentals of deep learning and PyTorch (basic)

**How I work**

- Specification-driven plus test-driven: requirements first become specs, interface contracts and acceptance criteria, then implementation and regression
- AI coding tools (Claude Code, MCP) for project-level context, code reading, plan breakdown and patch verification, leaving traceable specs and change records

<!-- Theme-aware SVG assets are stored in this repository. -->
<div align="center">

<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-0-en-night.svg"><img src="./assets/chips/label-0-en.svg" alt="Languages &amp; Systems" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/c-night.svg"><img src="./assets/chips/c.svg" alt="C" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/cplusplus-night.svg"><img src="./assets/chips/cplusplus.svg" alt="C++" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/python-night.svg"><img src="./assets/chips/python.svg" alt="Python" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/gnubash-night.svg"><img src="./assets/chips/gnubash.svg" alt="Shell" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/linux-night.svg"><img src="./assets/chips/linux.svg" alt="Linux" height="30"></picture>
<br/>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/label-1-en-night.svg"><img src="./assets/chips/label-1-en.svg" alt="Embedded" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/gd32-night.svg"><img src="./assets/chips/gd32.svg" alt="GD32" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/stmicroelectronics-night.svg"><img src="./assets/chips/stmicroelectronics.svg" alt="STM32" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/arm-night.svg"><img src="./assets/chips/arm.svg" alt="ARM" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/rtos-night.svg"><img src="./assets/chips/rtos.svg" alt="RTOS" height="30"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/chips/bus-night.svg"><img src="./assets/chips/bus.svg" alt="Serial Bus" height="30"></picture>
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
    <img width="640" src="https://raw.githubusercontent.com/Caden-1224/Caden-1224/output/stats.svg" alt="Caden-1224's public non-fork repositories: total stars, authored commits and repository count" />
  </picture>
</div>

<p align="center"><sub>Owned, public, non-fork repositories only. Commits sum my authored commits in each current default-branch history, across all time.<br>Scheduled every 10 minutes; the card shows its actual update time.<br><a href="https://github.com/Caden-1224/Caden-1224/actions/workflows/profile-assets.yml">View sync status</a></sub></p>

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
