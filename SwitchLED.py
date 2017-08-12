# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import os

class SwitchLEDPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("SwitchLED on_after_start")
		os.system('gpio export 7 out')
		os.system('gpio -g write 7 1')
    
__plugin_name__ = "SwitchLED"
__plugin_version__ = "1.0.0"
__plugin_description__ = "SwitchLED Plugin"
__plugin_implementation__ = SwitchLEDPlugin()
