#!/usr/bin/python3
import os

def run_terminal_command(command):
    try:
        os.system(command)
    except Exception as e:
        print(f"Error executing command: {e}")

def main():
    # Run cowsay with a dinosaur and fortune command
    run_terminal_command("fortune | cowsay -s")

if __name__ == "__main__":
    main()
