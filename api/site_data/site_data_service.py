from pymongo.database import Database

from site_data.data import SitesPart


def get_languages(db: Database):
    data = db['languages'].find({"draft": False}, {"language": True, '_id': False})
    res = []
    for el in data:
        res.append(el['language'])
    return res


def get_site_data(db: Database, language: str, part: SitesPart):
    data = db[part].find_one({"language": language})
    return data["data"] if data else {}
