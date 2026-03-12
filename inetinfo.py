from flask import Flask, jsonify
import netifaces
import os
import logging

# set default port
port = os.getenv('port', 50080)
app = Flask(__name__)

def get_interfaces():
    interfaces = netifaces.interfaces()
    interface_data = []
    
    for interface in interfaces:
        addrs = netifaces.ifaddresses(interface)
        interface_info = {'name': interface}
        
        if netifaces.AF_INET in addrs:
            inet = addrs[netifaces.AF_INET][0]
            interface_info['ipv4'] = inet.get('addr', 'N/A')
            interface_info['netmask'] = inet.get('netmask', 'N/A')
        else:
            interface_info['ipv4'] = 'N/A'
            interface_info['netmask'] = 'N/A'
            
        interface_data.append(interface_info)
    return interface_data

@app.route('/')
def interfaces_html():
    interface_data = get_interfaces()
    html = '<h1>Router interfaces</h1><ul>'
    for iface in interface_data:
        if iface['name'] == 'end1':
            html += f'<li><tt><strong>WAN (Cloud)</strong>: {iface["ipv4"]} / {iface["netmask"]}</tt></li>'
        elif iface['name'] == 'lan5':
            html += f'<li><tt><strong>WAN2 (OT)</strong>: {iface["ipv4"]} / {iface["netmask"]}</tt></li>'
        elif iface['name'] == 'br0':
            html += f'<li><tt><strong>LAN</strong>: {iface["ipv4"]} / {iface["netmask"]}</tt></li>'
        
    html += '</ul>'
    html += '<h1>All interfaces</h1><ul>'
    for iface in interface_data:
        html += f'<li><tt><strong>{iface["name"]}</strong>: {iface["ipv4"]} / {iface["netmask"]}</tt></li>'
    html += '</ul>'
    html += f'<h1>API</h1><p><a href="http://192.168.140.1:{port}/json">http://192.168.140.1:{port}/json</a></p>'
    
    return html

@app.route('/json')
def interfaces_json():
    interface_data = get_interfaces()
    return jsonify(interface_data)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("inetinfo")
    
    logger.info(f'Starting inetinfo webserver on port {port}')
    app.run(host='0.0.0.0', port=port)
