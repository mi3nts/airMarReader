# Mints Data Logger C1 Plus 

## Air Mar Reader 
### Sample Data Output
$HCHDT,274.7,T*2F </br>
$WIMWV,261.0,R,1.4,N,A*23</br>
$GPGGA,,,,,,0,,,,,,,,*66</br>
$GPVTG,,,,,,,,,N*30</br>
$GPZDA,,,,*48</br>
$WIMDA,29.3882,I,0.9952,B,20.9,C,,,40.0,,6.7,C,,,,,,,,*40</br>
$YXXDR,C,,C,WCHR,C,,C,WCHT,C,,C,HINX,P,0.9952,B,STNP*4C</br>
$YXXDR*4F</br>

### User Previledges 
- Udev Rules 
sudoedit /etc/udev/rules.d/50-mintsusb.rules</br>
```
KERNEL=="ttyUSB[0-9]*",MODE="0666"
KERNEL=="ttyACM[0-9]*",MODE="0666"
```

- Sudo Previledges 
```
sudo usermod -a -G sudo teamlary
sudo usermod -a -G dialout teamlary
```

- Write to folders owned by teamlary
```
/home/teamlary/gitHubRepos/
```

# Wiring 

## Airmar 
Inspired from [this link](https://www.fondriest.com/pdf/airmar_wx_manual.pdf)

| Airmar      | Connection    |
| ----------- | ------------- |
| 1) Red      | V+: 12 V      |
| 2) Black    | Ground:0 V    |
| 3) White    | TX            |
| 4) Bare     |               |
| 5) Bare     | Shield        |
| 6) Bare     |               |
| 7) Yellow   | RX            |
| 8) Orange   | No Connection |
| 9) Blue     | No Connection |
| 10) Bare    | Shield        |

Connect Blue and Orange togeather. On the rs232 cable make sure the ground is common. 

## 	USB-RS232-WE-1800-BT_5.0 
Inspired from [this link](https://www.ftdichip.com/Support/Documents/DataSheets/Cables/DS_USB_RS232_CABLES.pdf)

| Airmar      | Connection    |
| ----------- | ------------- |
| 1) Red      | V+: 12 V      |
| 2) Black    | Ground:0 V    |
| 3) White    | TX            |
| 4) Bare     |               |
| 5) Bare     | Shield        |
| 6) Bare     |               |
| 7) Yellow   | RX            |
| 8) Orange   | No Connection |
| 9) Blue     | No Connection |
| 10) Bare    | Shield        |












