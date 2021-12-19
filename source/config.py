from enum import Enum
import json


class ConfigKey(Enum):
    APPLICATION_NAME = "application-name"
    NOTIFICATION_ICON = "notification-icon"
    NOTIFICATION_SOUND = "notification-sound"


class Config:
    def __init__(self, path_to_json_config="config.json") -> None:
        with open(path_to_json_config, "r") as f:
            self.json_config = json.load(f)

    def get_value(self, key: ConfigKey) -> str:
        return self.json_config[key.value]
