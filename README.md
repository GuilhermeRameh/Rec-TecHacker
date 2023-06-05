# Rec-TecHacker

## Proposta:
Automaticamente determinar se um site pertence à uma cloud pública como AWS, Azure, Oracle, ou se é hosteado em uma nuvem privada.

## Descrição da Ferramenta:
A ferramenta usa da biblioteca `whois` e `pandas` para python. Whois faz scans de sites, e consegue nos retornar os DNSs associados àquele site, e portanto, conhecendo o padrão de DNS dos fornecedores principais, conseguimos determinar qual o fornecedor da nuvem dado apenas o site. 

## Entrada vs Saida:
Como entrada, selecionei "na mão" 48 universidades públicas, e seus sites (fonte: wikipedia), e mais dois testes para a Netflix e o site do VsCode, que ambos são hosteados em infraestrutura que estamos checando nesse projeto, portanto era esperado conseguirmos essas informações.