{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o3xlp_b0tII7",
        "outputId": "60acedec-223f-4f50-9cc3-c694f3af3df8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Buzz\n",
            "fizz\n",
            "7\n",
            "8\n",
            "fizz\n",
            "Buzz\n",
            "11\n",
            "fizz\n",
            "13\n",
            "14\n"
          ]
        }
      ],
      "source": [
        "#Mónica Ledesma \n",
        "#Tarea: Ejercicio Fizzbuzz\n",
        "\n",
        "#Valores iniciales\n",
        "ini= 5\n",
        "fin=15\n",
        "tres=\"fizz\" \n",
        "cinco=\"Buzz\"\n",
        "\n",
        "#Palabras que sustituyen si es divisible entre 3 o 5 por fizz o buzz, respectivamente\n",
        "for i in range(ini,fin):\n",
        "  if i%3 == 0 and i%5 == 0 : \n",
        "    print(tres+\" \"+cinco)\n",
        "  elif  i%3 == 0:\n",
        "        print(tres)\n",
        "  elif  i%5 == 0:\n",
        "        print(cinco)\n",
        "  else :\n",
        "    print(i)\n"
      ]
    }
  ]
}