{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ddf63e82-c7d4-415d-b4e3-72aa7db90af5",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<tokenize>, line 62)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m<tokenize>:62\u001b[1;36m\u001b[0m\n\u001b[1;33m    res.raise_for_status()\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": [
    "# Python script to scrape an article given the url of the article and store the extracted text in a file\n",
    "# Url: https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7\n",
    "\n",
    "import os\n",
    "import requests\n",
    "import re\n",
    "# Code here - Import BeautifulSoup library\n",
    "from bs4 import BeautifulSoup\n",
    "# Code ends here\n",
    "import sys\n",
    "# function to get the html source text of the medium article\n",
    "def get_page():\n",
    "\tglobal url\n",
    "\t\n",
    "\t# Code here - Ask the user to input \"Enter url of a medium article: \" and collect it in url\n",
    "\turl = input(\"Enter url of a medium article: \" )  # Ask user for input\n",
    "\t# Code ends here\n",
    "\t\n",
    "\t# handling possible error\n",
    "\tif not re.match(r'https?://medium.com/',url):\n",
    "\t\tprint('Please enter a valid website, or make sure it is a medium article')\n",
    "\t\tsys.exit(1)\n",
    "\n",
    "\t# Code here - Call gets method in requests object, pass url and collect it in res\n",
    "\tres = request.get(url)\n",
    "\t# Code ends here\n",
    "\n",
    "\tres.raise_for_status()\n",
    "\tsoup = BeautifulSoup(res.text, 'html.parser')\n",
    "\treturn soup\n",
    "\n",
    "# function to remove all the html tags and replace some with specific strings\n",
    "def clean(text):\n",
    "    rep = {\"<br>\": \"\\n\", \"<br/>\": \"\\n\", \"<li>\":  \"\\n\"}\n",
    "    rep = dict((re.escape(k), v) for k, v in rep.items()) \n",
    "    pattern = re.compile(\"|\".join(rep.keys()))\n",
    "    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)\n",
    "    text = re.sub('\\<(.*?)\\>', '', text)\n",
    "    return text\n",
    "\n",
    "\n",
    "def collect_text(soup):\n",
    "\ttext = f'url: {url}\\n\\n'\n",
    "\tpara_text = soup.find_all('p')\n",
    "\tprint(f\"paragraphs text = \\n {para_text}\")\n",
    "\tfor para in para_text:\n",
    "\t\ttext += f\"{para.text}\\n\\n\"\n",
    "\treturn text\n",
    "\n",
    "# function to save file in the current directory\n",
    "def save_file(text):\n",
    "\tif not os.path.exists('./scraped_articles'):\n",
    "        \n",
    "\t\tos.mkdir('./scraped_articles')\n",
    "\tname = url.split(\"/\")[-1]\n",
    "\tprint(name)\n",
    "\tfname = f'scraped_articles/{name}.txt'\n",
    "\t\n",
    "\t# Code here - write a file using with (2 lines)\n",
    "\tres = requests.get(url)\n",
    "    \n",
    "    res.raise_for_status()\n",
    "    soup = BeautifulSoup(res.text, 'html.parser')\n",
    "    return soup\n",
    "\t# Code ends here\n",
    "\n",
    "\tprint(f'File saved in directory {fname}')\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "\ttext = collect_text(get_page())\n",
    "\tsave_file(text)\n",
    "\t# Instructions to Run this python code\n",
    "\t# Give url as https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebb5af94-10ed-4975-8ac9-330da6dfd3b1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}