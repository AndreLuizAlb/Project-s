<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Pintura da Floresta</title>
        <style>
            body {
                      font-family: 'Georgia', serif;
                            background-color: #000;
                                  display: flex;
                                        justify-content: center;
                                              align-items: center;
                                                    height: 100vh;
                                                          margin: 0;
                                                                flex-direction: column;
                                                                      text-align: center;
            }

                .container {
                          text-align: center;
                }

                    .frame-container {
                              display: flex;
                                    flex-direction: column;
                                          align-items: center;
                    }

                        .frame {
                                  border: 15px solid #8b5e3c;
                                        border-image: url('imagens/moldura.png') 30 round; /* Moldura personalizada */
                                              background-color: transparent; /*fundo transparente */
                                                    padding: 0; /*remove espaço interno */
                                                          display: inline-block;
                                                                box-shadow: 0 0 30px rgba(255, 255, 255, 0.2);
                                                                      margin-bottom: 25px;
                        }

                            .frame img {
                                      max-width: 500px;
                                            height: auto;
                                                  display: block;
                            }

                                button {
                                          padding: 14px 28px;
                                                font-size: 16px;
                                                      background-color: #6b5b95;
                                                            color: white;
                                                                  border: none;
                                                                        border-radius: 10px;
                                                                              cursor: pointer;
                                                                                    transition: background-color 0.3s;
                                }

                                    button:hover {
                                              background-color: #957dad;
                                    }

                                        .fade-out {
                                                  opacity: 0;
                                                        transition: opacity 1s ease-in-out;
                                                              pointer-events: none;
                                        }

                                            #forestImage {
                                                      transition: opacity 1s ease-in-out;
                                                            opacity: 1;
                                            }

                                                .image-fade {
                                                          opacity: 0;
                                                }
                                                  </style>
                                                  </head>
                                                  <body>
                                                    <div class="container">
                                                        <div class="frame-container">
                                                              <div class="frame">
                                                                      <img id="forestImage" src="imagens/floresta.jpg" alt="Pintura da Floresta">
                                                                            </div>
                                                                                  <button id="activateButton">Lembrar</button>
                                                                                      </div>
                                                                                        </div>

                                                                                          <script>
                                                                                              document.getElementById('activateButton').addEventListener('click', function () {
                                                                                                      const button = document.getElementById('activateButton');
                                                                                                            const image = document.getElementById('forestImage');

                                                                                                                  const staticImage = 'imagens/floresta.jpg';
                                                                                                                        const animatedGif = 'imagens/floresta.gif';

                                                                                                                              button.classList.add('fade-out');
                                                                                                                                    image.classList.add('image-fade');

                                                                                                                                          setTimeout(() => {
                                                                                                                                                    image.src = animatedGif;
                                                                                                                                                            image.classList.remove('image-fade');
                                                                                                                                          }, 1000);
                                                                                              });
                                                                                                </script>
                                                                                                </body>
                                                                                                </html>
                                                                                                                                          })
                                                                                              })
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
