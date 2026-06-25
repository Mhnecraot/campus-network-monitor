#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置文件 - 校园网络监控系统
集中管理所有配置参数，方便后期修改
"""

from datetime import datetime

# ==================== Zabbix 配置 ====================
ZABBIX_URL = "http://your-zabbix-server/api_jsonrpc.php"  # 本地测试时可留空
ZABBIX_USER = "Admin"
ZABBIX_PASS = "zabbix"

# ==================== 监控配置 ====================
CHECK_INTERVAL = 10          # 监控间隔（秒）
TRAFFIC_THRESHOLD = 85       # 流量阈值（百分比）
LOG_FILE = "logs/monitor.log"

# ==================== 设备列表（模拟） ====================
MONITORED_DEVICES = [
    {"name": "核心路由器", "ip": "192.168.1.1"},
    {"name": "核心交换机", "ip": "192.168.1.2"},
    {"name": "无线AP", "ip": "192.168.1.10"},
    {"name": "服务器", "ip": "192.168.1.100"},
]

# ==================== 报警配置 ====================
ALERT_SETTINGS = {
    "email": "your-email@example.com",           # 模拟接收邮箱
    "wecom": True,                               # 是否启用企业微信报警
    "critical_threshold": 90                     # 严重报警阈值
}

# ==================== 日志配置 ====================
LOG_LEVEL = "INFO"
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"

def print_config():
    """打印当前配置（调试用）"""
    print("=" * 50)
    print(f"校园网络监控系统配置 - {datetime.now()}")
    print("=" * 50)
    print(f"Zabbix 服务器: {ZABBIX_URL}")
    print(f"监控间隔: {CHECK_INTERVAL} 秒")
    print(f"流量报警阈值: {TRAFFIC_THRESHOLD}%")
    print(f"监控设备数量: {len(MONITORED_DEVICES)} 个")
    print(f"日志文件: {LOG_FILE}")
    print("=" * 50)


# 测试
if __name__ == "__main__":
    print_config()
