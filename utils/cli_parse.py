import sys
arg_list = []

VIABLE_FLAGS = ["-h", "-in", "-IN", "-out", "-o", "-rows", "-cols", "-gap"]

'''
1. go through arg list and check flags
2. validate the arguments that flags take
3. put it in some kind of container
'''
current_index = 0

'''
match something:
    case "-h":

    case "-in":

    case "-IN":

    case "-out":
    case "-o"

    case "-rows":

    case "-cols":

    case "-gap"

    case _:
        ##default case 
'''



def tokenize_cli_arguments():
    temp_flag_arguments = []
    current_flag = ""

    for arg in sys.argv[1:]:
        if arg in VIABLE_FLAGS and arg != current_flag:
            if current_flag:
                arg_list.append({current_flag : temp_flag_arguments})
                temp_flag_arguments = []
            current_flag = arg
        elif current_flag:
            temp_flag_arguments.append(arg)
        else:
            raise Exception(f' Unknown argument was passed: "{arg}"')

    arg_list.append({current_flag : temp_flag_arguments}) # last pair