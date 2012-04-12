# This script converts SRT subtitles from CP1251 to UTF-8
# Useful to use as Folder Action on Downloads in OSX
#
# Author: Alexander Artmenko
# Source: http://github.com/svetlyak40wt/convert-srt

import datetime
import subprocess
import sys
import logging
import os.path

logging.basicConfig(filename='/tmp/utf-converter.log', level=logging.DEBUG)
logger = logging.getLogger()
logger.debug(str(datetime.datetime.today()))

for filename in sys.argv[1:]:
    logger.debug('checking filename ' + filename)
    if 'srt' in filename.lower():
        if subprocess.call('file -b "%s" | grep -i UTF > /dev/null' % filename, shell=True) != 0:
            logger.debug('converting %s to UTF-8')
            subprocess.call('iconv -f cp1251 -t utf8 "{long}" > "/tmp/{short}" && mv "/tmp/{short}" "{long}"'.format(
                short=os.path.basename(filename),
                long=filename
            ), shell=True)

