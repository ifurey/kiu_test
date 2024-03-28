from .kiu import (
    post_airport,
    post_client,
    post_package,
    post_travel,
)

POST_RUTES_MAPPING = {
    "/airport": post_airport,
    "/client": post_client,
    "/package": post_package,
    "/travel": post_travel,
}