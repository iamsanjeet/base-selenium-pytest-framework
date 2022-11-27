import argparse
import sys
from webdrivermanager import GeckoDriverManager, ChromeDriverManager, EdgeDriverManager

def initialize_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--browser", help = "Input browser name. For e.g chrome/firefox/edge")
    args = parser.parse_args()

    return args

def validate_args(args: argparse.ArgumentParser):
    if not args.browser:
        print("Please provide a browser name to download.")
        sys.exit()

def download_and_install_driver(args):
    manager = None
    if args.browser == "chrome":
        print("Download and install driver for chrome")
        manager = ChromeDriverManager()

    if args.browser == "firefox":
        print("Download and install driver for firefox")
        manager = GeckoDriverManager()

    if args.browser == "edge":
        print("Download and install driver for edge")
        manager = EdgeDriverManager()
    
    if manager:
        download_path, install_path = manager.download_and_install()
        print(f"Download path - {download_path}\nInstall path - {install_path}")

def main(args: argparse.ArgumentParser):
    validate_args(args)
    download_and_install_driver(args)


if __name__ == "__main__":
    args = initialize_parser()
    main(args)