with open('census.csv', encoding='utf8') as f:
    i = 0

    dictio = dict([
        ('Preschool', 0),
        ('1st-4th', 0),
        ('5th-6th', 0),
        ('7th-8th', 0),
        ('9th', 0),
        ('10th', 0),
        ('11th', 0),
        ('12th', 0),
        ('HS-grad', 0),
        ('Some-college', 0),
        ('Assoc-voc', 0),
        ('Assoc-acdm', 0),
        ('Bachelors', 0),
        ('Prof-school', 0),
        ('Masters', 0),
        ('Doctorate', 0)
    ])

    for line in f:
        entry = line.split(', ')
        edu_level = entry[3]
        if edu_level in dictio:
            dictio[edu_level] += 1
        if edu_level not in dictio:
            dictio[edu_level] = 1
        i += 1

    for item in dictio:
        print('{} -- {}'.format(dictio[item], item))

'''
Expected results:
(16 lines)
 5355 -- Bachelors
10501 -- HS-grad
 1175 -- 11th
 1723 -- Masters
  514 -- 9th
 7291 -- Some-college
 1067 -- Assoc-acdm
 1382 -- Assoc-voc
  646 -- 7th-8th
  413 -- Doctorate
  576 -- Prof-school
  333 -- 5th-6th
  933 -- 10th
  168 -- 1st-4th
   51 -- Preschool
  433 -- 12th
'''

'''
Suggestions from the class:
    - setdefault(item, 0) makes if not in dict not needed
    - Since every entry in file has at least one, you can also make dictionary empty
    - The syntax for dictionary is as follows:
        a_dict ={
         'key': value,
         'another key': another_value
        }
'''
