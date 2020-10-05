import re


def txt_to_str(file):
    with open(file, 'r') as f:
        data = f.read().replace('\n', '').lower()
        data = re.sub('don\'t', 'do not', data)
        data = re.sub('you\'ll', 'you will', data)
        data = re.sub('we\'ll', 'we will', data)
    return data


def get_jaccard_sim(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    intset = set1.intersection(set2)
    return float(len(intset)) / (len(set1) + len(set2) - len(intset))


def text_sim(text1, text2):
    str1 = txt_to_str(text1)
    str2 = txt_to_str(text2)
    return get_jaccard_sim(str1, str2)


text_file_1 = input("Enter the path of the first text file : ")
text_file_2 = input("Enter the path of the second text file : ")

print('The similiarity metric between the two texts is', text_sim(text_file_1, text_file_2))
