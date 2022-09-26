import sendmail_pipe

TMP_PATH = "./tmp/"
eml_dict = sendmail_pipe.get郵件本體字典自file("./tmp.sample/sample_image.eml")
that_day = eml_dict["header"].get("subject").split()[2]


def test_main():
    assert sendmail_pipe.main(eml_dict, TMP_PATH, that_day).split()[0] == "第12測試"
