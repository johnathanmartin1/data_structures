#include "linked_list.hpp"

class Node {

private:
	int value{};
	std::unique_ptr<Node> next = std::make_unique<Node>(nullptr);

public:
	friend class Linked_List;
	
	/*----------constructor and destructor----------*/
	Node(int value, std::unique_ptr<Node> next) {
		
		this->value = value;
		this->next = std::make_unique<Node>(next);
	}

	~Node() {
	}

};



class Linked_List {

public:

	Node base(const int val)
	{
		return Node(val, nullptr);
	}

	void const add_node(const int val)
	{
		Node new_node = Node(val, nullptr);
		this->next = std::make_unique<Node>(new_node);
	}
};