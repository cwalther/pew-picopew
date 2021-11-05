.. _pew-library-additions:

Pew Library Additions Reference
===============================

All functionality of the regular :py:mod:`pewpew:pew` library is supported by PicoPew. In addition, the function described here is available.

.. module:: pew

.. function:: palette([pal], [offset=0])

   Sets the mapping from the color numbers used elsewhere in the library to actual colors on the display.
   ``pal`` is a sequence (``bytes``, ``bytearray``, ``list``, …) of R, G, B, R, G, B, … values for up to 256 colors (i.e. 768 elements), each with values from 0 = off to 255 = full brightness. PicoPew only has a red-green display and ignores the blue components.

   ``offset`` cyclically shifts the palette.

   Passing no palette preserves the previous one and only adjusts the offset, which may be useful for some animations. Passing an empty palette or ``None`` sets a default palette, described below.

   Changes take effect at the next ``pew.show()``.

   The palette is preserved by ``pew.init()``, much like ``pew.brightness()``, so that a choice made by the user before starting a program stays in effect, unless the program explicitly sets its own palette (see ``tint.py``).

   This is the default palette (colors are approximate due to the very different characteristics of the LED matrix versus a computer monitor):

   .. image:: palette.png
      :align: center

   Expressed in terms of the bits of the color value, it works like this:

   = = = = = == === ====== =========================
   7 6 5 4 3 2  1   0
   = = = = = == === ====== =========================
   0 0 darkness red green  *red/green compatible*
   - - -------- --- ------ -------------------------
   0 1 hue      brightness *single-color compatible*
   - - -------- ---------- -------------------------
   1 red     green         *true-color*
   = ======= ============= =========================
