from UkrPy import translate_ukrpy_to_python

with open("examples/hello.ua.py", encoding="utf-8") as f:
    ukr_code = f.read()

py_code = translate_ukrpy_to_python(ukr_code)
print("Перекладений код:\n", py_code)
exec(py_code)
