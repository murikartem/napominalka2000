import logging
import asyncio
from loader import *

import handlers.start
import handlers.tasks
import handlers.AddTask
import handlers.RewriteTask
import handlers


async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
