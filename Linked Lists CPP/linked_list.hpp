#ifndef linked_lists
#define linked_lits

#include <iostream>
#include <string>
#include <memory>

class Node
{
private:
	int value;
	std::unique_ptr<Node> next;

public:
	Node(int value, std::unique_ptr<Node> next);

	~Node();

	int get_value();

};
	



class Linked_List
{
public:

	Node base(const int val);

	void add(const int val);
};
#endif