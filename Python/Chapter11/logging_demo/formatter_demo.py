__author__ = "ChiangWei"
__date__ = "2022/5/24"

import logging
import sys

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)

logger.log(logging.ERROR, '發生了 XD 錯誤')
