import base64
import sys
from bs4 import BeautifulSoup
import eml_parser
import pprint


def get郵件本體字典自stdin():
    eml_pipe = sys.stdin.read().encode()
    eml = eml_parser.parser.decode_email_b(eml_pipe, True, True)
    return eml


def get郵件本體字典自file(sample_image_eml):
    with open(sample_image_eml, "rb") as eml_handle:
        eml_pipe = eml_handle.read()
    eml = eml_parser.parser.decode_email_b(eml_pipe, True, True)
    return eml


def get乾淨的郵件本體list(body) -> list:
    body_text = []
    for i in body.split("\r\n"):
        if i == "趙永華 Marty Chao" or i[:14] == "Oh Life Logger":
            break
        else:
            body_text.append(i)
    return body_text


def main(eml_dict, TMP_PATH, that_day):
    if eml_dict.get("attachment"):
        for i in eml_dict["attachment"]:
            x = base64.b64decode(i["raw"])
            with open(
                TMP_PATH + that_day + "_ohlife." + i["filename"].split(".")[-1], "wb"
            ) as f:
                f.write(x)
    else:
        print("No Attachment")
    for i in eml_dict["body"]:
        if i["content_type"] == "text/plain":
            body = i["content"]
            break
        elif i["content_type"] == "text/html":
            soup = BeautifulSoup(i["content"], "lxml")
            p_data = soup.find_all("p")
            ree = []
            for j in p_data:
                res = j.get_text()
                ree.append(res)
            body = "".join(ree)
        else:
            body = i["content"].replace("\r\n", "")
    with open(TMP_PATH + that_day + "_ohlife.txt", "w") as f:
        for text in get乾淨的郵件本體list(body):
            f.write(text + "\n")
    if len(sys.argv) == 2 and sys.argv[1] == "text":
        pprint.pprint(eml_dict)
        print(body.split("\r\n"))
        pprint.pprint(get乾淨的郵件本體list(body))
        print(that_day)
        print(sys.argv)
    return body


if __name__ == "__main__":
    TMP_PATH = "./tmp/"
    eml_dict = get郵件本體字典自stdin()
    that_day = eml_dict["header"].get("subject").split()[2]
    main(eml_dict, TMP_PATH, that_day)
