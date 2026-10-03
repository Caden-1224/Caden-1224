<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-motion-dark.svg">
  <img src="./assets/banner-motion.svg" alt="Caden · EE → CS · From signals to systems, one layer deeper" width="100%">
</picture>

<p align="right">
  <a href="./README.md">中文</a> &nbsp; / &nbsp; <strong>English</strong>
</p>

<p align="center">
  <img src="./assets/avatar.png" width="120" alt="Caden"><br><br>
  <strong>Communication Engineering student · Embedded · Linux · Edge AI</strong><br>
  From EE to CS: starting with low-level hardware, moving up into computer systems
</p>

## 👋 Hi, I'm Caden

I'm a Communication Engineering student finding my way into computer systems. I started with microcontrollers and peripherals, then moved into multiprocess applications and edge inference on Linux. My curiosity has grown from getting a feature to work to understanding the scheduling, communication, and resource management underneath it.

I like following a problem one layer deeper. Where is the data waiting? Why does an old result arrive after cancellation? What happens to the rest of the system when a process exits? Embedded work made me attentive to timing, memory, and hardware constraints; now I want to understand the software side just as well.

🎯 **My main line right now is computer systems.** EE gave me an intuition for signals, timing, and hardware constraints; CS is where I want to put that back into the system view. I'm building up the foundations and testing what I learn through projects; longer term I'd like to work on GPUs and systems software.

## 🛠️ Projects · From boards to systems

These projects trace my path from peripherals and task scheduling to interprocess communication and task runtimes.

### [SlotNexus](https://github.com/Caden-1224/SlotNexus)

<sub>✅ <b>0.2.0 · Validated on hardware</b> &nbsp; / &nbsp; C++17 · Linux · epoll / Reactor · ZeroMQ · CMake</sub>

On-device multiprocess inference middleware for Linux edge devices. A general-purpose Core (communication, task routing, Node runtime) carries the first voice application module, which runs a fully offline **ASR → RAG → LLM → TTS** chain on the board.

- Core depends on neither voice types nor vendor SDKs and builds, tests and installs on its own (`find_package(slotnexus-core)`); nodes share one `setup / inference / cancel / taskinfo / exit` contract, task state bounds concurrent inference per task, and the Session filters stale events with a generation counter.
- On the board the chain runs as six processes: Gateway, Manager, Session, ASR, LLM, TTS. Stage timing showed the TTS consumer chain starting too late; starting the generate → synthesise → output pipeline earlier, together with amortised O(1) resampling buffers and a continuous decoder slice, brought the p50 WAV completion time over 30 persistent-input rounds down from 6.1 / 22.9 s to 4.0 / 18.4 s for L1 / L3, and L3 TTS RTF from 0.507 to 0.272 (test conditions and attribution are in the repository).

[Source and design](https://github.com/Caden-1224/SlotNexus)

### [CIMC Industrial Embedded 2026](https://github.com/Caden-1224/CIMC-Industrial-Embedded-2026)

<sub>🏆 <b>National Preliminary Round, First Prize</b> &nbsp; / &nbsp; C · GD32F470 · Keil MDK · RS485 · BootLoader / OTA</sub>

An acquisition terminal for the factory floor: wide-range power, three sampling channels, RS485 command handling, parameter persistence across power loss, and remote firmware updates. Two separate projects (App and BootLoader) replace an RTOS with cooperative time-sliced polling; OTA closes the loop from staging through CRC32 to install, backup, rollback, and the vector-table jump.

- **About 15,200 lines of C written by me**; the protocol is ASCII-Hex frames with CRC16-Modbus, and 29 commands cover system management, the data plane, parameters, alerts, and upgrades.
- The EDA project plus schematic and PCB renders for **three self-designed boards** (18–36 V supply, PT100 sampling, precision-resistor simulator) are open-sourced with the firmware.
- Stopped at the preliminary first prize: the trip to the Beijing finals had to be paid upfront, and I let it go. [The README says so](https://github.com/Caden-1224/CIMC-Industrial-Embedded-2026#stopping-at-the-preliminaries).

[Source and documentation](https://github.com/Caden-1224/CIMC-Industrial-Embedded-2026)

### [STM32 Polled Scheduler](https://github.com/Caden-1224/stm32-polled-scheduler)

<sub>📦 <b>Reusable template</b> &nbsp; / &nbsp; C · STM32F407 · HAL · Bare metal</sub>

A bare-metal template shaped by my microcontroller projects. Lightweight cooperative polling organizes periodic tasks, while **Core / Components / APP** layers separate peripheral drivers, reusable components, and application logic.

- **Practices included:** DMA, ring buffers, nonblocking state machines, and modules such as dual-axis SimpleFOC control.
- **Where it fits:** small embedded projects that need clear task organization and direct control of the hardware.

[Source and usage guide](https://github.com/Caden-1224/stm32-polled-scheduler)

### [NexWeave](https://github.com/Caden-1224/nexweave)

<sub>🚧 <b>In development</b> &nbsp; / &nbsp; C++17 · Linux · ZeroMQ · CMake / CTest</sub>

A task framework for Linux edge devices. It brings session lifecycles, streaming data, cancellation, and backend integration under explicit execution contracts so models and devices can work together.

- **What I'm working through:** bounded buffering, cross-process cancellation, stale-result isolation, and cleanup when a task ends.
- **Current progress:** validated the Linux multiprocess pipeline and implemented real ASR / LLM / TTS and ALSA adapters, plus a full-duplex audio frontend. VAD and complete hardware voice interaction remain to be integrated.

[Source](https://github.com/Caden-1224/nexweave) &nbsp; · &nbsp; [Status and roadmap](https://github.com/Caden-1224/nexweave#status)

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
