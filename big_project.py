import requests
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"___ [LOG] Initialising execution of: {func.__name__}---")
        return func(*args, **kwargs)
    return wrapper

from uptime_kuma_api import UptimeKumaApi

# Decorator for clean logging
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"--- [LOG] Initialising execution of: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class APIClient:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.api = UptimeKumaApi(self.url)

    def connect(self):
        self.api.login(self.username, self.password)

    def get_monitor_status(self):
        return self.api.get_monitors()

    def disconnect(self):
        self.api.disconnect()

class Device:
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address
        self.status = "Unknown"

    @log_execution
    def get_info(self):
        return f"{self.name} ({self.ip_address}) - Status: {self.status}"

# Configuration
# Use the base URL, NOT the dashboard/3 path
kuma_url = "BASE URL"
client = APIClient(kuma_url, "USERNAME", "PASSWORD")

# Execution
try:
    client.connect()
    monitors = client.get_monitor_status()

    # Example: Print the status of the first monitor found
    if monitors:
        print(f"Successfully connected! Found {len(monitors)} monitors.")

    for monitor in monitors:

        m_name = monitor.get('name', '').strip()
        m_status = monitor.get('status', 'Unknown')
        print(f"DEBUG: {monitor.get('name')} data: {monitor}")
    # This loop now maps the API data to your terminal output
        print(f"Monitor: {m_name} | Status: {m_status}")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.disconnect()

