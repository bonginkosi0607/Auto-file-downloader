import os
import requests
import asyncio
import os.path as op

async def main():
    await asyncio.sleep(5)

def is_online():
    url = "https://www.kite.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False


def download(url):
    r = requests.get(url, allow_redirects=True)
    url = url.replace(":", "")
    url = url.replace("/", "")
    url = url.replace("http", "")
    url = url.replace("www", "")
    url = url.replace("com", "")
    open(url, 'wb').write(r.content)


def stab(url):
    url = url.replace(":", "")
    url = url.replace("/", "")
    url = url.replace("http", "")
    url = url.replace("www", "")
    url = url.replace("com", "")
    return url


def piped(module):
    with open("main_output.txt", 'r+') as fil:
        fil = fil.read().split("\n")
        for lin in fil:
            if module in lin:
                return True
            else:
                continue


while True:
    asyncio.run(main())
    if is_online():
        with open("main.txt", "r+") as file:
            file = file.read().__str__().split("\n")
            for line in file:
                if line.__str__().startswith("pip: "):
                    line = line.__str__().replace("pip: ", "")
                    if piped(line) != True:
                        print("pip install " + line)
                        with open("main_output.txt", "a") as ot:
                            ot.write(line + ": Completed Successfully\n")
                        os.system("pip install " + line)

                elif line.__str__().startswith("file:"):
                    line = line.__str__().replace("file: ", "")
                    if not op.exists(stab(line)):
                        print("Downloading: " + line)
                        with open("main_output.txt", "a") as ot:
                            ot.write(line + ": Completed Successfully\n")
                        download(line)
                    else:
                        continue
