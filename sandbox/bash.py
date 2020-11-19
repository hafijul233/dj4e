text = "X-DSPAM-Confidence:    0.8475"

ind = text.find("0.8475")
substr = text[ind:]
value = float(substr)
print(type(value))
print(value)
