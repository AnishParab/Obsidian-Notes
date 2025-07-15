``` cpp
#include<iostream>
using namespace std;

class Node {
public:
	int data;
	Node* next;

	Node(int data) {
		this->data = data;
		this-> next = NULL;
	}
};

void insertAtHead(int data, Node* &head) { //Take reference so that no copy is made
	Node* new_node = new Node(data);
	new_node->next = head;
	head = new_node;
}

int main() {
	Node* node1 = new Node(10);
	
	Node* head = node1;

	return 0;
}
```

---
