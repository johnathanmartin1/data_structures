#ifndef temp_node
#define temp_node

#include <iostream>
#include <string>
#include <memory>
#include <string>

/*_________________________Node_Class_______________________*/
template <class T>
class Node {

private:
	/*node_variables*/

	T data;
	Node* next = nullptr;

public:
	/*constructor*/
	Node(T value, Node* next_ptr = nullptr) : data(value), next(next_ptr) {}

	/*destructor*/
	~Node() {
		delete next;
		std::cout << "instance of Node class: " << this << ", deleted" << '\n';
	};

	/*class methods*/
	T get_value() {
		return data;
	};

	void set_next(Node* new_node) {

		this -> next = new_node;
	};

	Node* get_next() {
		return next;

	};

};

#endif




