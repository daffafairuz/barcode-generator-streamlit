import streamlit as st
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

st.set_page_config(page_title="Barcode Generator", page_icon="📦", layout="centered")

st.title("📦 Barcode Generator (EAN13)")

# Input nomor barcode
number = st.text_input("Masukkan 12 digit angka (EAN13):", max_chars=12)

if st.button("Generate Barcode"):
    if len(number) == 12 and number.isdigit():
        # Generate barcode
        my_code = EAN13(number, writer=ImageWriter())
        filename = my_code.save("generated_barcode")

        # Tampilkan barcode
        image = Image.open(f"{filename}")
        st.image(image, caption="Hasil Barcode", use_container_width=True)

        # Download barcode
        with open(f"{filename}", "rb") as file:
            btn = st.download_button(
                label="⬇️ Download Barcode",
                data=file,
                file_name="barcode.png",
                mime="image/png"
            )
    else:
        st.error("Nomor harus 12 digit angka (EAN13 otomatis menambahkan checksum).")
