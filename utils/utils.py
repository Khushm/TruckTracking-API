from loguru import logger
from datetime import datetime


def get_mongo_data(conn, meta_data):
    try:
        query_data_list = conn.find({
            'datetime_local': {
                '$gte': datetime.strptime(meta_data['from_time'], "%Y-%m-%dT%H:%M:%S"),
                '$lte': datetime.strptime(meta_data['to_time'], "%Y-%m-%dT%H:%M:%S"),
            },
            'panel_no': meta_data['panel_no'],
            'channel_no': meta_data['camera_no']
        })
        return query_data_list
    except Exception as e:
        logger.debug(f'Error while Fetching data from Mongo: {e}')
        return []
