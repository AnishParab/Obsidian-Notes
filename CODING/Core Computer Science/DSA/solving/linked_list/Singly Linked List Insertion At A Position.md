
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
	Node* new_node = new Node(5);

	new_node->next = head;
	head = new_node;
}

void insertAtTail(int data, Node* &tail) {
	Node* new_node = new Node(15);

	tail->next = new_node;
	tail = new_node;
}

void insertAtPosition(int data, Node* &head, Node* &tail, int position) {

// Edge Case: Insertion at Head
	if(position == 1) {
		insertAtHead(data, head);
		return;
	}

// temp variable
	Node* temp = head;
	int count = 1;

	while(count < position-1) {
		temp = temp->next;
		count++;
	}

// Edge Case: Insertion at Tail
	if(temp->next == NULL) {
		insertAtTail(data,tail);
		return;
	}

// Insertion at Position
	Node* new_node = new Node(data);

	new_node->next = temp->next;
	temp->next = new_node;
}

void printLL(Node* &head) {
	Node* temp = head;

	while(temp != NULL) {
		cout<< temp->data << " ";
		temp = temp->next;
	}
	cout<< "\n";
}

int main() {
	Node* node1 = new Node(10);

	Node* head = node1;
	Node* tail = node1;

	insertAtHead(5,head);
	
	insertAtTail(15,tail);
	insertAtTail(20,tail);
	insertAtTail(25,tail);
	insertAtTail(30,tail);

	insertAtPosition(69,head,tail,3);

	printLL(head);

	return 0;
}
```

---

