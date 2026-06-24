import requests
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"___ [LOG] Initialising execution of: {func.__name__}---")
        return func(*args, **kwargs)
    return wrapper

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
    def fetch_data(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return None
client=APIClient( "https://jsonplaceholder.typicode.com")
users = client.fetch_data("/users")




class Device:
    def __init__(self, name, ip_address, ):
        self.name =  name
        self.ip_address = ip_address
        self.status= "Unknown"
    @log_execution
    def get_info(self):
        return f"{self.name} {self.ip_address} {self.status}"

class Monitor:
    def __init__(self, device, api_client):
        self.device = device  #Now monito has a device
        self.api_client = api_client# now monitor has an api tool
    @log_execution
    def check_status(self):
        print(f"Checking status for: {self.device.name}...")

my_server = Device("Infrawatch_server", "192.168.1.50")
my_monitor= Monitor(my_server, client)

print(my_monitor.check_status())

print (my_server.get_info())
if users:
    for user in users:
        print(f" User: {user['name'] } | City: {user['address']['city']}")

else:
    print("failed to retrieve data")
