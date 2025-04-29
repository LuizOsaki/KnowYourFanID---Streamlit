import streamlit as st
import os
from utils.document_validator import validate_document
from utils.profile_analyzer import analyze_profile

st.set_page_config(page_title="KnowYourFan - eSports ID", layout="centered")

# Cria diretório de uploads se não existir
if not os.path.exists("uploads"):
    os.makedirs("uploads")

st.title("Know Your Fan - eSports Collector")

# 1. Formulário de Cadastro
st.header("Cadastro")
with st.form(key="registration_form"):
    name = st.text_input("Nome Completo")
    cpf = st.text_input("CPF")
    address = st.text_input("Endereço")
    email = st.text_input("E-mail")
    interests = st.text_area("Interesses em eSports (times, jogos, eventos)")
    events = st.text_area("Eventos de eSports que participou no último ano")
    purchases = st.text_area("Compras relacionadas a eSports no último ano")
    
    submit_button = st.form_submit_button(label="Enviar Cadastro")

if submit_button:
    st.success("Cadastro enviado com sucesso!")
    st.session_state['user_data'] = {
        "name": name,
        "cpf": cpf,
        "address": address,
        "email": email,
        "interests": interests,
        "events": events,
        "purchases": purchases
    }

# 2. Upload de Documento
st.header("Upload de Documento de Identidade")
uploaded_file = st.file_uploader("Envie seu RG ou CPF (imagem ou PDF)", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Arquivo enviado com sucesso!")

    validation_result = validate_document(file_path)
    st.write("Resultado da validação:")
    st.json(validation_result)

# 3. Links de Perfis
st.header("Links de Perfis em sites de eSports")
profile_link = st.text_input("Cole aqui o link do seu perfil (ex: FaceIt, Steam, HLTV)")

if st.button("Validar Perfil"):
    if profile_link:
        analysis_result = analyze_profile(profile_link)
        st.write("Análise do perfil:")
        st.json(analysis_result)
    else:
        st.error("Por favor, insira um link para validar.")

# 4. Dashboard
st.header("Resumo do Cadastro")
if 'user_data' in st.session_state:
    st.json(st.session_state['user_data'])
else:
    st.info("Preencha o cadastro para visualizar o resumo.")
