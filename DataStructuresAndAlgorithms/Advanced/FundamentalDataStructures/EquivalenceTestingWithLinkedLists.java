/**
 * 
 * @author ChiangWei
 * @date 2020/3/7
 *
 */

public class EquivalenceTestingWithLinkedLists<E> {
	private static class Node<E> {
		private E element;
		private Node<E> next;
		public Node(E e, Node<E> n) {
			element = e;
			next = n;
		}
		public E getElement() { return element; }
		public Node<E> getNext() { return next; }
		public void setNext(Node<E> n) { next = n; }
	}
	
	private Node<E> head = null;
	private Node<E> tail = null;
	private int size = 0;
	public EquivalenceTestingWithLinkedLists() {}
	
	public int size() {
		return size;
	}
	
	public boolean isEmpty() {
		return size == 0;
	}
	
	public E first() {
		if (isEmpty()) return null;
		return head.getElement();
	}
	
	public E last() {
		if (isEmpty()) return null;
		return tail.getElement();
	}
	
	public void addFirst(E e) {
		head = new Node<>(e, head);
		if (size == 0) tail = head;
		size++;
	}
	
	public void addLast(E e) {
		Node<E> newest = new Node<>(e, null);
		if (isEmpty()) head = newest;
		else tail.setNext(newest);
		tail = newest;
		size++;
	}
	
	public E removeFirst() {
		if (isEmpty()) return null;
		E answer = head.getElement();
		head = head.getNext();
		size--;
		if (size == 0) tail = null;
		return answer;
	}
	
	public String toString() {
		String str = "";
		Node<E> temp = head;
		while (temp != null) {
			str += temp.getElement();
			temp = temp.getNext();
		}
		return str;
	}
	
	public boolean equals(Object o) {
		if (o == null) return false;
		if (getClass() != o.getClass()) return false;
		EquivalenceTestingWithLinkedLists other = (EquivalenceTestingWithLinkedLists)o;
		if (size != other.size) return false;
		Node walkA = head;
		Node walkB = other.head;
		while (walkA != null) {
			if (!walkA.getElement().equals(walkB.getElement())) return false;
			walkA = walkA.getNext();
			walkB = walkB.getNext();
		}
		return true;
	}
	
	public static void main(String[] args) {
		EquivalenceTestingWithLinkedLists<Character> singlyLinkedListsA = new EquivalenceTestingWithLinkedLists<>();
		for (int i = 0; i < 5; i++) singlyLinkedListsA.addLast((char)('A' + i));
		EquivalenceTestingWithLinkedLists<Character> singlyLinkedListsB = new EquivalenceTestingWithLinkedLists<>();
		for (int i = 0; i < 5; i++) singlyLinkedListsB.addLast((char)('A' + i));
		System.out.println(singlyLinkedListsA.equals(singlyLinkedListsB));
		for (int i = 0; i < 5; i++) singlyLinkedListsB.addLast((char)('A' + i));
		System.out.println(singlyLinkedListsA.equals(singlyLinkedListsB));
	}
}
