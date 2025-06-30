from modules.port_scan import scan_ports
from modules.http_headers import get_headers
import json

def main():
    target = input("Enter a domain or IP: ").strip()

    ports = scan_ports(target)
    headers = get_headers(target)

    result = {
        "target": target,
        "open_ports": ports,
        "http_headers": headers
    }

    print("\n[+] Scan Results:")
    # Convert int keys to strings for JSON
    result["open_ports"] = {str(k): v for k, v in result["open_ports"].items()}
    print(json.dumps(result, indent=2))


    with open(f"output/reports/{target}_report.json", "w") as f:
        json.dump(result, f, indent=2)
        print(f"\n[+] Report saved to output/reports/{target}_report.json")

if __name__ == "__main__":
    main()
