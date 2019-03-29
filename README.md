#Mints Data Logger C1 Plus 

## Sample Data Output
$HCHDT,274.7,T*2F </br>
$WIMWV,261.0,R,1.4,N,A*23</br>
$GPGGA,,,,,,0,,,,,,,,*66</br>
$GPVTG,,,,,,,,,N*30</br>
$GPZDA,,,,*48</br>
$WIMDA,29.3882,I,0.9952,B,20.9,C,,,40.0,,6.7,C,,,,,,,,*40</br>
$YXXDR,C,,C,WCHR,C,,C,WCHT,C,,C,HINX,P,0.9952,B,STNP*4C</br>
$YXXDR*4F</br>

## User Previledges 
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
