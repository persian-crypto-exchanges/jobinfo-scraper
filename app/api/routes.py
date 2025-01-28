from fastapi import APIRouter
from app.scraping import scraper
router = APIRouter()


@router.get("/scrap")
async def scrap_endpoint():
    wallex_scraped = scraper.scap_wallex()
    return {"status": wallex_scraped}
