/**
 * 
 * @author ChiangWei
 * @date 2020/3/7
 *
 */

public class CloningLinkedLists<E> implements Cloneable {
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
	public CloningLinkedLists() {}
	
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
	
	public CloningLinkedLists<E> clone() throws CloneNotSupportedException {
		CloningLinkedLists<E> other = (CloningLinkedLists<E>)super.clone();
		if (size > 0) {
			other.head = new Node<>(head.getElement(), null);
			Node<E> walk = head.getNext();
			Node<E> otherTail = other.head;
			while (walk != null) {
				Node<E> newest = new Node<>(walk.getElement(), null);
				otherTail.setNext(newest);
				otherTail = newest;
				walk = walk.getNext();
			}
		}
		return other;
	}
	
	public static void main(String[] args) throws CloneNotSupportedException {
		CloningLinkedLists<Integer> cloningLinkedListsA = new CloningLinkedLists<>();
		cloningLinkedListsA.addFirst(1);
		CloningLinkedLists<Integer> cloningLinkedListsB = cloningLinkedListsA.clone();
		System.out.println(cloningLinkedListsA.first());
		System.out.println(cloningLinkedListsB.first());
		System.out.println(cloningLinkedListsA.head == cloningLinkedListsB.head);
	}
}
