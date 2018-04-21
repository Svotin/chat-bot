#!/usr/bin/python3
# -*- coding: utf-8 -*-
import codecs

inp_file = "sample.txt"
outp_file = "output.txt"

def main():

    f_inp = codecs.open(inp_file,"r","utf_8_sig")
    f_out = codecs.open(outp_file,"w","utf_8_sig")
    text = f_inp.read()

    for section in text.split('\n'):
        if section[0]=='—':           # ТИРЕ МОЖЕТ БЫТЬ ДРУГОЕ, ЗАВИСИТ ОТ ТЕКСТА
            dashless = section.split("— ")    # ТИРЕ МОЖЕТ БЫТЬ ДРУГОЕ, ЗАВИСИТ ОТ ТЕКСТА
            f_out.write("-")
            for i in range(1,dashless.__len__(),2):
                f_out.write(dashless[i]+"  ")
            f_out.write("\n")

    f_inp.close()



if __name__ == '__main__':
    main()