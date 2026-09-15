# A/B Testing

Foi conduzida uma campanha de marketing com usuários de um site com objetivo de aumentar as vendas de um produto. E para isso, foi desenvolvido um anúncio especificamente com esse objetivo.

Para verificar se a campanha teve êxito em seu objetivo, se o anúncio de fato contribuiu para converter mais vendas, usuários do site foram selecionados aleatoriamente e separados em dois grupos: um grupo que viu o anúncio especificamente desenhado (AD) e outro grupo de controle, ao qual foi mostrado um anúncio genérico (PSA).

Nosso objetivo aqui é **verificar se a taxa de conversão do grupo AD é maior que o grupo controle (PSA) e se a diferença observada é estatisticamente significativa**.

A análise foi feita sobre o dataset [Marketing A/B Testing](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing), que se trata de um teste A/B: _"um experimento randomizado em que diferentes versões de variável (um anúncio ou funcionalidades de um sistema) são apresentadas a diferentes grupos de usuários ao mesmo tempo. O objetivo é avaliar o peso que a variável tem sobre o resultado final"_.

## Resultados

- Foram analisados pouco mais de 588.000 usuários divididos em dois grupos: um exposto ao anúncio especificamente desenvolvido para a venda de um produto (AD) e outro utilizado como controle, que foi exposto a um anúncio genérico (PSA). 
- Foi observado que usuários expostos ao anúncio específico (AD) possuem uma taxa de conversão 43% maior que os usuários do grupo de controle (PSA): foram p_AD = 2,55% contra p_PSA = 1,79%
  - A partir de testes, verificou-se que essa diferença nas taxas de conversão é estatisticamente significativa, ou seja, não se trata de ruído estatístico.
- Observamos que a taxa de conversão cresce junto com a quantidade de anúncios observados pelos usuários, chegando a quase 17% quando os usuários são expostos a mais de 100 anúncios. 
- Também foi possível determinar que os dias da semana com maiores taxa de conversão são Segunda e Terça-feira, e a janela dos melhores horários para apresentar anúncios vai de 14h-21h.

