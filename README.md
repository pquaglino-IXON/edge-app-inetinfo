# Edge App - Inet info for SecureEdge Pro

This project provides a simple web page listing all network interfaces of the SecureEdge Pro, and it is especially useful to retrieve WAN2 (OT port) IP address assigned via DHCP, since with the current firmware release it is not available.

## Features

- Webpage with listing of interfaces and current IP address / net mask
- API endpoint returning info in json format

## Prerequisites

- SecureEdge Pro (firmware version 5.8 or higher)
- Access to the SecureEdge Pro local web interface
- Ensure your environment is properly set up by following this guide: [Running custom Docker applications on the SecureEdge Pro](https://support.ixon.cloud/s/article/Running-custom-Docker-applications-on-the-SecureEdge-Pro).

## Quick Start

### 1. Download and Adjust to Your SecureEdge Pro

- Download or clone this project to your local machine.
- If you do not use the default LAN IP address for your SecureEdge Pro, update the IP address in the following files to match your device's LAN IP:
  - `buildkitd-secure-edge-pro.toml`
  - `build_and_push_containers.sh`
  - `build_and_push_containers.cmd`

### 2. Build and Push Containers

- For Unix-based systems:
  ```bash
  ./build_and_push_containers.sh
  ```
- For Windows:
  ```cmd
  build_and_push_containers.cmd
  ```

### 3. Deploy on SecureEdge Pro

1. Access the SecureEdge Pro local web interface.
2. Create and configure a new container
   - **Image:** Select inetinfo
   - **Networking** Choose "HOST" mode
   - **Environment variables** Optionally set the 'port' environment var - default is 50080

3. Start the container and access the app web interface (via IXON Cloud HTTP Web Server or LAN network)
   - Web page: [http://192.168.140.1:50080](http://192.168.140.1:50080)
   - JSON: [http://192.168.140.1:50080/json](http://192.168.140.1:50080/json)


See [LICENSE.md](LICENSE.md) for license information.
