#ifndef linked_lists
#define linked_lits

#include <iostream>
#include <string>
#include <memory>


/*_________________________Node_Class_______________________*/
class Node {

private:
	int data;
	Node* next;

public:
	Node(int value, Node* next_ptr = nullptr);

	~Node();

	int get_value();

	void set_next(Node& new_node);

	Node* get_next();

	

	

};
	
















#endif 
