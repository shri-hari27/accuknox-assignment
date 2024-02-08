def analyze_log():
    log_file = "access.log"
    with open(log_file, "r") as file:
        lines = file.readlines()

    num_404_errors = sum(1 for line in lines if "404" in line)

    page_requests = {}
    for line in lines:
        page = line.split()[6]
        page_requests[page] = page_requests.get(page, 0) + 1

    ip_requests = {}
    for line in lines:
        ip = line.split()[0]
        ip_requests[ip] = ip_requests.get(ip, 0) + 1

    print(f"Number of 404 errors: {num_404_errors}")
    print("Most requested pages:")
    for page, count in sorted(page_requests.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{page}: {count} requests")
    print("IP addresses with most requests:")
    for ip, count in sorted(ip_requests.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{ip}: {count} requests")

def main():
    analyze_log()

if __name__ == "__main__":
    main()