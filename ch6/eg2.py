line= "X-DSPAM-Confidence:0.8475"
a=line.find(":")
print(float(line[a+1:]))