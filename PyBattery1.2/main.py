# python script showing battery details
# If you do not have psutil, pygame module you can install with using pip in Terminal
import psutil  # (pip install psutil)

import time

from win10toast import ToastNotifier

toaster = ToastNotifier()


# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


battery = psutil.sensors_battery()

battery_life = battery.percent
battery_percentage = str(battery_life) + "%"
battery_list = list(battery)
print("Your current battery status:- ", battery_percentage)
if battery_list[2]:  # checking if power plugged on.
    print("Charger Plugged IN!!")

    while battery_life < 100:
        if battery_life <= 20:
            battery = psutil.sensors_battery()
            battery_life = battery.percent
            print("Your battery is {} charged, going for sleep for 1 Hour ".format(battery_percentage))
            time.sleep(3600)  # 3600 seconds means 1 Hour

        elif 20 < battery_life <= 40:
            battery = psutil.sensors_battery()
            battery_life = battery.percent
            print("Your battery is {} charged, going for sleep for 45 minutes ".format(battery_percentage))
            time.sleep(2700)  # 1800 seconds means half an hour

        elif 41 <= battery_life <= 50:
            battery = psutil.sensors_battery()
            battery_life = battery.percent
            print("Your battery is {} charged, going for sleep for Half an Hour ".format(battery_percentage))
            time.sleep(1800)  # 1800 seconds means half an hour

        elif 51 <= battery_life <= 60:
            battery = psutil.sensors_battery()
            battery_life = battery.percent
            print("Your battery is {} charged, going for sleep for 25 minutes ".format(battery_percentage))
            time.sleep(1500)  # 1500 seconds means 25 minutes

        elif 61 <= battery_life <= 80:
            battery = psutil.sensors_battery()
            battery_life = battery.percent
            print("Your battery is {} charged, going for sleep for 20 minutes ".format(battery_percentage))
            time.sleep(1200)  # 1200 seconds means 20 minutes

        elif 81 <= battery_life <= 90:
            battery = psutil.sensors_battery()
            battery_life = battery.percent
            print("Your battery is {} charged, going for sleep for 10 minutes ".format(battery_percentage))
            time.sleep(600)  # 600 seconds means 10

        elif 91 <= battery_life <= 95:

            battery = psutil.sensors_battery()
            battery_life = battery.percent
            print("Your battery is {} charged, going for sleep for 7 minutes ".format(battery_percentage))
            time.sleep(420)  # 420 minutes means 7 minutes

        elif 96 <= battery_life <= 98:
            battery = psutil.sensors_battery()
            battery_life = battery.percent
            print(" Battery will full charge soon")
            print("Your battery is {} charged, going for sleep for  2 minutes ".format(battery_percentage))
            time.sleep(120)  # 120 seconds means 2 minutes

        elif battery_life == 99:
            battery = psutil.sensors_battery()
            battery_life = battery.percent
            print(" Battery will full charge soon")
            print("Your battery is {} charged, going for sleep for  2 minutes ".format(battery_percentage))
            time.sleep(30)  # 120 seconds means half a minutes

        else:
            print("Your battery is {} charged, going for sleep fo 2 minutes".format(battery_percentage))

            time.sleep(120)
            battery = psutil.sensors_battery()
            battery_life = battery.percent

    else:

        print("Battery percentage : ", battery.percent)
        toaster.show_toast("PyBattery", "Battery full charged", threaded=True, icon_path=None, duration=3)

        if battery.power_plugged:
            print("Please Unplug the charger")
        else:
            print()

        # converting seconds to hh:mm:ss
        print("Battery left : ", convertTime(battery.secsleft))
        print("full charge")

else:
    print("Plug In your charger than rerun the program")
while True:
    continue

author = "Pranshu raj"
