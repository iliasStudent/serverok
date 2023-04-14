import os
import json
import ping3

def help():
    print()
    print("Available commands")
    print("------------------")
    print("- list: Lists all the hosts that are currently being monitored")
    print("- add: Adds a new host to the list of hosts to be monitored")
    print("- remove: Removes a host from the list of hosts to be monitored")
    print("- check: Checks if the hosts in the list are responding")
    print("- help: Displays this help message")

def list():
    if os.path.exists(os.path.expanduser("~") + "/okserver/list.json"):
        print("List of hosts being monitored")
        print("-----------------------------")
        # print the list of hosts
        f = open(os.path.expanduser("~") + "/okserver/list.json", "r")
        lijst = json.load(f)
        if(len(lijst["hosts"]) > 0):
            for host in lijst["hosts"]:
                print(host)
        else:
            print("No hosts are being monitored")
            print("Use the 'add' command to add a host to the list")
        f.close()
    else:
        print("List of hosts being monitored")
        print("-----------------------------")
        print("No hosts are being monitored")
        print("Use the 'add' command to add a host to the list")

def add(host):
    if not os.path.exists(os.path.expanduser("~") + "/okserver"):
        os.mkdir(os.path.expanduser("~") + "/okserver")
    if not os.path.exists(os.path.expanduser("~") + "/okserver/list.json"):
        hosts = {"hosts": [host]}
        f = open(os.path.expanduser("~") + "/okserver/list.json", "w")
        json.dump(hosts, f)
        f.close()
    else:
        file = open(os.path.expanduser("~") + "/okserver/list.json", "r")
        lijst = json.load(file)
        lijst["hosts"].append(host)
        file.close()
        f = open(os.path.expanduser("~") + "/okserver/list.json", "w")
        json.dump(lijst, f)
        f.close()

def remove(host):
    if os.path.exists(os.path.expanduser("~") + "/okserver/list.json"):
        f = open(os.path.expanduser("~") + "/okserver/list.json", "r")
        lijst = json.load(f)
        try:
            lijst["hosts"].remove(host)
        except:
            f.close()
            print("Host not found")
            return
        f.close()
        f = open(os.path.expanduser("~") + "/okserver/list.json", "w")
        json.dump(lijst, f)
        f.close()

def check():
    if os.path.exists(os.path.expanduser("~") + "/okserver/list.json"):
        f = open(os.path.expanduser("~") + "/okserver/list.json", "r")
        lijst = json.load(f)
        f.close()
        status = {}
        for host in lijst["hosts"]:
            if ping3.ping(host) == False:
                print("Host " + host + " is not responding")
                if(not os.path.exists(os.path.expanduser("~") + "/okserver")):
                    os.mkdir(os.path.expanduser("~") + "/okserver")
                status[host] = "down"
            else:
                print("Host " + host + " is responding")
                if(not os.path.exists(os.path.expanduser("~") + "/okserver")):
                    os.mkdir(os.path.expanduser("~") + "/okserver")
                status[host] = "up"
        f = open(os.path.expanduser("~") + "/okserver/status.json", "w")
        json.dump(status, f)
        f.close()
        generateHTML()
    else:
        print("No hosts are being monitored")
        print("Use the 'add' command to add a host to the list")

def generateHTML():
    # Load server status data from status.json file
    with open(os.path.expanduser("~") + "/okserver/status.json") as f:
        server_data = json.load(f)

    # Generate HTML page
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Server Status</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f2f2f2;
            }}
            
            .container {{
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
            }}
            
            .server {{
                display: flex;
                justify-content: space-between;
                padding: 10px;
                border-bottom: 1px solid #ddd;
            }}
            
            .server-name {{
                font-weight: bold;
            }}
            
            .server-status {{
                color: green;
                font-weight: bold;
            }}
            
            .server-status.offline {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Server Status</h1>
    '''

    # Add server data to HTML page
    for server in server_data:
        html += f'''
        <div class="server">
            <div class="server-name">{server}</div>
            <div class="server-status {'up' if server_data[server] == 'up' else 'down'}">{server_data[server].capitalize()}</div>
        </div>
        '''

    # Add closing tags to HTML page
    html += '''
        </div>
    </body>
    </html>
    '''

    # Write HTML page to file
    with open(os.path.expanduser("~") + "/okserver/index.html", 'w') as f:
        f.write(html)