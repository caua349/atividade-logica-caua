import streamlit as st

st.title("Analisador de Notas")

aprovadas = 0
reprovadas = 0

st.write("Digite 5 notas:")

for i in range(5):
    nota = st.number_input(
        f"Nota {i + 1}",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    if nota >= 6:
        aprovadas += 1
    else:
        reprovadas += 1

if st.button("Ver resultado"):
    st.write("Quantidade de aprovados:", aprovadas)
    st.write("Quantidade de reprovados:", reprovadas)