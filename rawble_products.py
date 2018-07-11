#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=nmb-0KcgXzI
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *
import os

def rawble_products(image, drawable,option_application="",option_form="",file_var=""):
    #pdb.gimp_undo_push_group_start(image)
    new_width = 250
    new_height = 300
    offx=0
    offy=0
    #pdb.gimp_image_resize(image, new_width, new_height, offx, offy)
    pdb.gimp_image_scale(image, new_width, new_height)
    
    
    
    
  # Application Options  
    
    if(option_application == 0 ):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Eye-Contour.jpg")
    elif(option_application == 1):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Hair-Care.jpg")
    elif(option_application == 2):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Men-Care.jpg")
    elif(option_application == 3):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Perfumes-and-fragrances.jpg")
    elif(option_application == 4):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Skin-Care.jpg")
    elif(option_application == 5):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Sun-Care.jpg")
    elif(option_application == 6):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Toileteries.jpg")
    elif(option_application == 7):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Baby-Food.jpg")
    elif(option_application == 8):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Bakery.jpg")
    elif(option_application == 9):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Beverages.jpg")
    elif(option_application == 10):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Cereal.jpg")
    elif(option_application == 11):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Confectionery.jpg")
    elif(option_application == 12):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Dairy-Products.jpg")
    elif(option_application == 13):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Desserts-and-icecream.jpg")
    elif(option_application == 14):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Fats-oils-sweets.jpg")
    elif(option_application == 15):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Fruits-and-vegetables.jpg")
    elif(option_application == 16):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Functional-food.jpg")
    elif(option_application == 17):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\grain-mill-products.jpg")
    elif(option_application == 18):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Ready-meal.jpg")
    elif(option_application == 19):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Meat-Products.jpg")
    elif(option_application == 20):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Snacks-Food")
    elif(option_application == 21):
        img_application = os.path.expanduser("~\.gimp-2.8\plug-ins\\applications\Seasonings.jpg")
    
 # Form Options
    
    if(option_form == 0):
        img_form_addr = os.path.expanduser("~\.gimp-2.8\plug-ins\\form\liquid.jpg")
    elif(option_form == 1):
        img_form_addr = os.path.expanduser("~\.gimp-2.8\plug-ins\\form\powder.jpg")
    elif(option_form == 2):
        img_form_addr = os.path.expanduser("~\.gimp-2.8\plug-ins\\form\oil.jpg")

    
    
    
    # function code goes here...
    #layer_one = gimp.Layer(image, "application", image.width, image.height, RGB_IMAGE,100, NORMAL_MODE)
    #image.add_layer(layer_one,0)
    #pdb.gimp_image_resize(img_application, new_width, new_height, offx, offy)
    layer_one = pdb.gimp_file_load_layer(image, img_application)
    image.remove_layer(image.layers[0])
    pdb.gimp_image_insert_layer(image, layer_one, None, 0)
    #image.remove_layer(image.layers[1])


    #pdb.gimp_image_resize(img_form, 100, 100, 0, 0)
    img_form_layer = pdb.gimp_file_load_layer(image,img_form_addr)
    #pdb.gimp_image_insert_layer(img_form, img_form_layer, None, 0)
    #pdb.gimp_message(img_form.layers)
    #active_layer = pdb.gimp_image_get_active_layer(img_form)
    pdb.gimp_image_insert_layer(image, img_form_layer ,None, 0)
    #pdb.gimp_layer_resize(img_form_layer, 100, 100, 0, 0)
    pdb.gimp_layer_scale(img_form_layer, 70, 70, False)
    img_form_layer.add_alpha()
    pdb.gimp_image_select_ellipse(image, 0, 0, 0, 70, 70)
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_clear(img_form_layer)
    pdb.gimp_selection_none(image)
    #pdb.gimp_drawable_free_shadow(img_form_layer)
    pdb.gimp_layer_translate(img_form_layer, 170, 220)


    img_product_layer = pdb.gimp_file_load_layer(image,file_var)
    pdb.gimp_image_insert_layer(image, img_product_layer ,None, 0)
    pdb.gimp_layer_scale(img_product_layer, 70, 70, False)
    img_product_layer.add_alpha()
    pdb.gimp_image_select_ellipse(image, 0, 0, 0, 70, 70)
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_clear(img_product_layer)
    pdb.gimp_selection_none(image)
    pdb.gimp_layer_translate(img_product_layer, 170, 140)

    #pdb.script_fu_drop_shadow(image, drawable, Offset X, Offset Y, Blur radius, color, Opacity, toggle)
    pdb.script_fu_drop_shadow(image, img_form_layer, 2, 4, 17, (0,0,0), 100, 1)
    pdb.script_fu_drop_shadow(image, img_product_layer, 2, 4, 17, (0,0,0), 100, 1)



    #layer_two = img_form.layers[0].copy()
    
    #active_layer.add_alpha(img_application)
    


register(
    "python-fu-rawble_products",
    "This will produce Product image for rawble.com",
    "LONG DESCRIPTION",
    "Jackson Bates", "Jackson Bates", "2015",
    "rawble_products",
    "*", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        
        ## Add New Application Name at the end of the list
        (PF_OPTION, "option_application", "Select Application", 0,
            ("Eye Contour", "Hair care", "Men Care", "Perfumes & Fragrances", "Skin Care","Sun Care","Toiletries","Baby Food/Infant Food","Bakery","Beverages","Cereals/Breakfast Foods","Confectionery","Dairy Products","Desserts and Ice Cream","Fats, Oils & Sweet Spreads","Fruits & Vegetables","Functional Food and Nutrition","Grain Mill Products","Meals, Convenience Foods, Ready Meals","Meat, Poultry, Fish & Egg Products","Sauces, Seasonings, Condiments & Soups","Snack Foods")
         ),
        ## Add New Form Name at the end of the list
         (PF_OPTION, "option_form", "Select Form", 0,
            ("Liquid","Powder","Oil")
         ),
        
        (PF_FILE, "file_var", "Input image", ""),
        # PF_SLIDER, SPINNER have an extra tuple (min, max, step)
        # PF_RADIO has an extra tuples within a tuple:
        # eg. (("radio_label", "radio_value), ...) for as many radio buttons
        # PF_OPTION has an extra tuple containing options in drop-down list
        # eg. ("opt1", "opt2", ...) for as many options
        # see ui_examples_1.py and ui_examples_2.py for live examples
    ],
    [],
    rawble_products, menu="<Image>/File")  # second item is menu location

main()
