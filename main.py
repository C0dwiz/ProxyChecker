import requests
import sys
from colorama import Fore, Style, init


class ProxyChecker:
    def __init__(self, filename: str):
        self.filename = filename
        self.proxies = self._load_proxies()

    def _load_proxies(self):
        try:
            with open(self.filename, "r") as file:
                proxies = [proxy.strip() for proxy in file if proxy.strip()]
            print(
                Fore.GREEN
                + f"Загружено {len(proxies)} прокси из файла '{self.filename}'."
            )
            return proxies
        except FileNotFoundError:
            print(Fore.RED + f"Ошибка: Файл '{self.filename}' не найден.")
            sys.exit(1)

    def _check_proxy(self, proxy: str):
        try:
            response = requests.get(
                "http://httpbin.org/ip",
                proxies={"http": proxy, "https": proxy},
                timeout=5,
            )
            if response.status_code == 200:
                print(Fore.GREEN + f"Прокси {proxy} работает! Ответ: {response.json()}")
            else:
                print(
                    Fore.YELLOW
                    + f"Прокси {proxy} не работает! Код ответа: {response.status_code}"
                )
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Прокси {proxy} не работает! Ошибка: {e}")

    def run(self):
        for proxy in self.proxies:
            self._check_proxy(proxy)


def main():
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Использование: python main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    proxy_checker = ProxyChecker(filename)
    proxy_checker.run()


if __name__ == "__main__":
    init(autoreset=True)
    main()
