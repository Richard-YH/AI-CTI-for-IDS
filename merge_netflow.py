# Merge nfcapd from 2023010200 to 2023053123

import csv
import subprocess
import glob

def nfcapd_to_list(file_path):
    command = ['nfdump', '-r', file_path, '-o', 'csv']
    result = subprocess.run(command, capture_output=True, text=True)


    lines = result.stdout.strip().split("\n")[1:-3]

    return [line.split(",") for line in lines]


pattern = './IDS_CTI dataset/netflow_malicious/2023*/nfcapd.*'
nfcapd_files = glob.glob(pattern)
nfcapd_files.sort()

all_data = []

for file in nfcapd_files:
    all_data.extend(nfcapd_to_list(file))

# header name
# headers = ["ts", "te", "td", "sa", "da", "sp", "dp", "pr", "flg", "fwd", "stos", "ipkt", "ibyt", "opkt", "obyt", "in", "out", "sas", "das", "smk", "dmk", "dtos", "dir", "nh", "nhb", "svln", "dvln", "ismc", "odmc", "idmc", "osmc"] + [f"mpls{i}" for i in range(1, 11)] + ["cl", "sl", "al", "ra", "eng", "exid", "tr"]
headers = ["start_time", "end_time", "duration_time", "source_address", "destination_address", "source_port", "destination_port", "protocol", "flags", "forwarding_status", "source_type_of_service", "ingress_packet_count", "ingress_byte_count", "egress_packet_count", "egress_byte_count", "ingress_interface", "egress_interface", "source_autonomous_system", "destination_autonomous_system", "source_mask", "destination_mask", "destination_type_of_service", "direction", "next_hop_ip", "next_hop_bgp_ip", "source_vlan", "destination_vlan", "ingress_source_mac_address", "egress_destination_mac_address", "ingress_destination_mac_address", "egress_source_mac_address"] + [f"mpls_label_{i}" for i in range(1, 11)] + ["client_latency", "server_latency", "application_latency", "router_ip_address_exported", "exporter_engine_type_id", "exporter_id", "transition"]

# write all_data to csv
csv_file_path = './netflow.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)  
    writer.writerows(all_data)

print(f"Data written to {csv_file_path}")
