# Implementing Double linked list node.
class node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        

# Doubly Linked List implementation
class DoubleLinkedList:
    
    def __init__(self):
        
        self.head = node('<start>')
        self.cursor =  self.head
    
    
    def insert(self, val):
        """
        Inserts a new node with the given value next to the cursor.
        """
        new_node = node(val)

        new_node.prev = self.cursor
        new_node.next = self.cursor.next

        if self.cursor.next != None:
            self.cursor.next.prev = new_node

        self.cursor.next = new_node

        self.cursor = new_node
    
    
    def delete(self):
        """
        Deletes the current node (node at the cursor) and moves the cursor to the previous node.
        """
        if self.cursor.val == "<start>" :
            return
        
        prev = self.cursor.prev
        
        prev.next = self.cursor.next
        if self.cursor.next != None:
            self.cursor.next.prev = prev
        
        del self.cursor
        
        self.cursor = prev
    
    
    def display(self):
        """
        Displays the values of the linked list from the first node to the last node.
        """
        n = self.head.next
        while n!=None:
            
            print(n.val)
            n = n.next


# Text Editor using the Doubly Linked List           
class TextEditor:
    
    def __init__(self):
        
        self.linked_list = DoubleLinkedList()
        
    
    def AddText(self, letter):
        """
        Adds the given letter to the text by inserting it next to the cursor.
        """
        
        self.linked_list.insert(letter)
    
    
    def DeleteText(self, no_of_spaces):
        """
        Deletes the specified number of characters before the cursor position.
        """
        
        for i in range(no_of_spaces):
            self.linked_list.delete()
        
        
    def MoveRight(self, no_of_spaces):     
        """
        Moves the cursor to the right by the specified number of spaces.
        """
        
        for i in range(no_of_spaces):
            if self.linked_list.cursor.next != None:
                self.linked_list.cursor = self.linked_list.cursor.next
            else:
                break
            
        
    def MoveLeft(self, no_of_spaces):
        """
        Moves the cursor to the left by the specified number of spaces.
        """
        
        for i in range(no_of_spaces):
            
            if self.linked_list.cursor.prev != None:
                self.linked_list.cursor = self.linked_list.cursor.prev
            else:
                break
        
        
    def PrintText(self):
        """
        Prints the sequence of characters in the text to a file named 'outputPS03.txt'.
        """
        
        with open('outputPS03.txt', 'a') as f:
            temp = self.linked_list.head.next
            while temp!= None:
                print(temp.val, end="", file=f)
                temp = temp.next
            print(file=f)
        
        

# Reading the file sample_input
try:
    with open("inputPS03.txt", "r") as f:
        commands = f.read().split("\n")
except FileNotFoundError:
    print("Input file inputPS03.txt not found.")
    exit()


# Initialize the text editor
te = TextEditor()

# Before starting the program, delete all the content of the output file "outputPS03.txt"
with open('outputPS03.txt', 'w') as f:
    f.truncate(0)

# Process each command in the input file
for command in commands:

    # Extract the main command from the command string
    main_command = command.split(" ")[0]

    if main_command == "AddText":
        # Add text to the editor
        text_to_add = command[8:]
        if text_to_add != "":
            for s in text_to_add:
                te.AddText(s)
        else:
            print('AddText: given input does not contain any characters.')

    elif main_command == "DeleteText":
        # Delete text from the editor
        try:
            no_of_backspaces = int(command.split(' ')[1])
            te.DeleteText(no_of_backspaces)
        except:
            print('DeleteText: command format is incorrect.')
            

    elif main_command == "MoveLeft":
        # Move the cursor to the left
        try:
            no_of_leftmoves = int(command.split(' ')[1])
            te.MoveLeft(no_of_leftmoves)
        except:
            print('MoveLeft: command format is incorrect.')

    
    elif main_command == "MoveRight":
        # Move the cursor to the right
        try:
            no_of_rightmoves = int(command.split(' ')[1])
            te.MoveRight(no_of_rightmoves)
        except:
            print('MoveRight: command format is incorrect.')

    
    elif main_command == "PrintText":
        # Print the text to the output file "outputPS03.txt"
        if len(command) != 9:
            print('PrintText: command format is incorrect.') #. te.PrintText()
        else:
            te.PrintText()
        
    else:
        print("Incorrect Command.")
