# 🎬 Catálogo Virtual de Filmes

Um app simples e elegante feito com **Streamlit**, que permite buscar filmes usando a API gratuita da **OMDb (Open Movie Database)**. Os resultados são exibidos como cartões com imagem, título, ano e tipo, e organizados em uma prateleira de 10 filmes por página.

---

## 🚀 Funcionalidades

- 🔎 Pesquisa de filmes por título
- 📄 Paginação com botões “Anterior” e “Próxima”
- 🎥 Exibição de cartazes, títulos, ano e tipo
- 📊 Contador de total de filmes encontrados

---

## 🔧 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/AlbuquerquexD/catalogo-virtual.git
   cd catalogo-virtual

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   source venv/bin/activate  # macOS/Linux

3. pip install -r requirements.txt

4. Obtenha uma chave da API da OMDb:

   * Acesse: https://www.omdbapi.com/apikey.aspx

   * Faça um cadastro gratuito

   * Você receberá uma chave de API por e-mail

5. Subistitua na (linha 23)
   ```bash
      api_key = st.secrets["OMDB_API_KEY"] 
      por: api_key = chave da API da OMDb (que foi criada)

6. Execute o projeto localmente com Streamlit: 
   ```bash
      streamlit run app.py

👨‍💻 Autor

Desenvolvido por Antony Albuquerque — para fins de estudo, prática com APIs públicas e projetos com Streamlit.
