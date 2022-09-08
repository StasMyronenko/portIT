from fastapi import FastAPI, Request, Response, Depends
from pymongo.database import Database

from configuration.utils import get_site_db
from site_data.data import SitesPart
from site_data.site_data_service import get_site_data, get_languages

app = FastAPI(root_path="/site_app")

# Create Admin panel for this


@app.get('/languages')
async def get_possible_languages(db: Database = Depends(get_site_db)):
    return get_languages(db)


@app.get('/{part}/{language}')
async def get_info(language: str, part: SitesPart, db: Database = Depends(get_site_db)):
    data = get_site_data(db, language, part)
    return data

