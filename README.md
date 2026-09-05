# Aprendizado Inicial

Este repositório registra minha evolução nos estudos de programação e cibersegurança, desde os primeiros conceitos em Python até o desenvolvimento de um projeto prático de Mini SOC.

Aqui serão documentados exercícios, testes, anotações, pequenos projetos e melhorias realizadas durante o processo de aprendizado. O objetivo é acompanhar meu progresso, consolidar conhecimentos e aplicar, na prática, conceitos de automação, redes, monitoramento e segurança da informação.

Os exercícios antigos continuam aqui como registro real dos primeiros passos, inclusive versões parecidas de uma mesma ideia. A organização por assunto facilita a consulta sem apagar esse caminho. Os novos exercícios são propostas de prática para continuar os estudos; sua inclusão não significa que todos os assuntos já foram dominados.

## Conteúdo e ordem de estudo

| Pasta | O que praticar | Arquivos Python |
| --- | --- | --- |
| [01-Fundamentos](01-Fundamentos/README.md) | Entrada, saída, variáveis, contas e conversões | 9 |
| [02-Desafios-Basicos](02-Desafios-Basicos/README.md) | Desafios históricos de strings e cálculos | 8 |
| [03-Condicionais](03-Condicionais/README.md) | Decisões com `if`, `elif` e `else` | 5 |
| [04-Repeticoes](04-Repeticoes/README.md) | Contadores, acumuladores, `for` e `while` | 6 |
| [05-Strings](05-Strings/README.md) | Análise e busca em textos | 4 |
| [06-Listas](06-Listas/README.md) | Guardar e percorrer vários valores | 4 |
| [07-Funcoes](07-Funcoes/README.md) | Parâmetros, retorno, escopo e validação simples | 5 |
| [08-Primeiros-Projetos](08-Primeiros-Projetos/README.md) | Calculadora, cadastro em memória e análise textual de IPv4 | 3 |

Comece pelos fundamentos e siga a numeração das pastas. Cada área tem um README com uma sequência sugerida. Leia os comentários, execute um arquivo por vez e experimente mudar os valores para entender o resultado. As listas e funções aparecem depois da prática com decisões e repetições; os projetos reúnem esses conceitos.

## Como executar

É necessário ter Python 3 instalado. Não há dependências externas para instalar.

No terminal, a partir da raiz do repositório:

```bash
python "01-Fundamentos/Obter-dados-user.py"
python "03-Condicionais/par-ou-impar.py"
```

Execute um comando de cada vez e responda às perguntas no terminal. Dependendo da instalação, o comando pode ser `python3` ou, no Windows, `py`.

Nos exercícios numéricos, digite o tipo de valor pedido e use ponto para casas decimais, salvo quando o próprio exercício já aceita vírgula. Os primeiros exemplos pressupõem entradas válidas: texto no lugar de número pode gerar `ValueError`. A repetição da pergunta após uma entrada inválida é praticada em `07-Funcoes/validacao-inteiro.py`. Nos menus, a opção `0` encerra o programa; `Ctrl+C` também permite interromper a execução.

## O histórico dos exercícios

Os 15 arquivos Python que estavam em `Exercicios/` foram movidos com `git mv`, conservando seus nomes. A licença MIT também foi mantida. Os ajustes nos códigos antigos se limitam a comentários/rótulos factuais e à linha que demonstrava um erro de escopo; a formatação e as soluções simples foram preservadas.

- O **Desafio 02 foi recuperado**, a partir de uma versão anterior que calculava dobro, triplo e raiz quadrada. Sua origem e a correção da raiz estão documentadas em [Desafios básicos](02-Desafios-Basicos/README.md).
- O **Desafio 05** continua com esse nome em [Repetições](04-Repeticoes/Desafio-5.py), pois já usa `for`.
- Apesar do nome, **ola-mundo.py** é um exemplo de funções e escopo, agora em [Funções](07-Funcoes/ola-mundo.py). A linha que causa `NameError` está comentada e pode ser descomentada para observar o erro.
- Esta expansão acrescenta **28 exercícios novos**, além do Desafio 02 recuperado: são **44 arquivos Python** ao todo.

Os valores de câmbio e tarifas usados nos exercícios são exemplos fixos, sem consulta a preços atuais. Use nomes fictícios nas práticas. O cadastro guarda dados apenas em memória, e o analisador de IPv4 verifica somente o texto digitado, sem consultas ou ações de rede. Os estudos futuros de cibersegurança seguirão essa proposta educacional.

## Verificar a sintaxe

Para compilar todos os exercícios sem executar suas perguntas, rode na raiz:

```bash
python -m compileall -q 01-Fundamentos 02-Desafios-Basicos 03-Condicionais 04-Repeticoes 05-Strings 06-Listas 07-Funcoes 08-Primeiros-Projetos
```

Esse comando pode criar pastas `__pycache__`, já ignoradas pelo Git. A compilação verifica a sintaxe; ela não substitui a prática com entradas e a conferência dos resultados.

## Licença

[MIT](LICENSE), conforme a licença original do repositório.
