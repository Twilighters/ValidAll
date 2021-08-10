import main
from main import InputParameterVerificationError
import re

string_verifier = re.compile(r"^\d+$")

if not string_verifier.match(main.from_json_input1):
    raise InputParameterVerificationError("Должны быть только цифры при вводе")
if not string_verifier.match(main.from_json_input2):
    raise InputParameterVerificationError("Должны быть только цифры при вводе")
