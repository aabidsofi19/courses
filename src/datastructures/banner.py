
schema = {
    1 : "4* 2-,4* 2-,2- 2* 2-,2- 2* 2-,2- 2* 2-,2- 2* 2-,6*,6*"
}



def schema_printer(num) :
    schema_ = schema[num]

    lines = schema_.split(",")

    for  line in lines : 
        x = ""
        for steps,char in line.split(" ") :
            if char == "-" :
                char = " "
            x += char* int(steps)
        print(x)


schema_printer(1)





