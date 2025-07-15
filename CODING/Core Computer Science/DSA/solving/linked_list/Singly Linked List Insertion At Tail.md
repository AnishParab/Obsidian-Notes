``` cpp
#include<iostream>
using namespace std;

class Node {
public:
	int data;
	Node* next;

	Node(int data) {
		this->data = data;
		this->next = NULL;
	}
};

void insertAtTail(int data, Node* &tail) {
	Node* new_node = new Node(data);
	tail->next = new_node;
	tail = new_node;
}

void printLL(Node* &head) {
	Node* temp = head;

	while(temp != NULL) {
		cout<< temp->data << " ";
		temp = temp->next;
	}
	cout<<"\n";
}

int main() {
	Node* node1 = new Node(10);

	Node* head = node1;
	Node* tail = node1;

	insertAtTail(15, tail);

	insertAtTail(20, tail);

	printLL(head);

	return 0;
}
```

---
