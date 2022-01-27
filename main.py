from fastapi import FastAPI
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from uvicorn import run
from db.mongo_connection import get_mongo_client
from utils.utils import get_mongo_data
import json
from bson import json_util


while True:
    mongo_coll = get_mongo_client()
    if mongo_coll:
        logger.info("Connected to MongoDB successfully.")
        break

app = FastAPI(
    title="Truck Testing API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


class truck_data(BaseModel):
    from_time: str
    to_time: str
    panel_no: int
    camera_no: int


@app.post('/trucktrack_api/get_data/', tags=["Truck Data"])
def truck_data(data: truck_data):
    try:
        meta_data = {"from_time": data.from_time, "to_time": data.to_time,
                     "panel_no": data.panel_no, "camera_no": data.camera_no}
        data_list = get_mongo_data(mongo_coll, meta_data)
        # for x, y in enumerate(data_list):
        #     print(x, y)

        data = json_util.dumps(data_list)
        main_data = json.loads(data)
        # main_data = {"data": main_data}
        return main_data
    except Exception as e:
        logger.debug(f'Error in truck_data: {e}')


if __name__ == '__main__':
    logger.info("Started main")
    run("main:app", host="0.0.0.0", port=5001, reload=True)


'''
{
  "from_time": "2021-10-01T00:01:00.364Z",
  "to_time": "2021-10-01T11:59:00.364Z",
  "panel_no": 500003,
  "camera_no": 5
}
'''