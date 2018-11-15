import platform
import subprocess
import wmi
def services():
    c = wmi.WMI()
    for s in c.Win32_Service (StartMode="Auto", State="Stopped"):
        if input ("Restart %s? " % s.Caption).upper () == "Y":
            s.StartService ()
def sys_version():
    c = wmi.WMI ()
    #获取操作系统版本
    for sys in c.Win32_OperatingSystem():
        print ("Version:%s" % sys.Caption.encode("UTF"),"Vernum:%s" % sys.BuildNumber)
        print (sys.OSArchitecture.encode("UTF"))#系统是位还是位的
        print (sys.NumberOfProcesses) #当前系统运行的进程总数
def cpu_mem():
    c = wmi.WMI ()
  #CPU类型和内存
    for processor in c.Win32_Processor():
        #print "Processor ID: %s" % processor.DeviceID
        print ("Process Name: %s" % processor.Name.strip())
        for Memory in c.Win32_PhysicalMemory():
            print ("Memory Capacity: %.fMB" %(int(Memory.Capacity)))
def network():
    c = wmi.WMI ()
    #获取MAC和IP地址
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled= True):
        print ("MAC: %s" % interface.MACAddress )
        for ip_address in interface.IPAddress:
            print ("ip_add: %s" % ip_address )


def w_disk():

    c = wmi.WMI()
    i = 0
    # 获取磁盘信息
    for disk in c.Win32_LogicalDisk (DriveType=3):
        # print(disk)
        # 可用大小G
        a = round(int(disk.FreeSpace) / (1024*1024*1024),2)
        print(a)
        # 可用大小%
        b = int(100.0 * float(disk.FreeSpace) /float(disk.Size))
        print(b)
        if disk.Caption == "c:":
            if (a < 2) or (b < 10):
                i += 1
            else:
                i += 0
        else:
            if (a < 10) or (b < 10):
                i += 1
            else:
                i += 0
    print (i)

def L_disk():
    free = subprocess.getstatusoutput('df -h|grep dev|egrep -v "tmp|var|shm"')
    list = free[1].split('\n')
    i = 0
    for disk in range(len(list)):
        vd = list[disk][6:8]
        a = list[disk].split()[3]
        if a[-1] == 'T':
            a = int(float(a[:-1]))*1024
        else:
            a = int(float(a[:-1]))
            b = 100 - int(list[disk].split()[4][:-1])
        if vd == "da":
            if (a < 2) or (b < 10):
                i += 1
            else:
                i += 0
        else:
            if (a < 10) or (b < 10):
                i += 1
    else:
        i += 0
    print (i)

if __name__ == "__main__":
    os = platform.system()
    if os == "Windows":
        # w_disk()
        # sys_version()
        # cpu_mem()
        # network()
        services()
    elif os == "Linux":
        L_disk()