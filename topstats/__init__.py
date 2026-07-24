# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2020 Arthurdw
# SPDX-FileCopyrightText: 2024-2026 null8626

from .bot import (
  Bot,
  PartialBot,
  Ranked,
  RecentBotStats,
  TimestampedBotStats,
)
from .client import Client
from .data import Period, SortBy, Timestamped
from .errors import Error, Ratelimited, RequestError
from .ratelimiter import Ratelimiter
from .version import VERSION

__title__ = 'topstats'
__author__ = 'null8626'
__credits__ = (__author__,)
__maintainer__ = __author__
__status__ = 'Production'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2020 Arthurdw; Copyright (c) 2024-2026 null8626'
__version__ = VERSION
__all__ = (
  'Bot',
  'Client',
  'Error',
  'PartialBot',
  'Period',
  'Ranked',
  'Ratelimited',
  'Ratelimiter',
  'RecentBotStats',
  'RequestError',
  'SortBy',
  'Timestamped',
  'TimestampedBotStats',
)
