#!/usr/bin/env python
# coding: utf-8

# # Análises Preditivas (Predictive Analysis)

# # Carregar dados das ações (Load Stock Data)

# In[4]:


get_ipython().system('pip install yfinance')


# In[3]:


import yfinance as yf


# In[8]:


ticker = input("Digite o código da ação: ")
dados = yf.Ticker(ticker).history("2y")
dados.head()


# In[13]:


dados["Close"].plot()


# # Tratamento de Dados (Data Treatment)

# In[15]:


dados.head()


# In[35]:


treinamento = dados.reset_index()
treinamento= treinamento[["Date", "Close"]]
treinamento["Date"] = treinamento["Date"].dt.tz_localize(None)
treinamento.columns = ['ds', 'y']
treinamento


# # Treinando o modelo de Machine Learning (Machine Learning Model Training)

# In[38]:


get_ipython().system('pip install prophet')


# In[39]:


from prophet import Prophet
from prophet.plot import plot_plotly


# In[40]:


# criar o modelo de Inteligência Artificial (Creating the AI model)
modelo = Prophet()


# In[41]:


#treinar o modelo (model training)
modelo.fit(treinamentoamento)


# # Realizando Previsões (Making predictions)

# In[49]:


periodo = modelo.make_future_dataframe(90)


# In[50]:


periodo.tail()


# In[53]:


previsoes = modelo.predict(periodo)


# In[55]:


previsoes


# # Gerar visualização gráfica (Generating Plot visualization)

# In[60]:


grafico = plot_plotly(modelo, previsoes)
grafico


# In[ ]:


grafico.write_html("Grafico_Previsoes.html")

