
n,index_of_converter_list,converter_list = None,None,None

def create_list_of_list():
    limit = int(input("enter limit"))
    index_of_converter_list = int(input("enter index of list"))
    converter_list = []
    for i in range(index_of_converter_list):
        converter_list_element = int(input("enter element of list"))
        converter_list.append(converter_list_element)
    
    return [converter_list[i:i+limit] for i in range(0,len(converter_list),limit)]
        



if __name__ == "__main__":
    print(create_list_of_list())