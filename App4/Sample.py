import streamlit as st
import bcrypt
import database as db
import py_avataaars as pa
from PIL import Image
import base64
from random import randrange

# Get usernames and hashed passwords from the database
users = db.fetch_all_users()
usernames = [user["key"] for user in users]
hashed_passwords = [user["password"] for user in users]

# Define the login function
def login():
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in usernames:
            user_index = usernames.index(username)
            hashed_password = hashed_passwords[user_index].encode("utf-8")
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
                st.sidebar.success("Logged in as {}".format(username))
                return True
            else:
                st.sidebar.error("Incorrect password")
        else:
            st.sidebar.error("Username not found")
    return False

# Avatar Gen
def avatar():
    col1, col2, col3 = st.columns(3)
    #st.sidebar.header('Character System')

    option_style = st.selectbox('Style', ('CIRCLE', 'TRANSPARENT'))

    list_skin_color = ['TANNED','YELLOW','BROWN','DARK_BROWN','BLACK']
    list_hair_color = ['BLACK','BLONDE','BROWN','PASTEL_PINK','RED','SILVER_GRAY']
    list_facial_hair_type = ['DEFAULT','BEARD_MEDIUM','BEARD_LIGHT','MOUSTACHE_FANCY']
    list_facial_hair_color = ['BLACK','BLONDE','BROWN','BROWN_DARK','RED']
    list_mouth_type = ['DEFAULT','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
    list_eye_type = ['DEFAULT','CLOSE','CRY','DIZZY','EYE_ROLL','HAPPY','HEARTS','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
    list_eyebrow_type = ['DEFAULT','DEFAULT_NATURAL','ANGRY','ANGRY_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','SAD_CONCERNED','SAD_CONCERNED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
    list_clothe_type = ['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
    list_clothe_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
    
    if st.button('Random Avatar'):
        index_skin_color = randrange(0, len(list_skin_color) )
        index_hair_color = randrange(0, len(list_hair_color) )
        index_facial_hair_type = randrange(0, len(list_facial_hair_type) )
        index_facial_hair_color= randrange(0, len(list_facial_hair_color) )
        index_mouth_type = randrange(0, len(list_mouth_type) )
        index_eye_type = randrange(0, len(list_eye_type) )
        index_eyebrow_type = randrange(0, len(list_eyebrow_type) )
        index_clothe_type = randrange(0, len(list_clothe_type) )
        index_clothe_color = randrange(0, len(list_clothe_color) )
    else:
        index_skin_color = 0
        index_top_type = 0
        index_hair_color = 0
        index_facial_hair_type = 0
        index_facial_hair_color = 0
        index_mouth_type = 0
        index_eye_type = 0
        index_eyebrow_type = 0
        index_accessories_type = 0
        index_clothe_type = 0
        index_clothe_color = 0
        index_clothe_graphic_type = 0
    avatar = pa.PyAvataaar(
        style=eval('pa.AvatarStyle.%s' % option_style),
        skin_color=eval('pa.SkinColor.%s' % option_skin_color),
        hair_color=eval('pa.HairColor.%s' % option_hair_color),
        facial_hair_type=eval('pa.FacialHairType.%s' % option_facial_hair_type),
        mouth_type=eval('pa.MouthType.%s' % option_mouth_type),
        eye_type=eval('pa.EyesType.%s' % option_eye_type),
        eyebrow_type=eval('pa.EyebrowType.%s' % option_eyebrow_type),
        nose_type=pa.NoseType.DEFAULT,
        clothe_type=eval('pa.ClotheType.%s' % option_clothe_type))

    def imagedownload(filename):
        image_file = open(filename, 'rb')
        b64 = base64.b64encode(image_file.read()).decode()  # strings to bytes
        href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename} File</a>'
        return href
    
    with col1:
        st.header('Character System')
        rendered_avatar = avatar.render_png_file('avatar.png')
        image = Image.open('avatar.png')
        st.image(image,width = 400,caption = 'User name')

    with col3:
        option_hair_color = st.selectbox('Hair Color', list_hair_color, index = index_hair_color)

        option_skin_color = st.selectbox('Skin color', list_skin_color, index = index_skin_color)

        option_eyebrow_type = st.selectbox('Eyebrow type', list_eyebrow_type, index = index_eyebrow_type)

        option_eye_type = st.selectbox('Eye type', list_eye_type, index = index_eye_type)

        option_mouth_type = st.selectbox('Mouth type', list_mouth_type, index = index_mouth_type)

        option_facial_hair_type = st.selectbox('Beard type', list_facial_hair_type, index = index_facial_hair_type)

        #option_facial_hair_color = st.selectbox('Facial hair color', list_facial_hair_color, index = index_facial_hair_color)

        option_clothe_type = st.selectbox('Clothe type', list_clothe_type, index = index_clothe_type)
    
# Test the login function
if login():
    st.title("Welcome to the app!")
    avatar()
    st.sidebar.button("Logout")
else:
    st.warning("Please log in.")
