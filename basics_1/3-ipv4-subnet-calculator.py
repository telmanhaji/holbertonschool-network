import ipaddress
import sys


def calculate_subnet(ip_cidr):
    """
    Calculates subnet details for a given IPv4 CIDR string.
    """
    try:
        # strict=False allows inputting an IP that has host bits set
        # (e.g., 192.168.1.50/24)
        network = ipaddress.ip_network(ip_cidr, strict=False)

        # Ensure we are strictly dealing with IPv4
        if network.version != 4:
            return {'Error': 'This tool is optimized for IPv4 only.'}

        network_id = str(network.network_address)
        broadcast_ip = str(network.broadcast_address)

        # Logic for usable IPs
        # /32 (1 address) and /31 (2 addresses) technically have no
        # usable hosts in standard subnetting (RFC 3021 excluded)
        if network.num_addresses > 2:
            first_usable_ip = str(network.network_address + 1)
            last_usable_ip = str(network.broadcast_address - 1)
            total_usable_hosts = network.num_addresses - 2
        else:
            first_usable_ip = "N/A (Point-to-Point or Single IP)"
            last_usable_ip = "N/A"
            total_usable_hosts = 0

        return {
            'Network ID': network_id,
            'Broadcast IP': broadcast_ip,
            'First usable IP': first_usable_ip,
            'Last Usable IP': last_usable_ip,
            'Total usable hosts count': total_usable_hosts
        }

    except ValueError as e:
        return {'Error': f"Invalid CIDR format. Details: {e}"}


def main():
    print("--- IPv4 Subnet Calculator ---")
    # Split long line for PEP 8 compliance
    prompt = "Enter IPv4 in CIDR format (e.g., 192.168.100.50/22): "
    user_input = input(prompt).strip()

    if not user_input:
        print("Error: Input cannot be empty.")
        return

    result = calculate_subnet(user_input)

    print("-" * 30)
    for key, value in result.items():
        # Clean formatting for the output
        print(f"{key:<25}: {value}")
    print("-" * 30)


if __name__ == "__main__":
    main()

