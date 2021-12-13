from fastapi import FastAPI
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from uvicorn import run
app = FastAPI(
    title="Ware House Testing API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


class ware_house_data(BaseModel):
    zone_no: int
    from_time: datetime
    to_time: datetime


@app.post('/warehouse_api/get_data/', tags=["Warehouse Data"])
def warehouse_data(data: ware_house_data):
    try:
        data_list = []
        print('Zone is : ', data.zone_no)
        # data_list = Call mongo data for zone and from_time to to_time
        return data_list
    except Exception as e:
        logger.debug(f'Error in warehouse_data: {e}')


if __name__ == '__main__':
    logger.info("Started main")
    run("main:app", host="0.0.0.0", port=5001, reload=True)
