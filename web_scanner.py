import requests
import sys
import json


class web_scanner:
    def __init__(self, url):
        self.security_headers = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-XSS-Protection",
            "X-Frame-Options",
            "X-Content-Type-Options",
        ]
        self.info_headers = [
            "Server",
            "X-Powered-By",
            "X-AspNet-Version",
            "X-Runtime",
            "X-Version",
            "X-UA-Compatible",
        ]
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }

    def get_url(self):
        try:
            r = requests.get(self.url, headers=self.headers)
            print(r.status_code)
        except Exception as e:
            print(e)
            sys.exit(1)

    def get_headers(self):
        self.r_security = []
        self.r_info = []
        try:
            r = requests.get(self.url, headers=self.headers)
            # compare response headers with security headers
            print("[*] Security headers missing:")
            for header in self.security_headers:
                if header not in r.headers:
                    self.r_security.append(header)
                    print("[-]", header, "not found")
            # compare response headers with info headers
            print("[*] Information filtering:")
            for header in self.info_headers:
                if header in r.headers:
                    self.r_info.append(header)
                    print("[+]", header, "found")
        except Exception as e:
            print(e)
            sys.exit(1)
        building_json = {"sec_headers": self.r_security, "info_headers": self.r_info}
        data = json.dumps(building_json)
        return data

    def send_headers():
        pass
