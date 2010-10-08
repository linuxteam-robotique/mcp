= Master Control Program =

== Installation == 

 1. Copy config-sample.py into config.py

== Use mcp in a python shell ==

 * python 

>>> from mcp import MakeRobot
>>> r = MakeRobot()
INFO:Robot:READY !
>>> r
<mcp.Robot object at 0x7fca94500350>
>>> r.md
<motor.Motor object at 0x7fca945004d0>
