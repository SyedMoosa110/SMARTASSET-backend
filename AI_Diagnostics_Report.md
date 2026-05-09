# AI Diagnostics Report - Smart Asset Tracking

This report summarizes how the Gemini 1.5 Flash AI handled hardware troubleshooting scenarios for various office equipment tracked in the system.

## Scenario 1: Screen Flickering (MacBook Pro)
**Input Specs:** MacBook Pro, 16GB RAM, macOS Sonoma, Apple M2 Pro
**User Query:** "The screen keeps flickering when I connect an external monitor."
**AI Solution:** 
1. Check the HDMI/USB-C cable for physical damage.
2. Reset NVRAM/PRAM (Shut down, then press Option-Command-P-R).
3. Update macOS to the latest version.
4. Try changing the refresh rate in System Settings > Displays.

## Scenario 2: Slow Performance (Dell XPS 15)
**Input Specs:** Dell XPS 15, 32GB RAM, Windows 11, Intel i9
**User Query:** "My laptop is running very slow even with simple tasks."
**AI Solution:**
1. Open Task Manager (Ctrl+Shift+Esc) to identify resource-heavy background processes.
2. Check for Dell SupportAssist updates and run hardware diagnostics.
3. Verify if the laptop is overheating; clean the air vents.
4. Update Intel Iris Xe or NVIDIA drivers via Device Manager.

## Scenario 3: Battery Not Charging (ThinkPad X1 Carbon)
**Input Specs:** ThinkPad X1 Carbon, 16GB RAM, Ubuntu 22.04, Intel i7
**User Query:** "Plugged in, but not charging. Battery percentage is stuck at 0%."
**AI Solution:**
1. Perform a 'Static Discharge': Unplug power, hold power button for 30 seconds.
2. Inspect the USB-C charging port for debris.
3. Check battery status in Linux terminal: `upower -i /org/freedesktop/UPower/devices/battery_BAT0`.
4. Consider replacing the CMOS battery if the system clock also resets.

## Scenario 4: Overheating (HP Spectre x360)
**Input Specs:** HP Spectre x360, 16GB RAM, Windows 11, Intel i7
**User Query:** "The fans are very loud and the bottom of the laptop is burning hot."
**AI Solution:**
1. Switch Power Mode to 'Best Power Efficiency' to reduce CPU clock speed.
2. Use HP Command Center to adjust Thermal Profile to 'Cool'.
3. Check for BIOS updates that might optimize fan curves.
4. Ensure the device is on a hard, flat surface to allow airflow.

## Scenario 5: Keyboard Keys Not Working (Surface Laptop 5)
**Input Specs:** Surface Laptop 5, 8GB RAM, Windows 11, Intel i5
**User Query:** "The 'E' and 'R' keys are completely unresponsive."
**AI Solution:**
1. Restart the device to rule out software glitches.
2. Run the Surface Diagnostic Toolkit.
3. Uninstall the Keyboard driver in Device Manager and restart.
4. If it's a hardware issue, check the ribbon cable connection (professional service recommended for Surface laptops).

---
**System Integration Note:** All chat histories are stored in the database to identify recurring hardware failures across the inventory.
