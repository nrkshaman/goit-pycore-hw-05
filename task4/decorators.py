from functools import wraps

from task4.constants import INVALID_COMMAND, NOT_EXISTS, UNKNOWN


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return INVALID_COMMAND
        except KeyError:
            return NOT_EXISTS
        #Graceful shutdown
        except KeyboardInterrupt:
            print("byeeeeeeeee")
        except Exception:
            return UNKNOWN

    return inner
