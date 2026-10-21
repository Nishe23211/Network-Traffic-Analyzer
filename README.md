# 🛡️ Network Traffic Analyzer

## Description

Network Traffic Analyzer is a beginner-friendly cybersecurity project developed using Python, Scapy, Pandas, and Streamlit.

The project captures network packets, analyzes source and destination IP addresses, identifies communication protocols, and visualizes network traffic through an interactive dashboard.

The main objective is to understand network communication, packet analysis, and basic network monitoring concepts.

## Features

- **Packet Capture:** Captures network packets using Scapy.
- **IP Address Analysis:** Identifies source and destination IP addresses.
- **Protocol Identification:** Categorizes captured IP packets into TCP, UDP, and OTHER.
- **Packet Size Monitoring:** Records and analyzes packet sizes.
- **Timestamp Recording:** Records the capture time of packets.
- **CSV Export:** Saves captured network traffic into a CSV file.
- **Interactive Dashboard:** Visualizes network traffic using Streamlit.
- **Protocol Distribution:** Displays network protocol statistics.
- **IP Statistics:** Shows frequently occurring source IP addresses.

## Technologies Used

- **Programming Language:** Python
- **Packet Analysis:** Scapy
- **Data Processing:** Pandas
- **Dashboard:** Streamlit
- **Packet Capture Driver:** Npcap (Windows)
- **Development Environment:** Visual Studio Code

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Nishe23211/Network-Traffic-Analyzer.git
```

### 2. Open the Project Directory

```bash
cd Network-Traffic-Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Required Libraries

```bash
python -m pip install -r requirements.txt
```

### 6. Install Npcap

For Windows packet capture, install Npcap from:

https://npcap.com/#download

## Usage Instructions

### Step 1: Start Network Packet Capture

Run:

```bash
python main.py
```

The program captures network packets and records:

- Source IP address
- Destination IP address
- Network protocol
- Packet size
- Capture timestamp

After capturing 100 packets, the program generates `traffic.csv`.

### Step 2: Launch the Dashboard

Run:

```bash
python -m streamlit run dashboard.py
```

### Step 3: Open the Dashboard

Open the local URL displayed in your terminal, typically:

http://localhost:8501

### Step 4: Explore Network Statistics

The dashboard displays:

- Total captured IP packets
- Unique source and destination IPs
- TCP/UDP protocol distribution
- Top source IP addresses
- Packet size statistics
- Captured traffic records

**Note:** The dashboard analyzes previously saved CSV data and does not yet provide real-time threat detection.

## Security and Privacy

This project is intended for educational purposes and authorized network monitoring only.

- Capture traffic only on devices or networks you own or have permission to monitor.
- Do not publish captured network traffic containing private information.
- The `traffic.csv` file is excluded from the public GitHub repository.

## Future Improvements

- Suspicious traffic detection
- Automated security alerts
- Real-time traffic visualization
- Advanced packet filtering
- Historical network traffic analysis

## Project Information

**Project:** Network Traffic Analyzer

**Category:** Cybersecurity / Network Security

**Language:** Python

**GitHub:** https://github.com/Nishe23211/Network-Traffic-Analyzer
