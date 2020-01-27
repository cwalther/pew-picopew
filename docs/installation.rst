Software Installation
=====================

This guide assumes that you are familiar with running MicroPython on an ESP32 as detailed in the `official MicroPython documentation <https://docs.micropython.org/en/latest/esp32/quickref.html>`_. In particular, you need to know how to transfer files to the board using `WebREPL <https://docs.micropython.org/en/latest/esp32/quickref.html#webrepl-web-browser-interactive-prompt>`_, `pyboard.py <https://docs.micropython.org/en/latest/reference/pyboard.py.html>`_, or third-party tools such as `rshell <https://github.com/dhylands/rshell>`_ or `ampy <https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy>`_. Unlike other PewPew devices using a SAMD microcontroller, PicoPew cannot appear as a USB drive.

Firmware
--------

No special firmware is needed to run PewPew programs. The stock MicroPython firmware that TinyPICOs ship with works fine, as do the `official MicroPython releases <https://micropython.org/download#esp32>`_.

Libraries
---------

Download the `PicoPew software <https://github.com/cwalther/pew-picopew>`_ from GitHub. If you are familiar with Git, you may clone it, otherwise use the *Download ZIP* option under the *Clone or download* button.

Copy the files from the *lib* folder (``pew.py``, ``random.py``, ``time.py``) to the ``/lib/`` folder on the TinyPICO. (You may need to create it using ``import os; os.mkdir('/lib')`` on the REPL, and if you are using the HTML WebREPL client, change to it using ``os.chdir('/lib')``.)

``pew.py`` is the :ref:`Pew library <pew-library-additions>`, the other two files are CircuitPython compatibility libraries that add some functions commonly used by PewPew games that are not present in MicroPython.

Programs and Games
------------------

The PicoPew software includes some optional programs in the *programs* folder:

* ``circles.py``, ``roll.py``: Non-interactive demos of the 256-color capability of the PicoPew display.
* ``tint.py``: Lets you choose a color scheme for 4-color PewPew programs – either red-green as on a PewPew Lite FeatherWing or shades of one color as on a PewPew Standalone.

It is recommended to install ``main.py`` from the `game-menu <https://github.com/pewpew-game/game-menu>`_ repository. Place it in the root of the filesystem. It will present you a menu of all ``.py`` files in the filesystem root when the device is turned on. Use the up and down buttons to move, O to select, and left and right to adjust the display brightness.

Several example games are available in the `game- repositories <https://github.com/pewpew-game>`_, often both fun to play and instructive to read. Start with `snake <https://github.com/pewpew-game/game-snake>`_, which is particularly simple. `Maze3D <https://github.com/cwalther/pewpew-game-maze3d>`_ is one of the first to take advantage of the 256-color display.

Any PewPew program should work on PicoPew as long as it is written in the common subset of CircuitPython and MicroPython. Programs that use CircuitPython-specific functionality, in particular GPIOs or other hardware access, will require some porting or additions to the compatibility libraries.
