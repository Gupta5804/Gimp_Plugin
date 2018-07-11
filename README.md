# Gimp Plugin

![alt text](http://www.rawble.com/skin/frontend/sm_market/default/images/logo.png "Rawble")


#### Plugin for gimp 2.8 to add custom product images


Prerequisites
--------------
* Install Gimp 2.8 [Download Here](https://www.gimp.org/downloads/)


Installation
--------------

1. Install Gimp 2.8 and run the program once and close it.
2. Download the repository as a zip file and extract it.
3. Copy the Contents Inside Gimp_plugin-master to ~C/users/`Your user`/.gimp-2.8/plug-ins


Usage
----------
1. Open Gimp 2.8
2. Go to `File > new` and create a new image of any size.
3. Go to `File > rawbleproducts`
4. Select the application,form and image of product and click ok.
5. Export the image created.

To Add a new Application
--------------------------
1. Open C:\Users\ `Your User` \ rawble_products.py   in a editor.
2. Add the product Name at the end of the list at line 143 .(may change)
3. Add the address of the product by copying the last elif code and change the option number.
4. Add the image file of size approx 330x397 in .gimp-2.8\application folder


To Add a new Form
--------------------------
1. Open C:\Users\ `Your User` \ rawble_products.py   in a editor.
2. Add the product Name at the end of the list at line 147 .(may change)
3. Add the address of the Form by copying the last elif code and change the option number.
4. Add the image file of any size in .gimp-2.8\form folder.


