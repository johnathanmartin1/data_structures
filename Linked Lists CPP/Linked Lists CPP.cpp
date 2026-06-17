// Linked Lists CPP.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
//#include "linked_list.hpp"
#include "link_list_node.hpp"
#include <string>
int main()
{
    Node<std::string>* node1 = new Node<std::string>("hi");
  
    Node<std::string>* node2 = new Node<std::string>("there");
    
    Node<std::string>* node3 = new Node<std::string>("obi wan");
    
    node1->set_next(node2);
    
    node2->set_next(node3);
    
    std::cout << node1->get_value() << std::endl;
    
    std::cout << node1->get_next()->get_value() << std::endl;
   
    std::cout << node1->get_next()->get_next()->get_value() << std::endl;
    
    delete node1;
    
    std::cout << "hi" << std::endl;
    
    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
