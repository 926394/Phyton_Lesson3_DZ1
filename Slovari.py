# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

word = (input('Здравствуйте! Слово БОЛЬШИМИ БУКВАМИ, для посчета очков: '))
spisok = list(word)
# РУССКИЙ СЛОВАРЬ
list_a = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list_b = ['Д', 'К', 'Л', 'М', 'П', 'У']
list_c = ['Б', 'Г', 'Ё', 'Ь', 'Я']
list_d = ['Й', 'Ы']
list_e = ['Ж', 'З', 'Х', 'Ц', 'Ч']
list_f = ['Ш', 'Э', 'Ю']
list_j = ['Ф', 'Щ', 'Ъ']
# English dictionary
list_a1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
list_b2 = ['D', 'G']
list_c3 = ['B', 'C', 'M', 'P']
list_d4 = ['F', 'H', 'V', 'W', 'Y']
list_e5 = ['K']
list_f6 = ['J', 'X']
list_j7 = ['Q', 'Z']
result = 0
print(spisok)
# РУССКИЙ СЛОВАРЬ
for i in spisok:
    for j in list_a:
        if i == j:
            result +=1            
for i in spisok:
    for j in list_b:
        if i == j:
            result +=2
for i in spisok:
    for j in list_c:
        if i == j:
            result +=3
for i in spisok:
    for j in list_d:
        if i == j:
            result +=4
for i in spisok:
    for j in list_e:
        if i == j:
            result +=5
for i in spisok:
    for j in list_f:
        if i == j:
            result +=8
for i in spisok:
    for j in list_j:
        if i == j:
            result +=10
# English dictionary
for i in spisok:
    for j in list_a1:
        if i == j:
            result +=1            
for i in spisok:
    for j in list_b2:
        if i == j:
            result +=2
for i in spisok:
    for j in list_c3:
        if i == j:
            result +=3
for i in spisok:
    for j in list_d4:
        if i == j:
            result +=4
for i in spisok:
    for j in list_e5:
        if i == j:
            result +=5
for i in spisok:
    for j in list_f6:
        if i == j:
            result +=8
for i in spisok:
    for j in list_j7:
        if i == j:
            result +=10
print(f"Ответ: слово '{word}' имеет {result} очков!")    

