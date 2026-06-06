# port-scanner
Fast concurrent port scanner like Nmap

# Async Port Scanner

A fast concurrent port scanner built with Python's asyncio. Scans all 1024 ports simultaneously using async I/O — far faster than traditional threaded scanners.

## How to run
python3 scanner.py                   # scans localhost
python3 scanner.py scanme.nmap.org   # scans a remote host

## Demo
Open ports on scanme.nmap.org:
22/tcp  open
80/tcp  open

## Concepts demonstrated

- Async I/O with asyncio
- Concurrent TCP connection attempts
- Why async is faster than threading for I/O-bound tasks
- Command line arguments with sys.argv

## Ethical use

Only scan hosts you own or have explicit permission to scan.

