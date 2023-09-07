from stack import Mystack


def check_seq(mystring):

    parenthesis = Mystack(len(mystring))
    parenthesis = Mystack.newstack(parenthesis)
    mapping = {'{': '}', '(': ')', '[': ']'}
    early_compl = False

    for element in mystring:
        # esli skobka otkrivaetsia
        if element in mapping.keys():
            Mystack.push(parenthesis, element)
        # esli skobka zakrivaetsia    
        elif element in mapping.values():
            # esli posledovatelnost nachalas s zakriv. skobki to dobavliaem v stack
            if Mystack.is_empty(parenthesis):
                Mystack.push(parenthesis, element)
            # proveriaem chto esli skobka zakriv. to prediduschaya eto ee para
            else:
                if element == mapping[Mystack.peek(parenthesis)]:
                    Mystack.pop(parenthesis)
                else:
                    early_compl = True

    if Mystack.is_empty(parenthesis) and not early_compl:
        print('Balanced')
    elif early_compl:
        print('Disbalanced')
    else:
        print('Disbalanced')


if __name__ == '__main__':

    check_seq(input("Enter parenthesis sequence:"))

    #nuzhno proverit esli sle element posle otkrivaushego zakravaishiu to chtobi on bil matching