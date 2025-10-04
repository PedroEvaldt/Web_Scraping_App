import streamlit as st


def render_header():
    st.title("TITULO DO STREAMLIT")
    st.caption("Enter your ASIN to get product insights")


def render_inputs():
    asin = st.text_input("ASIN", placeholder="e.g. EXAMPLE DE ASIN")
    geo = st.text_input("zip/P")
    domain = st.selectbox("Domain", ["com", "ca..."])
    return asin.strip(), geo.strip(), domain


def main():
    st.set_page_config(page_title="Titulo da pagina", page_icon="ICONE")
    render_header()
    asin, geo, domain = render_inputs()

    if st.button("Scrape Product") and asin:
        with st.spinner("Scrapping product"):
            st.write("Scrape")
            # TODO: scrape product
        st.success("Product scraped successfully")


if __name__ == "__main__":
    main()
