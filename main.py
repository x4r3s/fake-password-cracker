import os
import sys
import time
import random
import string


GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def type_text(text, color=GREEN, delay=0.02, newline=True):
    print(color, end="")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if newline:
        print()
    print(RESET, end="")


def glitch_text(text, repeats=3, delay=0.05):
    chars = string.ascii_uppercase + string.digits + "!@#$%^&*"
    for _ in range(repeats):
        fake = "".join(random.choice(chars) if c != " " else " " for c in text)
        print(f"\r{GREEN}{fake}{RESET}", end="", flush=True)
        time.sleep(delay)
    print(f"\r{GREEN}{text}{RESET}")


def spinner(duration=2, text="Decrypting"):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{CYAN}{text} {frames[i % len(frames)]}{RESET}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print("\r" + " " * (len(text) + 5), end="\r")


def progress_bar(current, total, width=30):
    progress = current / total
    filled = int(width * progress)
    bar = "█" * filled + "░" * (width - filled)
    percent = int(progress * 100)
    return f"{YELLOW}[{bar}] {percent:3d}%{RESET}"


def boot_sequence():
    lines = [
        "Booting cyber attack interface...",
        "Loading brute-force engine...",
        "Bypassing firewall...",
        "Establishing secure tunnel...",
        "Injecting payload...",
        "Accessing target node...",
    ]
    for line in lines:
        type_text(f"[+] {line}", GREEN, 0.018)
        time.sleep(0.15)


def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))


def hacker_banner():
    banner = rf"""
{GREEN}{BOLD}
 █████▒▄▄▄       ██ ▄█▀▓█████     ██▓███   ▄▄▄        ██████   ██████ 
▓██   ▒▒████▄     ██▄█▒ ▓█   ▀    ▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ 
▒████ ░▒██  ▀█▄  ▓███▄░ ▒███      ▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   
░▓█▒  ░░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄    ▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
░▒█░    ▓█   ▓██▒▒██▒ █▄░▒████▒   ▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒
 ▒ ░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░   ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
 ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
 ░ ░     ░   ▒   ░ ░░ ░    ░      ░░         ░   ▒   ░  ░  ░  ░  ░  ░  
             ░  ░░  ░      ░  ░                  ░  ░      ░        ░  
{RESET}
{MAGENTA}Fake Password Cracker Simulator{RESET}
{RED}WARNING: Simulation only. No real hacking is performed.{RESET}
"""
    print(banner)


def fake_logs():
    logs = [
        f"Routing traffic through {random_ip()}",
        f"Masking location via node {random_ip()}",
        f"Handshake accepted from {random_ip()}",
        "Hash database mounted",
        "Entropy stabilized",
    ]
    for log in logs:
        print(f"{CYAN}[LOG]{RESET} {log}")
        time.sleep(0.12)


def crack_password(password):
    pool = string.ascii_letters + string.digits + string.punctuation
    cracked = ""

    for i, target_char in enumerate(password, start=1):
        for _ in range(random.randint(8, 30)):
            random_guess = random.choice(pool)
            line = (
                f"\r{GREEN}Cracking:{RESET} "
                f"{BOLD}{cracked}{RED}{random_guess}{RESET}   "
                f"{progress_bar(i - 1, len(password))}"
            )
            print(line, end="", flush=True)
            time.sleep(0.02)

        cracked += target_char
        line = (
            f"\r{GREEN}Cracking:{RESET} "
            f"{BOLD}{cracked}{RESET}   "
            f"{progress_bar(i, len(password))}"
        )
        print(line, end="", flush=True)
        time.sleep(0.18)

    print()
    return cracked


def access_granted():
    for _ in range(2):
        print(f"{GREEN}{BOLD}ACCESS GRANTED{RESET}")
        time.sleep(0.2)
        print("\r" + " " * 30, end="\r", flush=True)
        time.sleep(0.1)
    print(f"{GREEN}{BOLD}ACCESS GRANTED{RESET}")


def main():
    clear()
    hacker_banner()
    time.sleep(0.5)

    type_text("Enter target password:", CYAN, 0.015, newline=False)
    print(" ", end="")
    password = input()

    if not password:
        print(f"{RED}Password cannot be empty.{RESET}")
        sys.exit(1)

    clear()
    hacker_banner()
    boot_sequence()
    fake_logs()
    spinner(1.8, "Synchronizing attack vectors")
    glitch_text("TARGET LOCKED")
    time.sleep(0.4)

    result = crack_password(password)

    print()
    type_text(f"[✓] Password cracked: {result}", GREEN, 0.02)
    time.sleep(0.4)
    access_granted()
    print(f"{MAGENTA}Session complete.{RESET}")


if __name__ == "__main__":
    main()