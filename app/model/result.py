import re
from .person import Person

class Result:
    @staticmethod
    def regex_nama(string):
        return re.search ("(.+nama.+|^nam|^na.+) ([\s\S]*?)",string)
    
    @staticmethod    
    def regex_nik(string):
        return re.search("^ni", string)
    
    @staticmethod   
    def regex_tempat(string):
        return re.search("(^tempat|^tempa|^temp|temp)([\s\S]*?)",string)

    @staticmethod
    def regex_tgl_lahir(string):
        return re.search("(^tempat|^tempa|^temp|temp)([\s\S]*?)",string)

    @staticmethod
    def regex_prov(string):
        return re.search("(^prov|^pro.+vinsi\s)",string)

    @staticmethod
    def regex_kab(string):
        return re.search("(^kab|^kot|^kab.+ten\s|^ko.+ta\s)",string)
    
    @staticmethod
    def regex_kec(string):
        return re.search("(^kec|^ke.+tan\s)",string)
    
    @staticmethod
    def regex_kel(string):
        return re.search("(^kel|^ke.+han\s)",string)

    @staticmethod
    def regex_rt_rw(string):
        return re.search("(^rtrw|^rt|^rw\s)",string)

    @staticmethod
    def nik_extract(word):
        word_dict = {
            'b' : "6",
            'e' : "2",
            'y': "4",
        }
        res = ""
        for letter in word:
            if letter in word_dict:
                res += word_dict[letter]
            else:
                res += letter
        replace_text = res.replace('NIK', '')
        replace_text = replace_text.replace(' ', '')
        return replace_text

    @staticmethod
    def prov_extract(word):
         replace_text = word.replace('provinsi ', '')
         return replace_text
    
    @staticmethod
    def rt_rw_extract(word):
        rt = ""
        rw = ""
        replace_text = word.replace('rtrw ', '')
        replace_text = replace_text.replace('rt/rw ', '')
        replace_text = replace_text.replace('rtirw :', '')
        replace_text = replace_text.replace('rt/rw :', '')
        replace_text = replace_text.replace(':', '')
        replace_text = replace_text.replace('/', ' ')
        splited_text = replace_text.split(' ')
        if len(splited_text) > 1:
            rt = splited_text[0]
            rw = splited_text[1]
        return rt, rw

    @staticmethod
    def ttl_extraxt(word):
        tempat = ""
        tgl_lahir = ""
        splited_text = word.split(',')
        if len(splited_text) > 1:
            tempat = splited_text[0]
            tgl_lahir = splited_text[1]
        return tempat, tgl_lahir

    @staticmethod
    def prepare_result(list_of_string):
        person = Person()
        if list_of_string is not None:
            person.nama = list_of_string[5]
            person.nik = Result.nik_extract(list_of_string[2])
            for item in list_of_string:
                item = item.lower()
                if Result.regex_prov(item):
                    prov = Result.prov_extract(item)
                    person.prov = prov
                if len(list_of_string) <= 23:
                    tempat, tgl_lahir = Result.ttl_extraxt(list_of_string[7])
                    if len(list_of_string) <= 21:
                        tempat, tgl_lahir = Result.ttl_extraxt(list_of_string[6])
                    person.tempat = tempat.lower()
                    person.tgl_lahir = tgl_lahir
                else:
                    if Result.regex_tempat(item):
                        person.tempat = item
                    if Result.regex_tgl_lahir(item):
                        person.tgl_lahir = item
                if Result.regex_kab(item):
                    person.kab = item
                if Result.regex_kec(item):
                    person.kec = item
                if Result.regex_kel(item):
                    person.kel = item
                if Result.regex_rt_rw(item):
                    rt, rw = Result.rt_rw_extract(item)
                    person.rt = rt
                    person.rw = rw
        return person