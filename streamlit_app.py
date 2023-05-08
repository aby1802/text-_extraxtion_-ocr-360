{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aby1802/text-_extraxtion_-ocr-360/blob/main/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Al_ZUOMbOTSN",
        "outputId": "f4b45b80-39bd-48f4-ba1c-275c71f72a0c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "The following additional packages will be installed:\n",
            "  tesseract-ocr-eng tesseract-ocr-osd\n",
            "The following NEW packages will be installed:\n",
            "  tesseract-ocr tesseract-ocr-eng tesseract-ocr-osd\n",
            "0 upgraded, 3 newly installed, 0 to remove and 24 not upgraded.\n",
            "Need to get 4,850 kB of archives.\n",
            "After this operation, 16.3 MB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu focal/universe amd64 tesseract-ocr-eng all 1:4.00~git30-7274cfa-1 [1,598 kB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu focal/universe amd64 tesseract-ocr-osd all 1:4.00~git30-7274cfa-1 [2,990 kB]\n",
            "Get:3 http://archive.ubuntu.com/ubuntu focal/universe amd64 tesseract-ocr amd64 4.1.1-2build2 [262 kB]\n",
            "Fetched 4,850 kB in 1s (4,816 kB/s)\n",
            "Selecting previously unselected package tesseract-ocr-eng.\n",
            "(Reading database ... 122518 files and directories currently installed.)\n",
            "Preparing to unpack .../tesseract-ocr-eng_1%3a4.00~git30-7274cfa-1_all.deb ...\n",
            "Unpacking tesseract-ocr-eng (1:4.00~git30-7274cfa-1) ...\n",
            "Selecting previously unselected package tesseract-ocr-osd.\n",
            "Preparing to unpack .../tesseract-ocr-osd_1%3a4.00~git30-7274cfa-1_all.deb ...\n",
            "Unpacking tesseract-ocr-osd (1:4.00~git30-7274cfa-1) ...\n",
            "Selecting previously unselected package tesseract-ocr.\n",
            "Preparing to unpack .../tesseract-ocr_4.1.1-2build2_amd64.deb ...\n",
            "Unpacking tesseract-ocr (4.1.1-2build2) ...\n",
            "Setting up tesseract-ocr-eng (1:4.00~git30-7274cfa-1) ...\n",
            "Setting up tesseract-ocr-osd (1:4.00~git30-7274cfa-1) ...\n",
            "Setting up tesseract-ocr (4.1.1-2build2) ...\n",
            "Processing triggers for man-db (2.9.1-1) ...\n",
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "The following additional packages will be installed:\n",
            "  libarchive-dev libleptonica-dev\n",
            "The following NEW packages will be installed:\n",
            "  libarchive-dev libleptonica-dev libtesseract-dev\n",
            "0 upgraded, 3 newly installed, 0 to remove and 24 not upgraded.\n",
            "Need to get 3,343 kB of archives.\n",
            "After this operation, 15.7 MB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libarchive-dev amd64 3.4.0-2ubuntu1.2 [491 kB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu focal/universe amd64 libleptonica-dev amd64 1.79.0-1 [1,389 kB]\n",
            "Get:3 http://archive.ubuntu.com/ubuntu focal/universe amd64 libtesseract-dev amd64 4.1.1-2build2 [1,463 kB]\n",
            "Fetched 3,343 kB in 1s (3,706 kB/s)\n",
            "Selecting previously unselected package libarchive-dev:amd64.\n",
            "(Reading database ... 122565 files and directories currently installed.)\n",
            "Preparing to unpack .../libarchive-dev_3.4.0-2ubuntu1.2_amd64.deb ...\n",
            "Unpacking libarchive-dev:amd64 (3.4.0-2ubuntu1.2) ...\n",
            "Selecting previously unselected package libleptonica-dev:amd64.\n",
            "Preparing to unpack .../libleptonica-dev_1.79.0-1_amd64.deb ...\n",
            "Unpacking libleptonica-dev:amd64 (1.79.0-1) ...\n",
            "Selecting previously unselected package libtesseract-dev:amd64.\n",
            "Preparing to unpack .../libtesseract-dev_4.1.1-2build2_amd64.deb ...\n",
            "Unpacking libtesseract-dev:amd64 (4.1.1-2build2) ...\n",
            "Setting up libleptonica-dev:amd64 (1.79.0-1) ...\n",
            "Setting up libarchive-dev:amd64 (3.4.0-2ubuntu1.2) ...\n",
            "Setting up libtesseract-dev:amd64 (4.1.1-2build2) ...\n",
            "Processing triggers for man-db (2.9.1-1) ...\n"
          ]
        }
      ],
      "source": [
        "!apt install tesseract-ocr\n",
        "!apt install libtesseract-dev\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rf8M58c-OXnB",
        "outputId": "8ba8328b-9ee0-4368-de2a-8401e39b4576"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pytesseract\n",
            "  Downloading pytesseract-0.3.10-py3-none-any.whl (14 kB)\n",
            "Requirement already satisfied: packaging>=21.3 in /usr/local/lib/python3.10/dist-packages (from pytesseract) (23.1)\n",
            "Requirement already satisfied: Pillow>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from pytesseract) (8.4.0)\n",
            "Installing collected packages: pytesseract\n",
            "Successfully installed pytesseract-0.3.10\n"
          ]
        }
      ],
      "source": [
        "!pip install pytesseract\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import re\n",
        "\n"
      ],
      "metadata": {
        "id": "xSw_AM-oK6F9"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def extract_data(text):\n",
        "    data = {}\n",
        "    lines = text.split('\\n')\n",
        "    lines = [line for line in lines if line.strip()]\n",
        "    for line in lines:\n",
        "        if re.match(r'^\\w{10}$', line):\n",
        "            data['id'] = line\n",
        "        elif 'ವಯಸ್ಸು :' in line:\n",
        "            data['age_gender'] = line\n",
        "        elif 'ಮನೆಯ ಸಂಖ್ಯೆ:' in line:\n",
        "            data['house_number'] = line\n",
        "        elif 'ಹೆಸರು:' in line:\n",
        "            data['name'] = line\n",
        "        elif 'ತಂದೆಯ ಹೆಸರು:' in line:\n",
        "            data['father_name'] = line\n",
        "    return data\n"
      ],
      "metadata": {
        "id": "OY0bd-GEK6I5"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data_list = []\n"
      ],
      "metadata": {
        "id": "QzXMwqCIK6N-"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get install poppler-utils\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y7mTaPirLkwy",
        "outputId": "92b30d91-a6de-4edb-899b-bc550f1ef31e"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "The following NEW packages will be installed:\n",
            "  poppler-utils\n",
            "0 upgraded, 1 newly installed, 0 to remove and 24 not upgraded.\n",
            "Need to get 174 kB of archives.\n",
            "After this operation, 754 kB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 poppler-utils amd64 0.86.1-0ubuntu1.1 [174 kB]\n",
            "Fetched 174 kB in 1s (269 kB/s)\n",
            "Selecting previously unselected package poppler-utils.\n",
            "(Reading database ... 122518 files and directories currently installed.)\n",
            "Preparing to unpack .../poppler-utils_0.86.1-0ubuntu1.1_amd64.deb ...\n",
            "Unpacking poppler-utils (0.86.1-0ubuntu1.1) ...\n",
            "Setting up poppler-utils (0.86.1-0ubuntu1.1) ...\n",
            "Processing triggers for man-db (2.9.1-1) ...\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pdf2image\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dUhBfjWtLo8l",
        "outputId": "c987da75-fab0-40ed-b911-9db1d20186f4"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pdf2image\n",
            "  Downloading pdf2image-1.16.3-py3-none-any.whl (11 kB)\n",
            "Requirement already satisfied: pillow in /usr/local/lib/python3.10/dist-packages (from pdf2image) (8.4.0)\n",
            "Installing collected packages: pdf2image\n",
            "Successfully installed pdf2image-1.16.3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!apt-get install tesseract-ocr\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ElpxlQ8ZL2iG",
        "outputId": "c7945f08-4d5a-442f-8f89-40debe50f88e"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "The following additional packages will be installed:\n",
            "  tesseract-ocr-eng tesseract-ocr-osd\n",
            "The following NEW packages will be installed:\n",
            "  tesseract-ocr tesseract-ocr-eng tesseract-ocr-osd\n",
            "0 upgraded, 3 newly installed, 0 to remove and 24 not upgraded.\n",
            "Need to get 4,850 kB of archives.\n",
            "After this operation, 16.3 MB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu focal/universe amd64 tesseract-ocr-eng all 1:4.00~git30-7274cfa-1 [1,598 kB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu focal/universe amd64 tesseract-ocr-osd all 1:4.00~git30-7274cfa-1 [2,990 kB]\n",
            "Get:3 http://archive.ubuntu.com/ubuntu focal/universe amd64 tesseract-ocr amd64 4.1.1-2build2 [262 kB]\n",
            "Fetched 4,850 kB in 1s (4,299 kB/s)\n",
            "Selecting previously unselected package tesseract-ocr-eng.\n",
            "(Reading database ... 122548 files and directories currently installed.)\n",
            "Preparing to unpack .../tesseract-ocr-eng_1%3a4.00~git30-7274cfa-1_all.deb ...\n",
            "Unpacking tesseract-ocr-eng (1:4.00~git30-7274cfa-1) ...\n",
            "Selecting previously unselected package tesseract-ocr-osd.\n",
            "Preparing to unpack .../tesseract-ocr-osd_1%3a4.00~git30-7274cfa-1_all.deb ...\n",
            "Unpacking tesseract-ocr-osd (1:4.00~git30-7274cfa-1) ...\n",
            "Selecting previously unselected package tesseract-ocr.\n",
            "Preparing to unpack .../tesseract-ocr_4.1.1-2build2_amd64.deb ...\n",
            "Unpacking tesseract-ocr (4.1.1-2build2) ...\n",
            "Setting up tesseract-ocr-eng (1:4.00~git30-7274cfa-1) ...\n",
            "Setting up tesseract-ocr-osd (1:4.00~git30-7274cfa-1) ...\n",
            "Setting up tesseract-ocr (4.1.1-2build2) ...\n",
            "Processing triggers for man-db (2.9.1-1) ...\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pytesseract\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lAwXr4zZL2lb",
        "outputId": "65f25cfa-4cab-43de-d3a3-7fe0f41f744b"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: pytesseract in /usr/local/lib/python3.10/dist-packages (0.3.10)\n",
            "Requirement already satisfied: packaging>=21.3 in /usr/local/lib/python3.10/dist-packages (from pytesseract) (23.1)\n",
            "Requirement already satisfied: Pillow>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from pytesseract) (8.4.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pytesseract\n",
        "pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'\n"
      ],
      "metadata": {
        "id": "HCV84jD5L2sV"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!wget https://github.com/tesseract-ocr/tessdata/raw/main/kan.traineddata -P /usr/share/tesseract-ocr/4.00/tessdata/\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tWSaxl50MOsD",
        "outputId": "9fea3359-5ced-4df8-c842-3b01c6ad5b04"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2023-05-08 21:07:37--  https://github.com/tesseract-ocr/tessdata/raw/main/kan.traineddata\n",
            "Resolving github.com (github.com)... 140.82.114.4\n",
            "Connecting to github.com (github.com)|140.82.114.4|:443... connected.\n",
            "HTTP request sent, awaiting response... 302 Found\n",
            "Location: https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/kan.traineddata [following]\n",
            "--2023-05-08 21:07:38--  https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/kan.traineddata\n",
            "Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...\n",
            "Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 3608311 (3.4M) [application/octet-stream]\n",
            "Saving to: ‘/usr/share/tesseract-ocr/4.00/tessdata/kan.traineddata’\n",
            "\n",
            "kan.traineddata     100%[===================>]   3.44M  --.-KB/s    in 0.07s   \n",
            "\n",
            "2023-05-08 21:07:38 (50.1 MB/s) - ‘/usr/share/tesseract-ocr/4.00/tessdata/kan.traineddata’ saved [3608311/3608311]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/'\n"
      ],
      "metadata": {
        "id": "tsDMnzqLMOvZ"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pdf2image import convert_from_path\n",
        "import pytesseract\n",
        "\n",
        "pages = convert_from_path('/content/OCR_Dataset_unlocked.10 (1).pdf', dpi=300)\n",
        "\n",
        "for page in pages:\n",
        "    text = pytesseract.image_to_string(page, lang='kan')\n",
        "    data_list.append(extract_data(text))\n"
      ],
      "metadata": {
        "id": "ZZsrubSVLOLe"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.DataFrame(data_list)\n"
      ],
      "metadata": {
        "id": "x_R6NGiQNWPj"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.to_csv('output.csv', index=False, encoding='utf-8-sig')\n",
        "\n"
      ],
      "metadata": {
        "id": "T0AXoujfNYtL"
      },
      "execution_count": 19,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPDica7SMkwtKEeCF6YKAyD",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}