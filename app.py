import streamlit as st
import requests

st.set_page_config(layout="wide")

# css nas imagens
st.markdown("""
    <style>
    .zoom-img {
        border-radius: 8px;
        height: 240px;
        width: 100%;
        object-fit: cover;
        transition: transform 0.3s ease;
        cursor: zoom-in;
    }
    .zoom-img:hover {
        transform: scale(1.2);
    }
    </style>
""", unsafe_allow_html=True)

api_key = st.secrets["OMDB_API_KEY"]

# Busca de filmes
def buscar_filmes(SEARCH_TERM, page=1):
    url = f'http://www.omdbapi.com/?apikey={api_key}&s={SEARCH_TERM}&page={page}'
    response = requests.get(url)
    data = response.json()
    filmes = data.get('Search', [])
    total = int(data.get('totalResults', 0)) if 'totalResults' in data else 0
    return filmes, total

st.title("🎬 Catálogo Virtual")

if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = 1

if "ultimo_titulo" not in st.session_state:
    st.session_state.ultimo_titulo = ""

# Input da pesquisa
title = st.text_input("Pesquisar :")

# Detecta mudança de título e reseta a página
if title.strip() and title != st.session_state.ultimo_titulo:
    st.session_state.pagina_atual = 1
    st.session_state.ultimo_titulo = title

st.markdown("<br>",unsafe_allow_html=True)

# Verifica se foi digitado algo
if title.strip():
    try:
        filmes, total = buscar_filmes(title, st.session_state.pagina_atual)
        total_paginas = (total + 9) // 10
        total_filmes = total

        st.write(f"🔍 Resultados para: **{title}**")
        st.write(f" 🎯 Total encontrados: **{total_filmes}**")

        # Mostra os 10 cards
        cols = st.columns(10)
        for idx, filme in enumerate(filmes):
            with cols[idx]:
                st.markdown('<div class="card">', unsafe_allow_html=True)

                poster = filme['Poster'] if filme['Poster'] != 'N/A' else "https://via.placeholder.com/150x220?text=Sem+Imagem"
                st.markdown(f'<img src="{poster}" class="zoom-img">', unsafe_allow_html=True)
                st.markdown(f"<strong>{filme['Title']}</strong>", unsafe_allow_html=True)
                st.caption(f"📅 {filme['Year']} | 🎞️ {filme['Type']}")

                st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erro na busca: {e}")
        total_paginas = 1

    # Indicador de página
    st.markdown(f"""
    <div style='text-align: center; font-size: 18px; font-weight: 600; padding-top: 10px; color: #f0f0f0;'>
        📄 Página <span>{st.session_state.pagina_atual}</span> de <span>{total_paginas}</span>
    </div>
    """, unsafe_allow_html=True)

    # Botões
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅️ Anterior") and st.session_state.pagina_atual > 1:
            st.session_state.pagina_atual -= 1
    with col3:
        if st.button("Próxima ➡️") and st.session_state.pagina_atual < total_paginas:
            st.session_state.pagina_atual += 1

else:
    st.info("💡 Digite um nome de filme para começar a busca.")


