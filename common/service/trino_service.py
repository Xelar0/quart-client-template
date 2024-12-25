from common.config.config import CYODA_AI_URL
from common.util.utils import send_post_request

def get_trino_schema_id_by_entity_name(entity_name: str):
    return "89b73030-c2c3-11ef-8531-961a8c79180b"

#runs sql to retrieve data
def run_sql_query(token, query):
    resp = send_post_request(token, CYODA_AI_URL, "api/v1/trino/run-query", query)
    return resp.json()["message"]