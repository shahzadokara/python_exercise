{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPiz9Kz/3N4sB9bLABCWYem",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shahzadokara/python_exercise/blob/master/panda.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aKQIWznaZMfI",
        "outputId": "1ffa8de1-0132-46c3-e882-c3ad53a849d9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "import pandas as pd\n",
        "a = pd.Series(data=[2,3,4], index=[\"ali\", \"Jhon\", \"shahzad\"])\n",
        "print(a)\n",
        "print()\n",
        "a.index\n",
        "print()\n",
        "\n",
        "\n"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "ali        2\n",
            "Jhon       3\n",
            "shahzad    4\n",
            "dtype: int64\n",
            "\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}