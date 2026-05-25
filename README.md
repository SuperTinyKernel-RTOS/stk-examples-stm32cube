# SuperTinyKernel™ RTOS examples for STMicroelectronics STM32CubeIDE

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Arm Cortex-M](https://img.shields.io/badge/Platform-Arm%20Cortex--M-blue.svg)](https://developer.arm.com/ip-products/processors/cortex-m)

**SuperTinyKernel™ RTOS** (STK) is a high-performance, deterministic, bare-metal C++ real-time operating system designed for resource-constrained embedded systems.

> **Note:** This repository is related to examples configured exclusively for STM32CubeIDE. For details about SuperTinyKernel RTOS, visit its [project on GitHub](https://github.com/SuperTinyKernel-RTOS).

---

## 🛠 Getting Started with [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html)

STK provides ready-to-use examples for popular development boards. Follow these steps to get up and running:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/SuperTinyKernel-RTOS/stk-examples-stm32cube.git
    cd stk-examples-stm32cube
    ```

2.  **Initialize Dependencies:**
    Navigate to your chosen example folder and run the configuration script. This will automatically fetch the STK kernel and necessary HAL drivers.
    ```bash
    cd stm/blinky-stm32f407g-disc1
    python configure.py
    ```

3. **Configure MCU:**
   Use [**STM32CubeMX**](https://www.st.com/content/st_com/en/stm32cubemx.html) to reconfigure the project.

   > **Note**: When project is regenerated make sure to uncomment `SVC_Handler`, `PendSV_Handler` and `SysTick_Handler` functions (or prefix function name with _) in `stm32f4xx_it.c` file. These ISR handlers are used by STK.

4**Build & Flash:**
    Open the generated project in **STM32CubeIDE**, compile, and flash your board. To reconfigure project use [**STM32CubeMX**](https://www.st.com/content/st_com/en/stm32cubemx.html).

---

## 📂 Supported Examples

| Board                | Path                          | Description                               |
|:---------------------|:------------------------------|:------------------------------------------|
| **STM32F407G-DISC1** | `stm\blinky-stm32f407g-disc1` | Basic LED toggle using STK tasks/threads. |

> **Note:** Using GCC/Eclipse? Examples for these environments are located in [STK Main Repo - Examples](https://github.com/SuperTinyKernel-RTOS/stk/tree/main/build/example/project).

> **Note:** Using MCUXpresso, or Arm Keil MDK/µVision, IAR EWARM? Examples for these environments are located in their [respective repositories](https://github.com/SuperTinyKernel-RTOS/).

---

## 🔗 Resources

* **Core:** [Repository](https://github.com/SuperTinyKernel-RTOS/stk)
* **Documentation:** [STK API](https://supertinykernel.org)
* **Issue Tracker:** [Report a bug](https://github.com/SuperTinyKernel-RTOS/stk-examples-stm32cube/issues)