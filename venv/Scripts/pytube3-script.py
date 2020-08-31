#!C:\Users\347\PycharmProjects\movietoaudio\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pytube3==9.6.4','console_scripts','pytube3'
__requires__ = 'pytube3==9.6.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pytube3==9.6.4', 'console_scripts', 'pytube3')()
    )
