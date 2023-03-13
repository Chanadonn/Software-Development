import streamlit as st
import py_avataaars as pa
import base64

st.markdown("Character System")

option_style = st.selectbox('Style', ('CIRCLE', 'TRANSPARENT'))

#st.write('You selected:', option)
avatar = pa.PyAvataaar(
    #style=eval('pa.AvatarStyle.%s' % option_style),
    style=pa.AvatarStyle.CIRCLE,
    skin_color=pa.SkinColor.LIGHT,
    hair_color=pa.HairColor.BROWN,
    facial_hair_type=pa.FacialHairType.DEFAULT,
    
    top_type=pa.TopType.SHORT_HAIR_SHORT_FLAT,
    mouth_type=pa.MouthType.SMILE,
    eye_type=pa.EyesType.DEFAULT,
    eyebrow_type=pa.EyebrowType.DEFAULT,
    nose_type=pa.NoseType.DEFAULT,
    accessories_type=pa.AccessoriesType.DEFAULT,
    clothe_type=pa.ClotheType.GRAPHIC_SHIRT,
    clothe_graphic_type=pa.ClotheGraphicType.BAT,
    facial_hair_color=pa.HairColor.BLACK,
)

def imagedownload(filename):
    image_file = open(filename, 'rb')
    b64 = base64.b64encode(image_file.read()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename} File</a>'
    return href