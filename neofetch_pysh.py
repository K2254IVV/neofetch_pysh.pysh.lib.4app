import platform
import os

def neofetch():
    system = platform.system()
    if system == "Linux":
        icon = "🐧"
        os_info = os.popen('cat /etc/os-release | grep PRETTY_NAME').read().strip().split('=')[1].strip('"')
    elif system == "Windows":
        icon = "🪟"
        os_info = platform.version()
    elif system == "Darwin":
        icon = "🍎"
        os_info = platform.mac_ver()[0]
    else:
        icon = "💻"
        os_info = "Unknown OS"

    print(f"""
{icon} OS: {system} {os_info}
{icon} Host: {platform.node()}
{icon} Kernel: {platform.version()}
{icon} Shell: pysh
{icon} CPU: {platform.processor()}
{icon} Memory: {os.popen('free -m').read().splitlines()[1].split()[1]} MB
""")
