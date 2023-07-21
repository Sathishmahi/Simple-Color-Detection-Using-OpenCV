import streamlit as st
from detector.detect import detect_color 
import os
import cv2
import uuid

# rgb_to_hex=lambda rgb:"#"+"".join([hex(c)[2:] for c in rgb])

imgs_dir_name="images"
raw_img_path=os.path.join(imgs_dir_name,f"input.png")
gray_img_path=os.path.join(imgs_dir_name,f"gray.png")

final_img_path=os.path.join(imgs_dir_name,f"final.png")
os.makedirs(imgs_dir_name,exist_ok=True)
def rgb_to_hex(rgb):
    r, g, b = [max(0, min(255, x)) for x in rgb]
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_color
def hex_to_rgb(hex_val:str):
    hex_val=hex_val.lstrip("#")
    return [ int(hex_val[i:i+2],16) for i in range(0,len(hex_val),2)]

def main():
    img=st.file_uploader(label="upload the file for color prediction",type=["png","jpg","jpeg"],accept_multiple_files=False)
    if img:
        with open(raw_img_path,"wb") as img_file:
            img_file.write(img.getbuffer())
        # cv2.imwrite("demo.png", img)
        r = st.sidebar.slider("Red", 0, 255, 0)
        g = st.sidebar.slider("Green", 0, 255, 0)
        b = st.sidebar.slider("Blue", 0, 255, 0)
        hex_color=rgb_to_hex([r,g,b])
        color = st.color_picker('Pick A Color', hex_color)
        st.write(f'The current selected color hexa decimal value is {color} and RGB value is {hex_to_rgb(color)}')
        isclick=st.button(label="Detect Color")
        if isclick:
            detect_color(raw_img_path,[r,g,b],gray_img_path,final_img_path)
            st.title("Detectd Image")
            st.image(final_img_path, caption="Predicted Image", use_column_width=True)



if __name__=="__main__":
    main()