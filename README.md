Aplicação Python integrada com a biblioteca Dash(react) que monta gráficos, a partir de um CSV, com a finalidade de analisar dados sobre mortalidade infantil e neonatal no estado do Acre

# Instalação:
```bash
# Execute os seguintes comandos no seu terminal:

python -m pip install --upgrade pip
pip3 install graphs
pip3 install pandas
pip3 install dash
pip3 install numpy

```

# Acessar a aplicação:
Para acessar a aplicação basta executar o arquivo golden_project.py em seu terminal .
```bash
python golden_project.py
```

Acesse a aplicação através do link [localhost:8050](http://localhost:8050)

# Como navegar pela aplicação?
### ***Existem 3 abas para navegação e exploração de gráficos .***
### **1. Na primeira aba, para alterar a visualização do gráfico basta apenas alterar as informações dos ComboBox ou do slider de ano !**

![alt text](https://i.imgur.com/8qjBBgi.png)

### **2. Na segunda aba é possível apenas alterar o slider.**

![alt text](https://i.imgur.com/HZCF6ay.png)

### **2.1 É Possível também alterar o angulo de visualização do gráfico 3D, basta apenas clicar segurar e movimentar o mouse !**

![alt text](https://media.giphy.com/media/gIweUJnk9KxvsV0Tv4/giphy.gif)

### **3. Na terceira aba também é possível apenas alterar o slider.**

![alt text](https://i.imgur.com/FFdf7Wm.png)


# **O que significam os gráficos?**

## 1. O primeiro gráfico :
- Estabelece uma relação entre a cor da mãe da criança, o lugar onde o parto foi realizado e mortes neonatal por ano .
```bash
# Observação:

O gráfico mostra os dados do primeiro ano disponível até o ano marcado pelo slider e não somente os dados do ano marcado .

```
- ***Com essa visualização podemos concluir que a maiora das recorrências de morte neonatal ocorre entre as mães pardas que fizeram o parto no hospital .***


## 2. O segundo gráfico :
- Estabelece uma relação entre mortes neonatal (***Eixo X***)  por faixa de peso em *gramas* (***Eixo Y***) e média de dias que vividos por faixa de peso (***Eixo Z***) .
- Também oferece a porcentagem de meninos e meninas que morreram para os anos marcados .
```bash
# Observação

O gráfico 3D é interativo e você pode alterar o angulo da visão apenas segura o mouse clicado em cima do gráfico e o arrastando para os lados ou pra cima .
```
- ***Com essa visualização é possível interpretar que as crianças na faixa de peso entre 1950g->2410g possuem maior expectativa de vida .***
- ***Com essa informação pode-se concluir que se a criança estiver entre essa faixa de peso o médico tem mais tempo para agir e tomar atitudes cruciais para que a mesma não venha a óbito .***
- ***Também é possível observar que meninos representam a maior quantidade dos óbitos. Isso pode ser um indicador para o médico tomar mais cuidado com os meninos .***
## 3. O terceiro gráfico :
- Estabelece uma relação entre a quantidade de mortes neonatal por faixa de idade das mães e por tipo de parto realizado.
```bash
# Observação
A legenda das faixas etárias das mães são (Eixo X) :
1 - Mães de 8->14 anos ,
2 - '' 15->19 anos ,
3 - '' 20->24 anos ,
4 - '' 25->29 anos ,
5 - '' 30->34 anos ,
6 - '' 35->39 anos ,
7 - '' 40->44 anos .

Cor verde: Parto cesariano .
Cor amarela: Parto normal .
```
* ***Com esta visualização podemos observar que mães que realizam cesária possuem menos chance de que seus filhos venham a óbito !***
- ***Podemos observar também que as mães a cima de 30 anos optam mais pela cesária que pelo parto normal, isso indica um fator de prevenção importante !***

### Implementações futuras
1. Design de interface .
2. Otimização de código .



### ***Obrigado pela atenção!***

*Qualquer dúvida pode me contactar .*
