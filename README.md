# calculadora 🧮

É uma calculadora front-end em python, usando a biblioteca Tkinter. Bem simples de se fazer e divertido de usar 🤩

Este projeto foi desenvolvido em um ambiente Ubuntu Linux. Pode funcionar em distribuições linux baseada em Debian.

## Como usar

- Ative o Docker e faça um build da imagem do Dockerfile

  `docker build -t calculadora:0.1 .`

- depois dar um run pra criar o container.
  `docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --rm calculadora:0.1`

E voilà ✨ Já vai estar pronta pra uso! 😃

![Captura de tela de 2023-08-10 14-20-44](https://github.com/Julioc10/calculadora/assets/69183396/301d68ff-28dc-4db8-abea-1955de4272a3)
