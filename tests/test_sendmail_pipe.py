from datetime import datetime
from tempfile import NamedTemporaryFile
import sys
import pprint

# from pathlib import Path
# sys.path[0] = str(Path(sys.path[0]).parent)
import sendmail_pipe

from sendmail_pipe import get乾淨的郵件本體list, get郵件本體字典自file, get郵件本體字典自stdin, main
import os
from io import BytesIO, StringIO
import sys

TMP_PATH = "./tmp/"
eml_dict = sendmail_pipe.get郵件本體字典自file("./tmp.sample/sample_image.eml")
that_day = eml_dict["header"].get("subject").split()[2]
if not os.path.isdir(TMP_PATH):
    os.mkdir(TMP_PATH)


def test_main_marty():
    assert sendmail_pipe.main(eml_dict, TMP_PATH, that_day).split()[0] == "第12測試"


def test_get_clean_body():
    dirty_body = "Hello\r\nWorld\r\n趙永華 Marty Chao\r\nOh Life Logger"
    expected_clean_body = ["Hello", "World"]
    assert get乾淨的郵件本體list(dirty_body) == expected_clean_body


def test_get_email_dict_from_stdin():
    sample_image_eml = "tmp.sample/sample_image.eml"
    with open(sample_image_eml, "r") as eml_handle:
        test_eml = eml_handle.read()

    sys.stdin = StringIO(test_eml)
    assert (
        get郵件本體字典自stdin()["header"]["subject"]
        == "Re: Today! 2022-09-23 星期五 DUO 3.0 No.1"
    )


def test_get_email_dict_from_file():
    expected_subject = "Test email"
    with NamedTemporaryFile(mode="w", delete=False) as tmp_file:
        tmp_file.write(
            f"From: test@example.com\nTo: test@example.com\nSubject: {expected_subject}\n\nThis is a test email."
        )
    assert get郵件本體字典自file(tmp_file.name)["header"]["subject"] == expected_subject
    os.unlink(tmp_file.name)
