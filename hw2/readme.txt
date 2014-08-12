THE FILE TO RUN IS main.py


Class system (classes.py)

The system of classes can be briefly explained as follows:
    - FinInstument - the basic class for all financial instruments (Bond, Stock, MutualFund). The purpose of it is to serve as an
    interface. Hence, other classes which use either of these financial instruments don't have to bother which one they actually use. 
    This follows the idea of a clear separation of the elements of the program. First, it makes it easier to add more 
    classes for financial instruments. Second, due to its internal completeness, higher level classes don't need to specify class-specific
    operations on the array of FinInstruments. For example, each FinInstrument has buy() and sell(), which is diffirent dependent on
    the child class. Meanwhile, the call of this functions looks the same. Buy() and sell() return the monetary result of the operation,
    meaning expenses or input. The actual change in the instance of the class, such as the change of the amount, is their side effects. 
    
    - The child classes of FinInstrument: Stock, Bond, MutualFund
    
    - FinList - a class which wraps a list of FinInstruments. The core of this class is the list of the objects, each of which is one
    instance of a either of the classes Bond, Stock, MutualFund. By construction, it is assumed that all objects in the list belong to the same class.
    The type of the class is saved in the type field and is used in the print function. When the user wants to sell or buy an assert, the wrapper
    finds this assert in the list if it is there or adds it in the other case or deletes it. Having found the assert, the wrapper just calls
    functions buy or sell which are defined in "each element" of the list.        

    - Portfolio - the wrapper for all financial instruments.

functions.py contains functions independent relative to the classes above 

The log of the operations is stored in the program folder. 