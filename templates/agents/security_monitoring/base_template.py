#!/usr/bin/env python3
"""
Security Monitoring Agent Template
Real-time threat detection and analysis
"""

import re
import json
from typing import List, Dict
from datetime import datetime
import time

class MonitoringAgent:
    def __init__(self, config: Dict):
        self.config = config
        self.alerts = []
        self.patterns = self._load_patterns()
    
    def _load_patterns(self) -> List[Dict]:
        """Load threat detection patterns"""
        return [
            {
                "name": "SQL Injection",
                "pattern": r"(union.*select|select.*from|insert.*into)",
                "severity": "high"
            },
            {
                "name": "XSS Attempt",
                "pattern": r"(<script|javascript:|onerror=)",
                "severity": "high"
            },
            {
                "name": "Path Traversal",
                "pattern": r"(\.\./|\.\.\\\\/)",
                "severity": "medium"
            }
        ]
    
    def analyze_log(self, log_entry: str) -> List[Dict]:
        """Analyze a single log entry"""
        alerts = []
        
        for pattern in self.patterns:
            if re.search(pattern['pattern'], log_entry, re.IGNORECASE):
                alerts.append({
                    "timestamp": datetime.now().isoformat(),
                    "alert_type": pattern['name'],
                    "severity": pattern['severity'],
                    "log_entry": log_entry,
                    "matched_pattern": pattern['pattern']
                })
        
        return alerts
    
    def monitor_logs(self, log_file: str):
        """Continuous log monitoring"""
        print(f"[*] Monitoring {log_file}...")
        
        with open(log_file, 'r') as f:
            # Move to end of file
            f.seek(0, 2)
            
            while True:
                line = f.readline()
                if line:
                    alerts = self.analyze_log(line)
                    if alerts:
                        self.handle_alerts(alerts)
                else:
                    time.sleep(1)
    
    def handle_alerts(self, alerts: List[Dict]):
        """Handle detected threats"""
        for alert in alerts:
            print(f"[!] ALERT: {alert['alert_type']} - {alert['severity']}")
            self.alerts.append(alert)
            # Send notifications, trigger responses, etc.
