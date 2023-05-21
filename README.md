# Server-Monitoring-and-Voice-Warning-Script
"Real-Time System Monitoring and Voice Warning Script: Monitor System Metrics, Display Information, and React to Threshold Exceedances"

![Image Description](https://github.com/cy-cus/System-Monitoring-and-Voice-Warning-Script/blob/main/systemmonitor.PNG)

This Python script is designed to provide comprehensive real-time monitoring of your system, displaying important system metrics and generating voice warnings when specific thresholds are exceeded. It is a versatile script that works seamlessly on both Windows and Linux servers, ensuring cross-platform compatibility. By utilizing this script, you can keep a close eye on crucial system parameters, receive immediate alerts when thresholds are surpassed, and take proactive measures to maintain optimal system performance and stability. With its user-friendly interface and adaptable functionality, this script empowers you to effectively monitor your system and respond promptly to any critical events.

## Features
- Monitors CPU usage, memory usage, GPU information, CPU temperature, storage usage, system uptime, and network data transfer.
- Displays system information in a clear and organized manner.
- Generates voice warnings when critical thresholds, such as high CPU or RAM usage, are exceeded.
- Supports both Windows and Linux servers.

## Usage
1. Clone the repository to your local machinem `git clone https://github.com/cy-cus/System-Monitoring-and-Voice-Warning-Script.git`
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the script using Python: `python system_monitor.py`.
4. Enjoy real-time system monitoring and voice warnings.

Please note that this script relies on external libraries such as `pyttsx3`, `GPUtil`, `psutil`, `wmi`, and `termcolor`. Make sure to have these dependencies installed before running the script.

Feel free to customize and enhance the script based on your specific requirements.

Also check the system_monitor_with_email.py through which you can confugure your email to be receiving notifications from the system monitor.



