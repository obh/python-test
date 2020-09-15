
import datetime

import jwt


def assert_quick_response(response):
    """Make sure that a request doesn't take too long
    Args:
        response (requests.Response): response object
    """
    assert response.elapsed < datetime.timedelta(seconds=1)
