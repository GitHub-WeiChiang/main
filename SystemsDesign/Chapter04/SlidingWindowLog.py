import time
import threading
import math

# Typing module.
from typing import List
# Datetime module.
from datetime import datetime

lock = threading.Lock()


class SlidingWindowLog:
    def __init__(self, request_limit: int, time_interval: int):
        """
        :param request_limit:
            The maximum number of requests that are acceptable within the set time interval.
        :param time_interval:
            The interval setting in seconds.
        """

        # Parameter check.
        if request_limit < 1:
            raise ValueError("The request limit should be a positive integer.")
        if time_interval < 1:
            raise ValueError("The time interval should be at least 1 second.")

        # Setting parameters.
        self.__request_limit = request_limit
        self.__time_interval = time_interval

        # Log... just a log...
        # Queue operation (FIFO).
        self.__log: List[float] = list()

    def is_pass(self) -> dict:
        # Get current time.
        date_time: datetime = datetime.now()
        # Convert to unix timestamp format.
        current_unix_timestamp: float = time.mktime(date_time.timetuple())

        with lock:
            # Add new request timestamp to log.
            self.__log.append(current_unix_timestamp)

            # Log size is less than limit (this can effectively improve the performance).
            if len(self.__log) <= self.__request_limit:
                # Request "can pass" through.
                return {
                    "is_pass": True,
                    "X-RateLimit-Limit": self.__request_limit,
                    "X-RateLimit-Remaining": self.__request_limit - len(self.__log)
                }

            # Get start time of current time interval.
            current_interval_start_unix_timestamp: float = current_unix_timestamp - self.__time_interval

            # Iterate to discard expired timestamps to avoid accumulating too many logs.
            while len(self.__log) > 0 and self.__log[0] <= current_interval_start_unix_timestamp:
                # Discard timed out timestamps.
                self.__log.pop(0)

            # Log size is less than limit.
            if len(self.__log) <= self.__request_limit:
                # Request "can pass" through.
                return {
                    "is_pass": True,
                    "X-RateLimit-Limit": self.__request_limit,
                    "X-RateLimit-Remaining": self.__request_limit - len(self.__log)
                }

            # The number of seconds (approximate value) remaining util then next acceptable request interval begins.
            x_rate_limit_reset: int = math.ceil(
                self.__log[len(self.__log) - self.__request_limit] - current_interval_start_unix_timestamp
            )

            # Request "can't pass" through.
            return {
                "is_pass": False,
                "X-RateLimit-Reset": x_rate_limit_reset
            }
