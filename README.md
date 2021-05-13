# PCA - MEMORY KIDS

### Autores: 

- Daniele Lemos de Mello Andrade
- Gabriel da Silva Mourão
- Robson Tadeu Da Cruz Santos
- João Victor da Conceição Menezes
- Vinicius Mattos do Nascimento

### Objetivo

- Criação do sistema “Memory Kids”
- Jogo para crianças com deficiência visual, visando auxiliar na concentração e capacidade de memorização;
- Requisitos do sistema (funcionais e não funcionais):
  - Deverá iniciar de forma aleatória registrando para as teclas de 0 a 9 sons, 5 sons diferentes;
  - Deverá capturar as teclas pressionadas pela criança, verificando se a combinação está correta;
    - Caso a combinação estiver correta, deverá ser emitido som de acerto. Caso contrário deverá ser emitido som de erro;
- Deverá armazenar em memória as combinações já acertadas;
- Ao completar o jogo deverá ser emitido som de vitória;
- Para que os pais possam auxiliar as crianças, também será exibido em tela os resultados;

### Proposta

- Implementação do sistema em terminal;
- Utilizado Python puro, sem frameworks;
- Utilizado também os pacotes:
  - Pynput: Capturar os eventos de pressionar teclas;
  - Rich: Fazer interface amigável no terminal;
  - Simpleaudio: Reproduzir os áudios;

### Implementação

- [Vídeo da Apresentação](https://www.youtube.com/watch?v=aXFTAeQLuiw)