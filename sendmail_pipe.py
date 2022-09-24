import base64
import sys
from bs4 import BeautifulSoup
import eml_parser


def get郵件本體字典(debug=False):
    if len(sys.argv) == 2:
        with open(sys.argv[1], "rb") as fhdl:
            eml_pipe = fhdl.read()
    elif debug:
        with open("example.eml", "rb") as fhdl:
            eml_pipe = fhdl.read()
    else:
        eml_pipe = sys.stdin.read().encode()
    # ep = eml_parser.eml_parser.EmlParser(include_attachment_data=True)
    # eml = ep.decode_email_bytes(eml_pipe)
    eml = eml_parser.eml_parser.decode_email_b(eml_pipe, True, True)
    print(eml["body"])
    return eml


if __name__ == "__main__":
    TMP_PATH = "/home/marty/github/ohlife/tmp/"
    eml_dict = get郵件本體字典()
    if eml_dict.get("attachment"):
        for i in eml_dict["attachment"]:
            x = base64.b64decode(i["raw"])
            with open(TMP_PATH + i["filename"], "wb") as f:
                f.write(x)
    else:
        print("No Attachment")
    the_day = eml_dict["header"].get("date")
    that_day = the_day.strftime("%Y-%m-%d")
    for i in eml_dict["body"]:
        if i["content_type"] == "text/plain":
            body = i["content"]
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
        f.write(body)
