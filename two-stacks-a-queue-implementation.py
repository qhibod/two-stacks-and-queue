#Run with python installed
output_queue = []

def convert_input_to_list(string):
    the_list = list(string.split(",")
    return the_list
    
    
def push_to_output_queue(the_list):
    length = len(the_list)
    iterator = 1
    diff = length - iterator
    while diff >= 0:
        output_queue.append(the_list[diff])
        iterator += 1
        diff = (length - iterator)
        
        
def print_output_queue(the_queue):
    for item in the_queue:
         print(item + " ")
         
         
         
# Main Program
input_one = input(" Enter input one separated by commas: ")
input_two = input(" Enter input two separated by commas: ")
list_one = convert_input_to_list(input_one)
list_two = convert_input_to_list(input_two)
push_to_output_queue(list_one)
push_to_output_queue(list_two)
print_output_queue(output_queue)
