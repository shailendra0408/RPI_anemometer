import MacTmp
import psutil
battery = psutil.sensors_battery()
percent = battery.percent

print (MacTmp.CPU_Temp())
print (MacTmp.GPU_Temp())
print (f"Battery Percentage: {percent}%")


