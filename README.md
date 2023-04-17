# cardio-risk-ai
Este projeto é uma solução de previsão de riscos de doenças cardiovasculares, baseada em aprendizado de máquina. Utilizando uma arquitetura de microsserviços, o cardio-risk-ai é capaz de prever o risco de doenças cardiovasculares com alta precisão.


## Microsserviços
Os microsserviços são uma abordagem moderna e eficiente para escrever programas de software, onde as aplicações são desmembradas em componentes mínimos e independentes. No cardio-risk-ai, temos dois microsserviços: o training-microservice e o prediction-microservice.


### Microsserviço training-microservice
O training-microservice é responsável por treinar o modelo de machine learning com base em uma série de bibliotecas em Python, como Flask, Pandas, Pickle5, Scikit-learn e Setuptools. Além disso, o uso de Docker permite uma integração fácil e rápida em diferentes ambientes.


### Microsserviço prediction-microservice
O prediction-microservice é responsável por receber os dados de entrada e fazer previsões de risco de doenças cardiovasculares com base no modelo treinado. Ele também utiliza as mesmas bibliotecas em Python e Docker, garantindo uma consistência e qualidade na solução.


### Compartilhamento de código
O projeto conta com um pacote compartilhado chamado "shared", que possui funcionalidades de preparação de dados para o treinamento e previsão do modelo, pronto para ser utilizado nos microsserviços.


### Como Executar
Para executar o projeto cardio-risk-ai, siga os passos abaixo:

#### Pré-requisitos
- Linux ou Linux WSL2
- Visual Studio Code
- Docker
- docker-compose

### Passos
1. Abra o terminal no diretório raiz do projeto.
2. Execute o comando `chmod +x .docker/up.sh` para dar permissão de execução ao script.
3. Em seguida, execute o comando `.docker/up.sh` para iniciar os microsserviços do projeto.
4. Aguarde até que os serviços estejam em execução.
5. Após a conclusão, você poderá acessar os serviços de treinamento e previsão de risco de doenças cardiovasculares e testar usando a extensão REST Client do Visual Studio Code usando o arquivo `http.rest` em cada microsserviço.
6. Treine o modelo de machine learning no microsserviço training-microservice, copie o arquivo `model.pkl` (modelo treinado) da pasta training-microservice para a pasta prediction-microservice para fazer previsões de risco de doenças cardiovasculares com base no modelo treinado.

## Contribuições
Fique à vontade para contribuir com o projeto! Abra issues ou pull requests para reportar bugs, fazer melhorias ou adicionar novos recursos.

## Licença
Este projeto é licenciado sob a [MIT License](https://mit-license.org), o que significa que você pode utilizá-lo, copiá-lo, modificar e distribuí-lo livremente.
