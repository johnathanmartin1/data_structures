#include "linked_list.hpp"

Node::Node(int value, Node* next_ptr) {
	this -> data = value;
	this -> next = next_ptr;
}

Node::~Node(){}

int Node::get_value() {
	return data;
}

void Node::set_next(Node& new_node) {
	Node* node_ptr =  &new_node;
	this->next = node_ptr;
}

Node* Node::get_next() {
	return next;
	
}




