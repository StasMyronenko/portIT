from enum import Enum


class SitesPart(str, Enum):
    header = "header"
    menu = "menu"
    auth = "auth"
    about = "about"
    footer = "footer"
