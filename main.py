from fastapi import FastAPI
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from uvicorn import run
from db.mongo_connection import get_mongo_client
from utils.utils import get_mongo_data

while True:
    mongo_coll = get_mongo_client()
    if mongo_coll:
        logger.info("Connected to MongoDB successfully.")
        break

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


def convert_to_string(d):
    return d.strftime("%Y-%m-%dT%H_%M_%S")

@app.post('/warehouse_api/get_data/', tags=["Warehouse Data"])
def warehouse_data(data: ware_house_data):
    try:
        data_list = []

        print('Zone is : ', data.zone_no)

        meta_data = {"zone_no": data.zone_no, "from_time": convert_to_string(data.from_time), "to_time": convert_to_string(data.to_time)}
        # data_list = Call mongo data for zone and from_time to to_time
        data_list = get_mongo_data(mongo_coll, meta_data)
        print(data_list)
        return data_list
    except Exception as e:
        logger.debug(f'Error in warehouse_data: {e}')


if __name__ == '__main__':
    logger.info("Started main")
    run("main:app", host="0.0.0.0", port=5001, reload=True)
