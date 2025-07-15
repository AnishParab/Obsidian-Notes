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

void insertAtHead(int data, Node* &head) {
	Node* new_node = new Node(data);
	new_node-> next = head;
	head = new_node;
}

void printLL(Node* &head) {
	Node* temp = head;

	while(temp != NULL) {
		cout<< temp->data <<" ";
		temp = temp->next;
	}
	cout<<"\n";
}

int main(){
	Node* node1 = new Node(10);

	Node* head = node1;
	printLL(head);

	insertAtHead(12, head);
	printLL(head);

	insertAtHead(15, head);
	printLL(head);

	return 0;
}
```

---
