import requests
import time
from datetime import datetime
from config import *
from alert import send_alert


def write_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def get_auth_token():
    payload = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": ZABBIX_USER,
            "password": ZABBIX_PASS
        },
        "id": 1
    }

    response = requests.post(ZABBIX_URL, json=payload)
    data = response.json()

    return data["result"]


def get_hosts(token):
    payload = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid", "name", "status"]
        },
        "auth": token,
        "id": 2
    }

    response = requests.post(ZABBIX_URL, json=payload)
    return response.json()["result"]


if __name__ == "__main__":
    print(f"[{datetime.now()}] 校园网络监控系统启动")

    token = get_auth_token()

    while True:
        hosts = get_hosts(token)
        current_time = str(datetime.now())

        print(f"\n[{current_time}] 状态检查")

        for host in hosts:
            status = "正常" if host["status"] == "0" else "异常"
            msg = f"{host['name']} -> {status}"

            print(msg)
            write_log(msg)

            if host["status"] != "0":
                send_alert(host["name"])

        time.sleep(CHECK_INTERVAL)
