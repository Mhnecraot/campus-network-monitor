#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
报警模块 - 校园网络监控系统
负责发送异常报警（控制台 + 日志 + 模拟邮件）
"""

from datetime import datetime
import time

def send_alert(alert_type: str, message: str, severity: str = "warning"):
    """
    发送报警
    alert_type: 报警类型 (traffic, device, security)
    message: 报警内容
    severity: 严重程度 (info, warning, critical)
    """
    timestamp = datetime.now()
    
    # 不同严重程度使用不同前缀
    prefix = {
        "info": "ℹ️",
        "warning": "⚠️",
        "critical": "🚨"
    }.get(severity, "⚠️")
    
    full_message = f"{prefix} [{timestamp}] {alert_type.upper()} 报警: {message}"
    
    # 1. 控制台输出
    print(full_message)
    
    # 2. 写入日志
    try:
        with open("logs/monitor.log", "a", encoding="utf-8") as f:
            f.write(full_message + "\n")
    except Exception as e:
        print(f"日志写入失败: {e}")
    
    # 3. 模拟邮件/企业微信报警（实际项目中可接入真实接口）
    if severity == "critical":
        print(f"🚨 高级报警！已模拟发送邮件/企业微信通知给管理员")
        # 这里以后可以扩展真实邮件发送功能（smtplib）
    
    return full_message


# 测试函数
if __name__ == "__main__":
    print("=== 报警模块测试 ===")
    send_alert("traffic", "校园主干网络流量异常，超过阈值 85%", "warning")
    send_alert("device", "交换机 SW-03 离线", "critical")
    send_alert("security", "检测到潜在端口扫描行为", "warning")
    print("报警测试完成")
