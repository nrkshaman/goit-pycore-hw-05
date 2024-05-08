from collections import Counter
from argparse import ArgumentParser, FileType, Namespace
from io import TextIOWrapper


def get_args() -> Namespace:
    log_levels = ["INFO", "DEBUG", "ERROR", "WARNING"]
    parser = ArgumentParser()
    #type=FileType("r") opens file and handles FileNotFoundError. Requires file.close()?
    parser.add_argument("filepath", help="Path to the file with logs", type=FileType("r"))
    #type=str.upper makes choises case insensitive
    #nargs="?" makes positional argument optional
    parser.add_argument("log_level", help="List logs of specified level, case insensitive.", choices=log_levels, type=str.upper, nargs="?")
    return parser.parse_args()

def load_logs(logs_file: TextIOWrapper) -> list[str]:
    with logs_file:
        return logs_file.readlines()

def parse_log_line(line: str) -> dict:
    date, time, log_level, *log_msg_list = line.strip().split()
    log_msg = " ".join(log_msg_list)
    return {"date": date, "time": time, "level": log_level, "message":log_msg}

def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    return filter(lambda log_dict:log_dict["level"] == level, logs)

def count_logs_by_level(logs: list[dict]) -> dict[str, int]:
    return dict(Counter(map(lambda log: log["level"], logs)))

def display_log_counts(counts: dict):
    print(f"{'Log level':<15} | Count")
    print("-"*16 + "|" + "-"*6)
    for level in counts.keys():
        print(f"{level:<15} | {counts[level]}")

def main():
    args = get_args()
    logs_list= list()
    for line in load_logs(args.filepath):
        logs_list.append(parse_log_line(line))
    display_log_counts(count_logs_by_level(logs_list))
    if args.log_level:
        for log_dict in filter_logs_by_level(logs_list, args.log_level):
            print(" ".join(log_dict.values()))


if __name__ == "__main__":
    main()
