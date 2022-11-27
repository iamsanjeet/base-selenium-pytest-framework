import argparse
import sys
from robot import run_cli, rebot_cli


def initialize_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--browser",
        help="Input browser name to run the test. For e.g chrome/firefox/edge",
        default="chrome",
    )
    parser.add_argument(
        "-u",
        "--url",
        help="Input federation base url. For e.g https://smoke3.eng.macrometa.io",
        default="https://smoke3.eng.macrometa.io",
    )
    parser.add_argument("--mm_email", help="MM email id", default="mm@macrometa.io")
    parser.add_argument("--mm_pwd", help="MM password", default="Macrometa123!@#")
    parser.add_argument("--tenant_email", help="Tenant email id", default='sanjeet.singh1@macrometa.com')
    parser.add_argument("--tenant_pwd", help="Tenant password", default='Macrometa123!@#')
    parser.add_argument(
        "-t", "--tags", help="Comma separated tag list to run"
    )
    parser.add_argument(
        "--tests", help="Tests to be run, can be a specific robot file or test dir", default='tests/'
    )
    args = parser.parse_args()

    return args

def validate_args(args):
    # TODO: implement a validator
    pass

def main(args: argparse.ArgumentParser):
    validate_args(args)
    options = [
        "--name",
        "C8 Automation GUI",
        "--variable",
        f"BROWSER:{args.browser}",
        "--variable",
        f"BASE_URL:{args.url}",
        "--variable",
        f"MM_EMAIL:{args.mm_email}",
        "--variable",
        f"MM_PWD:{args.mm_pwd}",
        "--variable",
        f"TENANT_EMAIL:{args.tenant_email}",
        "--variable",
        f"TENANT_PWD:{args.tenant_pwd}",
        "--outputdir",
        "results",
        "--loglevel",
        "DEBUG"
    ]

    # Add tag if provided
    if args.tags and args.tags != "ALL":
        options.extend(["--include", f"{args.tags}"])

    # add test dir
    options.append(args.tests)
    print(f"Run options are - {options}")
    run_cli(options)


if __name__ == "__main__":
    args = initialize_parser()
    sys.exit(main(args))