import os
import platform
import time
import pyttsx3
import GPUtil
import psutil
from termcolor import colored

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def unit(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def clr(text, color):
    return colored(text, color)

def get_cpu_temperature():
    if platform.system() == "Linux":
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temp = int(file.read()) / 1000  # Temperature in degrees Celsius
            return temp
    elif platform.system() == "Windows":
        import wmi
        c = wmi.WMI()
        temperature = c.Win32_PerfFormattedData_Counters_ThermalZoneInformation()[0].Temperature
        return temperature
    else:
        return "N/A"

def speak_warning(message):
    engine.say(message)
    engine.runAndWait()

def monitor():
    time.sleep(1.5)
    gpus = GPUtil.getGPUs()
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    mem = psutil.virtual_memory()
    gpus = GPUtil.getGPUs()
    internet = psutil.net_io_counters()
    sys = uname.system
    core = psutil.cpu_count(logical=True)
    cpu_freq_mx = cpufreq.max
    mem_total = (int(mem.total)) / (1024 * 1024 * 1024)

    gpu_list = []
    if gpus:
        for gpu in gpus:
            gpu_name = gpu.name
            gpu_total_memory = f"{gpu.memoryTotal}MB"
            gpu_temperature = f"{gpu.temperature} °C"
            gpu_list.append((gpu_name, gpu_total_memory))

    g_pu = (gpu_list[0])[0] if gpu_list else "N/A"
    g_pu_mem = (gpu_list[0])[1] if gpu_list else "N/A"
    os.system("clear" if platform.system() != "Windows" else "cls")
    cpu_temperature = get_cpu_temperature()

    cpu_percent = psutil.cpu_percent()
    cpu_color = None

    if cpu_percent >= 80:
        cpu_color = "red"
        speak_warning("High CPU usage!")
    elif cpu_percent >= 50:
        cpu_color = "yellow"
    else:
        cpu_color = "green"

    ram_percent = mem.percent
    ram_color = None

    if ram_percent >= 80:
        ram_color = "red"
        speak_warning("High RAM usage!")
    elif ram_percent >= 50:
        ram_color = "yellow"
    else:
        ram_color = "green"

    storage = psutil.disk_usage("/")
    storage_percent = storage.percent
    storage_color = None

    if storage_percent >= 80:
        storage_color = "red"
        speak_warning("High storage usage!")
    elif storage_percent >= 50:
        storage_color = "yellow"
    else:
        storage_color = "green"

    uptime = time.time() - psutil.boot_time()
    uptime_formatted = time.strftime("%H:%M:%S", time.gmtime(uptime))

    disk_io = psutil.disk_io_counters()
    read_speed = unit(disk_io.read_bytes)
    write_speed = unit(disk_io.write_bytes)

    print(
        f"""
    {"%"*10}{"="*10} SYSTEM INFORMATION {"="*10}{"%"*10}
            System          - {clr(sys, "cyan")}
            Total Cores     - {clr(f"{core} Cores", "cyan")} 
            Cpu Usage       - {clr(f"{cpu_percent}%", cpu_color)}
            Max Cpu Freq    - {clr(f"{cpu_freq_mx}MHz", "cyan")}
            Total Ram       - {clr(f"{round(mem_total)}GB", ram_color)}
            Ram in Use      - {clr(f"{unit(mem.used)}", ram_color)} | {clr(f"{ram_percent}%", ram_color)}
            Gpu             - {clr(g_pu, "cyan")}
            Gpu Memory      - {clr(g_pu_mem, "cyan")}
            CPU Temperature - {clr(f"{cpu_temperature}°C", "cyan")}
            Storage         - {clr(f"{unit(storage.used)}", storage_color)} | {clr(f"{storage_percent}%", storage_color)}
            System Uptime   - {clr(uptime_formatted, "cyan")}
            Read Speed      - {clr(read_speed, "cyan")}/s
            Write Speed     - {clr(write_speed, "cyan")}/s
    {"-"*100}
      {"%"*10}{"="*10} INTERNET {"="*10}{"%"*10}        
            Data Sent       - {clr(unit(internet.bytes_sent), "cyan")}
            Data Receive    - {clr(unit(internet.bytes_recv), "cyan")}
                                    
    """
    )

while True:
    monitor()
