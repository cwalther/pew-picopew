Assembly
========

PicoPew comes as a partially assembled kit and requires some soldering to complete assembly. It is not recommended for complete beginners to soldering, as space is quite tight in some places.

There are many possible ways of connecting a TinyPICO to the PicoPew board, depending on whether you want the TinyPICO to be removable, whether you want to add a battery and of which size, whether you want to add an `audio shield <https://www.tinypico.com/add-ons>`_, … it’s up to you to choose.

The way proposed here

* keeps the TinyPICO removable and breadboard-friendly when combined with two additional male pin headers,
* has space for a small LiPo battery between the boards,
* fits into the 3D-printed case for which a 3D model is provided.

(Battery and case are not included in the kit.)

.. image:: exploded.png
   :width: 50%
   :align: center

0. Capacitor Replacement (optional)
-----------------------------------

If your kit is from the first manufactured batch, it may have a 1.2 mm thick capacitor C1. When the LED matrix is placed on top of that, it will not sit totally flush on the board but leave a gap of about 0.2 mm. If this gap bothers you and you are comfortable soldering SMD parts, you may desolder the capacitor and replace it with the thinner one (0.9 mm) provided in the kit. If your kit does not come with a replacement capacitor, it should already have the thin one soldered and you should be able to get the LED matrix to sit flush with some force.

1. Pin Headers
--------------

Take the male pin headers and use pliers or a vise or similar tools to push or pull the pins through the black plastic part until their short part is short enough to fit into the female headers (socket strips) without leaving a gap between the plastic parts. The remaining length should be around 2.5 mm. Make sure you get this right before soldering. **If you leave the pins too long and get a gap, the whole assembly will be thicker and will not fit into the 3D-printed case.** It does not matter in which direction you push or pull the pins – the black plastic part has a groove that is meant to go toward the soldering side, but it also works the other way around.

Insert the female headers into the TinyPICO on the bottom side as shown in the picture (the side with the single PSRAM chip and the TinyPICO label) and solder them from the top side. To keep them steady and properly aligned during soldering, placing them on a breadboard using the male pin headers may be helpful.

Insert the male pin headers into the PicoPew with their long ends and solder them on the top. Again a breadboard or the female headers on the TinyPICO may be helpful to keep them in place. Be careful not to fill any of the other nearby holes with solder, as that would make it much more difficult to insert the LED matrix. Once soldered, cut the pins on the top side as flat on the surface as possible – don’t just cut the pin but also try to cut off as much of the solder hill as you can. Use side-cutters that cut at the edge if possible. To make the leftmost three solder joints of each row more pleasant to look at and touch (the rest will disappear under the LED matrix), you can heat them again after cutting and add a little more solder, which should form nice hemispherical domes on its own.

2. LED Matrix
-------------

Orient the LED matrix with the writing on the left side, toward the directional buttons. **If you mount it the wrong way, it will work, but the colors (red/green) will be swapped.** The six outermost pins will need to be bent a little to fit in the holes, and will bend outward a good deal more as you push the matrix down. The rest of the pins should go in straight. By pushing down with sufficient force and pulling on the bent pins, you should be able to get the matrix to sit flush on the board (unless you have a thick capacitor, see step 0. above). Bend the bent pins a bit more to keep it in place. Then solder all the pins on the bottom side, being careful not to melt too much of the pin header plastic. Cut the pins as closely to the board as possible again, especially if you plan to add a battery.

3. Battery (optional)
---------------------

PicoPew is designed to work with a `105 mAh LiPo battery as sold by Adafruit <https://www.adafruit.com/product/1570>`_ sandwiched between the two boards. Any others of size 401230 (4 mm thick, 12 mm wide, 30 mm long) should work as well, `these <https://www.aliexpress.com/item/1000005511849.html>`_ have been tested. They provide around 1 hour of play time, but it depends a lot on how many LEDs on the display are on and whether WiFi is on. **Caution:** TinyPICO charges them faster than recommended – so far no problems have been found with that, but don’t let them charge unattended.

For the most compact assembly, these batteries are connected by soldering their leads to the holes marked ``+`` (red) and ``-`` (black) on the PicoPew. To connect different or larger lithium ion batteries, you can alternatively solder one of the JST connectors that came with the TinyPICO to the pads provided for that on the PicoPew. Make sure to check the polarity!

Before adding a battery, place some adhesive tape on the board to cover the pins of the LED matrix and make sure they cannot pierce through the battery enclosure. When handling the battery, be very careful not to touch the leads to each other and to contacts on the circuit board, if you make a short these batteries may have enough power to blow up a trace on the board. Cut, strip, and solder one lead at a time, leaving the other taped off.

The on-off switch on the PicoPew disconnects the battery, which means that it needs to be in the ON position to charge.

4. 3D-Printed Case (optional)
-----------------------------

PicoPew works fine without a case, but adding one makes it more comfortable to hold and provides protection for the TinyPICO, both from mechanical damage and electrical discharges. If you have access to a 3D printer, you can `download the STL file <https://github.com/cwalther/picopew-hardware/blob/master/Case.stl>`_ and print it yourself. Any common FDM printer should work, the model is designed for 0.1 mm layer height and a 0.4 mm nozzle. The case clamps on the TinyPICO tightly, inserted with the USB port first. If the fit is too tight you may have to use a knife or sandpaper to loosen it.

If you want to make modifications before printing, copy the `source document <https://cad.onshape.com/documents/e3309d4ac17b46a5b68f1692/w/48c8a4f558bfebf576ff0b13/e/29a3e79e4175691d6c08b592>`_ in Onshape.
