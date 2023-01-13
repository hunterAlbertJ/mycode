#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random

URL= "https://opentdb.com/api.php?amount=10&category=18&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    for x in data['results']:
        print(x["question"])
        answers_arr =  []
        answers_arr.append(x["correct_answer"])
        for x in x["incorrect_answers"]:
            answers_arr.append(x)
        random.shuffle(answers_arr)
        print(answers_arr)
if __name__ == "__main__":
    main()

