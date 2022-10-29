# logging decorator
## log function name and params
## log returned result and pass it on
import logging
import sys
from functools import wraps

log = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)

def performanceLogger(name=False, params=False):
  def funcWrapper(func):
    @wraps(func)
    def callWrapper(*args, **kwargs):
      if name:
        log.debug(func.__name__)
      if params:
        log.debug("args: %s kwargs: %s ", args, kwargs)
      start = time.time()
      result = func(*args, **kwargs)
      end = time.time()
      log.debug("Took %s seconds to complete", end-start)
      return result
    return callWrapper
  return funcWrapper

