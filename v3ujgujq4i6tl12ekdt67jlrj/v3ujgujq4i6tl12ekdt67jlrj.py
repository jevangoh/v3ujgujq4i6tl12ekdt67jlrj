from typing import Any
from structlog.stdlib import _FixedFindCallerLogger as FixedFindCallerLogger

import fwzzlhjtb520ky7cblteynsev as the_log_types


class v3ujgujq4i6tl12ekdt67jlrj(FixedFindCallerLogger):
    def record(self, msg: object, *args: object, **kwargs: Any):
        self._log(the_log_types._.record.level, msg, args, **kwargs)

    def inform(self, msg: object, *args: object, **kwargs: Any):
        self._log(the_log_types._.information.level, msg, args, **kwargs)

    def notify(self, msg: object, *args: object, **kwargs: Any):
        self._log(the_log_types._.notice.level, msg, args, **kwargs)

    def alert(self, msg: object, *args: object, **kwargs: Any):
        self._log(the_log_types._.alert.level, msg, args, **kwargs)

    def warn(self, msg: object, *args: object, **kwargs: Any):
        self._log(the_log_types._.warning.level, msg, args, **kwargs)
