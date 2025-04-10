# Ansible Web Server Deployment

This Ansible project automates the deployment of a scalable web server stack with the following components:
- Nginx as a reverse proxy
- Docker for containerization
- Flask web application
- UFW firewall configuration
- Prometheus Node Exporter and Grafana for monitoring

## Prerequisites

1. Ansible installed on your control machine
2. SSH access to target servers
3. SSH keys set up for passwordless authentication
4. Ubuntu 20.04 or later on target servers

## Project Structure

```
ansible-project/
├── inventory/
│   └── hosts
├── roles/
│   ├── common/
│   ├── nginx/
│   ├── docker/
│   ├── webapp/
│   ├── firewall/
│   └── monitoring/
└── site.yml
```

## Configuration

1. Update the inventory file (`inventory/hosts`) with your server details:
   ```
   [webservers]
   web1 ansible_host=YOUR_SERVER1_IP ansible_user=ubuntu
   web2 ansible_host=YOUR_SERVER2_IP ansible_user=ubuntu
   ```

2. Ensure your SSH key is properly set up:
   ```bash
   ssh-copy-id ubuntu@YOUR_SERVER_IP
   ```

## Usage

1. Test the connection to your servers:
   ```bash
   ansible all -i inventory/hosts -m ping
   ```

2. Run the playbook:
   ```bash
   ansible-playbook -i inventory/hosts site.yml
   ```

## Accessing the Services

- Web Application: http://YOUR_SERVER_IP
- Grafana Dashboard: http://YOUR_SERVER_IP:3000
  - Default credentials: admin/admin

## Security Notes

- The firewall is configured to allow only necessary ports (22, 80, 443)
- All services are configured with security best practices
- Sensitive data should be stored in Ansible Vault

## Monitoring

- Prometheus Node Exporter runs on port 9100
- Grafana is configured to collect metrics from Node Exporter
- Basic system metrics are collected automatically

## Maintenance

To update the deployment:
```bash
ansible-playbook -i inventory/hosts site.yml
```

To restart services:
```bash
ansible-playbook -i inventory/hosts site.yml --tags restart
``` 