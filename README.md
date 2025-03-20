# Prova Prática - Seleção de Estágio na CODIN (PGE)

## Descrição do Projeto
Esta prova prática tem como objetivo avaliar habilidades em modelagem de banco de dados, análise de dados e documentação.

## Entregáveis

### 1. Modelagem do Banco de Dados
Foi desenvolvido um modelo de banco de dados relacional que permite:
- Identificar e acompanhar processos jurídicos
- Controlar prazos importantes
- Armazenar documentos essenciais
- Gerenciar procuradores e clientes
- Permitir a redistribuição de processos entre procuradores

#### Tecnologias Utilizadas
- **Banco de Dados:** MySQL
- **Linguagem SQL:** Para criação das tabelas e restrições
- **Ferramenta de Modelagem:** MySQL Workbench
- **Ferramenta de Inserção de Dados via SQL:** MySQL Workbench
- **Ambiente de Desenvolvimento Apache/MySQL:** XAMPP
- **Ferramenta de Inserção de Dados via Código:** VSCode
- **Linguagem de Programação Python:** Para estabelecer conexão com o banco de dados, inserir dados e fazer consultas via código.
- **Bibliotecas Python:** MySQL Connector

#### Como Executar
1. Instale o XAMPP em sua máquina e ative o Apache e o MySQL.
2. Instale o MySQL em sua máquina.
3. Execute o script SQL fornecido no repositório no caminho `"Modelagem_Dados\Esquema_SQL"` para criar o banco de dados e tabelas.
4. (Opcional) Popular o banco com dados fictícios e executar consultas utilizando os scripts adicionais encontrados nos caminhos `Modelagem_Dados\Extra_PopularDB\Insercao_SQL` e `Modelagem_Dados\Extra_PopularDB\Insercao_Python` para execução em SQL e Python respectivamente.

---

### 2. Análise de Dados - Conjunto Iris
Foi realizada uma análise exploratória do conjunto de dados Iris utilizando Python. A análise seguiu as etapas descritas abaixo:

#### Etapas da Análise
- **Verificação e limpeza de dados**
- **Cálculo de medidas estatísticas**
- **Geração de gráficos de distribuição e correlação**
- **Identificação das variáveis que impactam na classificação das espécies**
- **(Extra) Construção de um modelo preditivo para classificação das espécies**

<br>

#### Verificação e Limpeza de Dados
Comecei fazendo definição das colunas (segundo o arquivo iris.names) inserindo os nomes das colunas do dataset. Em seguida, carreguei o dataset, verifiquei se existiam valores ausentes ou duplicados. Nessa verificação, percebi 3 dados duplicados, mas ao pesquisar a fundo sobre esse dataset, cheguei a decisão que não estavam duplicados por conta de algum erro visto que o iris dataset é uma base de dados com amostras de espécies e pode acontecer de ter amostras semelhantes. Também verifiquei os tipos de dados, traduzi o nome das colunas e retirei o termo “Iris-” antes dos nomes das espécies, pois não era necessário.

<br>

#### Cálculo de Medidas Estatísticas
1. Medidas de Tendências Central:  
   Usei o cálculo da média, mediana e moda. Com isso, verifiquei que as flores do conjunto possuem o comprimento das sépalas maior do que o comprimento de suas pétalas. Também é possível notar que a distribuição de valores da coluna “Comprimento_Petala” não são equilibradas, contendo valores extremos puxando sua média para baixo.

2. Quais são as espécies (classes) e a quantidade de observações de cada uma delas:  
   Identifiquei que os tipos de espécies no conjunto são: Setosa, Versicolor e Virginica. Cada uma possui 50 amostras no dataset.
 
3. Medidas de Tendências Central por Espécie:  
   Agrupei a coluna de espécie e calculei a média, mediana e desvio padrão. É possível notar que a espécie virginica tem as maiores pétalas e sépalas e a espécie setosa tem as menores. A espécie setosa possui muitas amostras parecidas no conjunto, enquanto a virginica possui amostras mais diversificadas.

<br>

#### Gráficos de Distribuição e Correlação
**Distribuição das Variáveis:**
- Comprimento_Sepala: É notável que existem mais quantidades de amostras com valores entre 4,5 e 6,5 cm. A distribuição desses dados possui vários tipos pelo fato de ter três espécies nesse conjunto e cada uma tem um padrão distinto de comprimento da sépala.
- Largura_Sepala: Nesta distribuição, os valores estão mais concentrados entre 2,5 e 3,5 cm. Existe um pico concentrado próximo de 3.0 cm, indicando que essa é a largura mais comum entre as flores do dataset.
- Comprimento_Petala: A distribuição tem a presença de dois grupos distintos. Um grande pico perto de 1.5 cm, possivelmente correspondente à espécie de menor porte. Outro grupo entre 4.0 cm e 6.0 cm, que pode corresponder a outras espécies com pétalas mais longas.
- Largura_Petala: A distribuição também possui dois grupos distintos, com um grupo grande de valores próximos de 0.2 cm e outro entre 1.2 cm e 2.0 cm.

<br>

**Distribuição por Espécie:** 

Comprimento_Sepala:
- A setosa tem sépalas mais curtas, variando entre 4.5 e 5.8 cm.
- A versicolor apresenta sépalas maiores que a setosa, mas menores que a virginica.
- A virginica tem as sépalas mais longas, variando entre 5.0 e 8.0 cm.
  
Largura_Sepala:
- A setosa tem as sépalas mais largas, variando entre 2.3 e 4.4 cm.
- A versicolor tem sépalas com largura menor e menos dispersão.
- A virginica tem uma distribuição intermediária, mas com um outlier abaixo de 2.5 cm e um acima de 3,5 cm.
  
Comprimento_Petala:
- A setosa tem pétalas curtas entre 1.0 e 1.9 cm e sem sobreposição com as outras espécies.
- A versicolor tem pétalas de comprimento intermediário, entre 3.0 e 5.3 cm.
- A virginica tem pétalas longas, entre 4.5 e 7.0 cm.
  
Largura_Petala:
- A setosa tem pétalas muito estreitas entre 0.1 e 0.6 cm e apresenta alguns outliers.
- A versicolor tem pétalas mais largas entre 1.0 e 1.8 cm.
- A virginica tem as pétalas mais largas entre 1.4 e 2.5 cm.

<br>


**Correlação entre Variáveis:** 

Relações: 

Comprimento_Sepala vs. Comprimento_Petala (0.87):
- Existe uma forte correlação positiva, indicando que flores com sépalas mais longas tendem a ter pétalas mais longas.  
<br>
  
Comprimento_Sepala vs. Largura_Sepala (-0.11):
- Há uma correlação negativa fraca, indicando que não há uma relação forte entre essas duas medidas.  
<br>
  
Largura_Sepala vs. Comprimento_Petala (-0.42):
- Existe uma correlação negativa moderada, indicando que quanto maior a largura da sépala, menor tende a ser o comprimento da pétala.  
<br>
  
Comprimento_Petala vs. Largura_Petala (0.96):
- Há uma correlação muito forte e positiva, indicando que pétalas mais longas também tendem a ser mais largas.  
<br>



#### Identificação das Variáveis que Impactam na Classificação das Espécies
O comprimento e a largura da pétala são as melhores variáveis para diferenciar as espécies:
- Setosa tem pétalas curtas e estreitas.
- Virginica tem pétalas longas e largas.
- Versicolor é intermediária.

<br>

#### (Extra) Construção de um Modelo Preditivo

<br>

Etapas: 
1. Divida o conjunto de dados em conjunto de treinamento e conjunto de teste (EXTRA): <br>
   - Usando a biblioteca Sklearn, separei as variáveis preditoras (x) e a variável alvo (y) e fiz a divisão do conjunto de dados entre treino (80%) e teste (20%).

2. Selecione um algoritmo de aprendizado supervisionado e construa um modelo (EXTRA):
	  - Importei o modelo DecisionTreeClassifier (Árvore de Decisão para classificação) e treinei ele com o conjunto de dados de treino que separei na etapa anterior.
     
3. Teste seu modelo e gere as métricas de acurácia, precisão e recall para os resultados (EXTRA): 	
	  - Testei o modelo com os dados de teste e gerei um relatório da precisão, acurácia e recall. O modelo apresentou uma acurácia de 1.00 indicando que classificou corretamente todas as amostras do conjunto 
     de teste. Também apresentou uma precisão de 1.00 e um recall de 1.00 significando que não houve falsos positivos e nem falsos negativos.
     
4. Aplique a redução de dimensionalidade e refaça os passos de construção do modelo e testes (EXTRA):
   - Apliquei técnicas de PCA para reduzir para apenas dois componentes principais e transformei em um dataframe. Em seguida refiz as etapas anteriores, separei os dados em treinos e testes, importei um 
     modelo de aprendizado, treinei e testei o modelo. Gerei um novo relatório da precisão, acurácia e recall e obtive os mesmos resultados do relatório anterior.


#### Tecnologias Utilizadas
- **Linguagem:** Python 3.12.5
- **Bibliotecas:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, RegEx
- **Dataset:** Iris-Dataset

#### Como Executar
1. Instale as bibliotecas necessárias:
   ```sh
   pip install pandas numpy matplotlib seaborn scikit-learn re
   ```
2. Execute o script Python fornecido para reproduzir a análise.
3. Os gráficos gerados serão salvos automaticamente na pasta `Graficos`.

---

### 3. Documentação
Foi criado um **Diagrama Entidade-Relacionamento (DER)** representando o modelo de banco de dados. O arquivo pode ser encontrado na pasta `Documentacao` do repositório.

#### Tecnologias Utilizadas
- **Ferramenta de Modelagem:** MySQL Workbench

#### Como Visualizar o DER
1. Acesse a pasta `Documentacao`.
2. Abra o arquivo no MySQL Workbench.

