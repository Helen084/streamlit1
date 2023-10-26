import math
import streamlit as st

st.set_page_config(page_title="EEMP 2023")
#st.date_input(value="today",format="DD/MM/YYYY")
st.title("Simulador da média escolar na Rede Estadual do RN")
st.write ("Autor: Heleno Carlos. e-mail: helenoneto524@educar.rn.gov.br")
st.write("Importante lembrar: Cuidado com as faltas, pois a frequência mínima para ser aprovado é de 75% .")
st.write("Vamos fazer uma simulação do  cálculo da média ?")


with st.container():

    bim1 = (st.number_input("Digite a sua nota do 1ª Bimestre",min_value=0.,max_value=10.,step=0.1, format="%.1f"))
    #st.write("Você obtve {:.1f} ponto(s) no 1 e para passar por média precisa:".format(bim1))
    diferenca = (24 - bim1)/3
    if bim1!=0:
        st.write("Meta de pontuação:  {:.1f} no 2ª, 3ª e 4ª bimestres.".format(diferenca))
    st.write("---")
    bim2 = (st.number_input("Digite a sua nota do 2ª Bimestre", min_value=0., max_value=10.,step=0.1, format="%.1f"))
    #st.write("Você obtve {:.1f} ponto(s) e para passar por média precisa:".format(bim2))
    diferenca2 = ((24 - bim1 - bim2)) / 2
    if bim2 !=0:
        st.write("Meta de pontuação:  {:.1f} no  3ª e 4ª bimestres.".format(diferenca2))
    st.write("---")
    bim3 = (st.number_input("Digite a sua nota do 3ª Bimestre", min_value=0., max_value=10.,step=0.1, format="%.1f"))
    #st.write("Você obtve {:.1f} ponto(s) e para passar por média precisa:".format(bim2))
    diferenca3 = ((24 - bim1 - bim2 - bim3))

    if bim3!=0:
        if diferenca3<=0:
            st.write("Você já está aprovado por média no 3ª Bimestre!")
        elif diferenca3>=10:
            st.write("Você já está na prova final de recuperação. \n A sua estratégia será obter a melhor nota possível no 4ª bimeste para precisar de um valor de pontos menor na prova final ")
        else:
            st.write("Meta de pontuação:  {:.1f} no  4ª bimestre.".format(diferenca3))
    st.write("---")

    bim4 = (st.number_input("Digite a sua nota do 4ª Bimestre", min_value=0., max_value=10.,step=0.1, format="%.1f"))
    #st.write("Você obtve {:.1f} ponto(s) e para passar por média precisa:".format(bim4))
    media_anual = (bim1 + bim2 + bim3 + bim4) / 4
    media_anual = math.ceil(media_anual * 10)
    media_anual = media_anual / 10


    if bim4 != 0:
        st.write("Sua média anual: {} ponto(s).".format(media_anual))

        if (media_anual)<2.5:
            st.write("Infelizmente você está reprovado sem direito a prova final de recuperação!")
            st.write("Motivo: Média anual <2.5")
        elif( media_anual>=2.5 and media_anual<6.0):
            st.write("Com essas notdas você vai precisar fazer a prova final de recuperação!")
            nota_pf = 15-(2*media_anual)
            st.write("Na prova final você precisará tirar {:.1f} pontos  para ser aprovado(a)!".format(nota_pf))
        else:
            st.write("Parabéns você está aprovado(a) por nota!")

st.write("Clique aqui --> [Sigeduc-RN](https://sigeduc.rn.gov.br/sigeduc/verTelaLogin.do)")





