from fastapi import APIRouter

router = APIRouter()


@router.get("/scrape")
async def scrape_endpoint(url: str):
    return {"status": "success"}
