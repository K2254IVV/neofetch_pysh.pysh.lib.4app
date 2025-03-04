import platform
import os
import psutil  # Для получения информации о памяти в Windows

def neofetch():
    system = platform.system()
    if system == "Linux":
        icon = "🐧"
        os_info = os.popen('cat /etc/os-release | grep PRETTY_NAME').read().strip().split('=')[1].strip('"')
        memory = os.popen('free -m').read().splitlines()[1].split()[1] + " MB"
    elif system == "Windows":
        icon = "🪟"
        os_info = platform.version()
        memory = f"{psutil.virtual_memory().total // (1024 ** 2)} MB"  # Общая память в MB
    elif system == "Darwin":
        icon = "🍎"
        os_info = platform.mac_ver()[0]
        memory = os.popen('vm_stat | grep "Pages free"').read().strip().split()[-1] + " MB"
    else:
        icon = "💻"
        os_info = "Unknown OS"
        memory = "Unknown"

    print(f"""
{icon} OS: {system} {os_info}
{icon} Host: {platform.node()}
{icon} Kernel: {platform.version()}
{icon} Shell: pysh
{icon} CPU: {platform.processor()}
{icon} Memory: {memory}
""")
