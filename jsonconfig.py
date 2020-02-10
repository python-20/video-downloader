import json


def configure():
    with open("config.json", "r") as config:
        config = json.load(config)
        # print(config)
        for key in config:
            print(f"{key}: {config[key]}")


if __name__ == "__main__":
    configure()
