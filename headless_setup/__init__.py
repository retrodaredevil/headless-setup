import locale
from pathlib import Path


SSH_FILE = Path("ssh")
WIFI_FILE = Path("wpa_supplicant.conf")
WIFI_STRING = """ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country={country}

network={{
\tssid="{ssid}"
\tpsk={password}
}}
"""


def request_boolean(default_value=None):
    if default_value is None:
        prompt = "(y/n)"
    elif default_value:
        prompt = "(Y/n)"
    else:
        prompt = "(y/N)"
    value = input(prompt).lower()
    if "n" in value:
        return False
    elif "y" in value:
        return True
    elif not value and default_value is not None:
        return default_value
    return request_boolean(default_value)


def real_main():
    ssh_enabled = SSH_FILE.exists()
    print("Enable ssh?")
    should_enable = request_boolean(True)
    if ssh_enabled != should_enable:
        if ssh_enabled:
            SSH_FILE.unlink()
            print("Removed ssh file")
        else:
            SSH_FILE.open("w").close()
            print("Created ssh file")

    wifi_message = "Configure WiFi?"
    if WIFI_FILE.exists():
        wifi_message += " (Will overwrite file)"
    print(wifi_message)
    if request_boolean(True):
        default_country = locale.getdefaultlocale()[0].split("_")[1]
        country = input("Country (default " + default_country + ") ") or default_country
        print("Setting country to " + country)
        ssid = input("SSID ")
        print("Encrypt password?")
        encrypt = request_boolean(True)
        password = input("Password ")
        if encrypt:
            import hashlib
            import binascii
            while not (8 <= len(password) < 64):
                print("Passphrase must be 8..63 characters")
                password = input("Password ")
            dk = hashlib.pbkdf2_hmac(
                'sha1',
                str.encode(password),
                str.encode(ssid),
                4096,
                256
            )
            # credit to https://stackoverflow.com/a/60684618/5434860
            password = binascii.hexlify(dk)[0:64].decode("utf8")
        else:
            password = '"' + password + '"'  # plaintext passwords need quotes around them

        with WIFI_FILE.open("w") as f:
            f.write(WIFI_STRING.format(country=country, ssid=ssid, password=password))


def main():
    try:
        real_main()
    except KeyboardInterrupt:
        print("\nExiting")


if __name__ == '__main__':
    main()
