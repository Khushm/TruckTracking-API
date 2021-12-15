import json

from loguru import logger


def get_mongo_data(conn, meta_data):
    try:
        main_list = []
        query_data_list = conn.find({
            "Zone_ID": meta_data["zone_no"],
            "From_Time": {"$gt": meta_data["from_time"]},
            "To_Time": {"$lt": meta_data["to_time"]}
        })
        print(query_data_list)
        for query_data in query_data_list:
            del query_data["_id"]
            print(query_data)
            # query_data = str(query_data)
            main_list.append(query_data)
        return main_list
    except Exception as e:
        logger.debug(f'Error while Fetching data from Mongo: {e}')
        return []
