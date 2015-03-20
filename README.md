# DSA815-TG
Rigol DSA815-TG Basic Communications Library, connected via VISA (tested over USB although other IO connections should work).

To use this you'll need to install:

  * Ultra Sigma from Rigol [OPTIONAL: Can also just copy/paste the address from the DSA815 display]
  * Python 2.7 with PySide, suggested to just install WinPython (see http://winpython.sourceforge.net/)
  * pyvisa, use easy_install or pip install

Once your system is running, just run dp815.py via your installed Python. Supply the address string in the test file (open Ultra Sigma, make sure it finds your analyzer, and copy-paste address string from that, OR just look in the 'utilities' menu). Will look something like USB0::0x1AB1::0x0960::DSA8Axxxxxx::INSTR

If the address copied from the DSA815 display doesn't work, install Ultra Sigma to confirm it is detected there.