# Code
```
sudo su -
yum install python3 -y
yum install libXcomposite libXcursor libXi libXtst libXrandr alsa-lib mesa-libEGL libXdamage mesa-libGL libXScrnSaver git wget -y
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh

sh Anaconda3-2022.10-Linux-x86_64.sh
source ~/.bashrc

git clone https://github.com/manifoldailearning/ml-deployment-demo-1

cd ml-deployment-demo-1
sudo apt install python3-pip
python3 pip install -r requirements.txt

flask --app app run 

```