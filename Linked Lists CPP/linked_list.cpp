#include "linked_list.hpp"

Node::Node(int value, Node* next_ptr) {
	this -> data = value;
	this -> next = next_ptr;
}

Node::~Node(){
	delete next;
	std::cout <<"instance of Node class: " << this << ", deleted" << '\n';
}

int Node::get_value() {
	return data;
}

void Node::set_next(Node* new_node) {
	
	this->next = new_node;
}

Node* Node::get_next() {
	return next;
	
}




