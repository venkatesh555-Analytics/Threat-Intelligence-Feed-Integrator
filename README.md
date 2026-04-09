# Threat-Intelligence-Feed-Integrator

## Project Overview
This project demonstrates automated threat intelligence enrichment of IP indicators using VirusTotal and AbuseIPDB APIs. It identifies malicious, suspicious, and benign IPs based on reputation scores.

## Features
- Automated IOC enrichment
- Integration with VirusTotal API
- Integration with AbuseIPDB API
- Classification of IPs (Malicious / Suspicious / Safe)
- Real-world SOC use case

## Tools & Technologies
- Python
- VirusTotal API
- AbuseIPDB API
- Requests Library

## Dataset
A mixed dataset of IP addresses including:
- Malicious IP ranges
- Public IPs (Google, Cloudflare)
- Internal IPs
- Random internet IPs

##  How It Works
1. Reads IP addresses from `ioc_list.txt`
2. Queries VirusTotal for malicious detections
3. Queries AbuseIPDB for abuse score
4. Outputs enriched threat intelligence data

## Sample Output
IP                VT    Abuse 185.220.101.1     14    100 8.8.8.8           0     0

##  Screenshots
- Terminal output
- VirusTotal result (malicious IP)
- AbuseIPDB result

## Note
Due to API rate limits, only a subset of IPs is processed during execution.

## Security Note
API keys are removed from the code for security purposes.

## Key Learnings
- Threat intelligence enrichment
- API integration
- SOC investigation workflow
- Automation using Python

## Use Case
This project simulates a SOC analyst workflow for validating indicators of compromise (IOCs).
