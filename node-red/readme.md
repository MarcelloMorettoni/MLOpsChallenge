 Helpful commands

Installation of node-red detecting USB
 ```
 1914  docker run -it -p 1880:1880 -v node_red_data:/data nodered/node-red
 1917  docker run -it -p 1880:1880 -v node_red_data:/data nodered/node-red
 1925  docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered -u node-red:dialout nodered/node-red
 1926  docker run -it -p 1880:1880 -v node_red_data:/data -u node-red:dialout nodered/node-red
 1935  npm install -g --unsafe-perm node-red
 1936  node-red
 ```

Enabling Serial on WSL

 ```
 sudo modprobe vhci-hcd
 ```

Then
share the usb

```
C:\Windows\System32>usbipd attach --wsl --busid 1-8
usbipd: info: Using WSL distribution 'Ubuntu' to attach; the device will be available in all WSL 2 distributions.
usbipd: info: Using IP address 172.19.80.1 to reach the host.

C:\Windows\System32>usbipd list
Connected:
BUSID  VID:PID    DEVICE                                                        STATE
1-8    1a86:7523  USB-SERIAL CH340 (COM8)                                       Attached
1-9    046d:c548  Logitech USB Input Device, USB Input Device                   Not shared
1-10   046d:082d  HD Pro Webcam C920                                            Shared
1-11   187c:0550  USB Input Device                                              Not shared
1-12   0bda:887b  Realtek Bluetooth Adapter                                     Not shared
3-1    1235:8210  Scarlett 2i2 USB                                              Not shared
3-2    1b1c:1b80  USB Input Device                                              Not shared

Persisted:
GUID                                  DEVICE
8a6f76fa-3ee3-48f3-a394-50f45af5eeba  Arduino Mega 2560 (COM3)


C:\Windows\System32>usbipd attach --wsl --busid 1-10
usbipd: info: Using WSL distribution 'Ubuntu' to attach; the device will be available in all WSL 2 distributions.
usbipd: info: Using IP address 172.19.80.1 to reach the host.

C:\Windows\System32>
```
