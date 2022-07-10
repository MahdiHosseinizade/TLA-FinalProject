def decoding(current :1, current_index :10,strip, transition):
    if current == len(transition):
        # print(current)
        return "Accepted"
    if  strip[current_index] not in transition[current]:
        return "Rejected"
    temp = transition[current][strip[current_index]]
    # print(temp)
    current = temp[0]
    strip[current_index] = temp [1]
    Way = temp[2]
    if Way != 1:
        current_index = current_index + 1
    else:
        current_index = current_index - 1
    return decoding(current, current_index, strip, transition)


def main():
    turing_machine = {}
    turing = input()
    i = 0
    counter = 0
    temp = ""
    rules = []
    Dir = []
    # for separeate "00" 
    while i < len(turing) - 1:
            if turing[i] == '0' and turing[i + 1] == '0':
                for j in range(counter, i):
                    temp += turing[j]
                rules.append(temp)
                counter = i + 2
                temp = ""
            i += 1
    j = counter
    while j < len(turing):
        temp += turing[j]
        j += 1
    rules.append(temp)
    for direct in rules:
        spell = direct.split('0')
        start = len(spell[0])  
        variable = len(spell[1]) 
        end = len(spell[2]) 
        write = len(spell[3]) 
        way = len(spell[4])  
        if start not in turing_machine:
            turing_machine[start] = {}
        if end not in turing_machine:
            turing_machine[end] = {}
        set_tuple = (end,write,way)
        turing_machine[start][variable] = set_tuple
    number = int(input())
    for i in range(0,number):
        Dir.append(input())
        i+=1
    for query in Dir:
        if query == "" :
            strip = []
            strip.append(1)
        else:
            strip = []
            for str in query.split('0'):
                len_str = len(str)
                strip.append(len_str)
        newstrip = ([1] * 10) + strip +( [1] * 10)
        strip = newstrip
        out = decoding(1,10, strip,turing_machine)
        print(out)


main()