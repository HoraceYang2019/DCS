# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:06:32 2018
-----------------------------------------------------------------------------------------------------------------
Installing OpenCV 3.4.3 on Raspberry Pi 3 Model B+
https://hk.saowen.com/a/d7b2ef7edebd0c36baddd1f858bfa0f3a0814fae09fb9bb487c6d96696d5856a
https://zlotus.github.io/2018/10/01/rbp3-opencv3/
---------------------------------------------------------------------------------------------------------
A.1: make sure your OS is current. 
    $ sudo apt-get update && time
    $ sudo apt-get -y dist-upgrade
    $ sudo apt-get install cmake

A.2: configure SSH and utilities 
  ''''Make sure SSH is enabled
    $ sudo apt-get install screen
    $ sudo apt-get install htop

A.3: free up 1GB+ by ditching Wolfram and Libreoffice
    $ sudo raspi-config 
           Advanced Options-> Expand filesystem -> reboot
    $ sudo apt-get purge wolfram-engine
    $ sudo apt-get purge libreoffice*
    $ sudo apt-get clean
    $ sudo apt-get autoremove

B.1: install dependencies
  ''' cmake for development
    $ sudo apt-get install build-essential cmake pkg-config

  ''' image IO packages  
    $ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

  ''' videos & streaming
    $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
    $ sudo apt-get install libxvidcore-dev libx264-dev
  
  ''' for GUI  
    $ sudo apt-get install libgtk2.0-dev libgtk-3-dev

  ''' for optimization
    $ sudo apt-get install libatlas-base-dev gfortran

B.2: install Python 3
    $ sudo apt-get install python3-dev

B.3: install pip3
    $ sudo apt-get install python3-pip

C.1: get the available (3.4.3) OpenCV source code
    $ wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.3.zip
    $ unzip opencv.zip
C.2 
    $ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.3.zip
    $ unzip opencv_contrib.zip

D.1: install berryconda
    $ wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh
    $ chmod +x Berryconda3-2.0.0-Linux-armv7l.sh
      ./Berryconda3-2.0.0-Linux-armv7l.sh
    $ sudo reboot

D.2: update berryconda
    $ conda update --all
    $ sudo pip install virtualenv virtualenvwrapper
    
D.3: prepare python environment
    $ conda create -n cv python=3.5.3
    $ source activate cv

   '''在cv虛擬環境下安裝numpy
    (cv)-> $ conda install numpy

E.1: compile OpenCV
    (cv)-> $ cd ~/opencv-3.4.3/
    (cv)-> $ mkdir build
    (cv)-> $ cd build

    (cv)-> $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.3/modules \
        -D BUILD_EXAMPLES=ON ..

E.2 change SWAP size for compiling opencv
    (cv)-> $ sudo nano /etc/dphys-swapfile
        CONF_SWAPSIZE=1024
    (cv)-> $ sudo /etc/init.d/dphys-swapfile stop
    (cv)-> $ sudo /etc/init.d/dphys-swapfile start

E.3: compile OpenCV
    (cv)-> $ make -j4
    '''once OpenCV builds successfully, continue the installation:'''
    (cv)-> $ sudo make install
    (cv)-> $ sudo ldconfig

E.4: change name
    (cv)-> $ cd /usr/local/lib/python3.5/site-packages/
    (cv)-> $ sudo mv cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so

E.5: link to conda
    (cv)-> $ cd ~/berryconda3/envs/cv/lib/python3.5/site-packages/
    (cv)-> $ ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so
    (cv)-> $ sudo reboot

F.1: test your OpenCV installation
    $ source activate cv
    (cv)-> $ python
    Python 3.5.3 (default, September 5 2018, 14:11:04) 
    [GCC 6.3.0 20170124] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import cv2
    >>> cv2.__version__
    '3.4.3'
    >>> 
    
F.2: reset SWAP
    (cv)-> $ sudo nano /etc/dphys-swapfile
        CONF_SWAPSIZE=100

F.3: install picamera
    $ source activate cv
    (cv)-> $ python -m pip install -U --force-reinstall setuptools picamera
    
F.4: setup virtual environment in Tonny Python IDE 
    Tools-> Options-> Interpreter-> Alternative Python3... -> Details (/home/pi/berryconda3/envs/cv/python3.5) 
-----------------------------------------------------------------------------------------------------------------
A. Basic
    1. Operations.py
    2. pc_take_photo.py
    3. Equalization.py

B. Convolution
    1. Convolutions.py

C. Detection 
    1. CornerDetect.py
    2. EdgeDetect.py
    3. SIFT.py
    4. FaceDetect.py
    

E. Raspberry
    1. pi_take_photo.py 
