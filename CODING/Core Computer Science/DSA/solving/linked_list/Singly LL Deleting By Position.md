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

	~Node() {
		int value = this->data;

		if(this->next != NULL) {
			delete next;
			this->next = NULL;
		}
		cout<< "Memory is free for data " << value << "\n";
	}
};

void insertionAtHead(int data, Node* &head) {
	Node* new_node = new Node(data);

	new_node->next = head;
	head = new_node;
}

void insertionAtTail(int data, Node* &tail) {
	Node* new_node = new Node(data);

	tail->next = new_node;
	tail = new_node;
}

void insertionAtPosition(int data, int position, Node* &head, Node* &tail) {
	// Edge case: Insertion at Head
	if(position == 1) {
		insertionAtHead(data, head);
		return;
	}

	// temp variable
	Node* temp = head;
	int count = 1;

	while(count < position-1) {
		temp = temp->next;
		count++;
	}

	// Edge case: Insertion at Tail
	if(temp->next == NULL) {
		insertionAtTail(data, tail);
		return;
	}

	// Insertion At Position
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

void deleteNodeByPos(int position, Node* &head) {

	// Edge Case: First Position
	if(position == 1) {
		Node* temp = head;

		head = head->next;
		// Prevent segmentation fault
		temp->next = NULL;
		delete temp;
	} else {
		Node* current = head;
		Node* previous = NULL;

		int count = 1;
		while(count < position) {
			previous = current;
			current = current->next;
			count++;
		}

		// Deleting
		previous->next = current->next;
		// Prevent Segmentation fault
		current->next = NULL;
		delete current;
	}
}

int main() {
	Node* node1 = new Node(10);

	Node* head = node1;
	Node* tail = node1;

	insertionAtHead(5, head);
	insertionAtTail(15, tail);
	insertionAtTail(20, tail);
	insertionAtPosition(69, 3, head, tail);

	printLL(head);

	return 0;
}
```

---
