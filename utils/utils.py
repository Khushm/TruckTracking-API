from loguru import logger


def get_mongo_data(conn, meta_data):
    try:
        query_data_list = conn.find({
            "Zone": meta_data["zone_no"],
            "From_Time".split(".")[0]: meta_data["from_date"],
            "To_Time".split(".")[0]: meta_data["to_date"]

            # "From_Time": {"$gt": meta_data["from_date"]},
            # "To_Time": {"$lt": meta_data["to_date"]}
        })
        return query_data_list
    except Exception as e:
        logger.debug(f'Error while Fetching data from Mongo: {e}')
        return []
