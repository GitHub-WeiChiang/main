/**
 * 
 * @author ChiangWei
 * @date 2020/3/24
 *
 */

import java.util.ArrayList;
import java.util.Iterator;

public class LinkedBinaryTree<E> extends AbstractBinaryTree<E> {
	protected static class Node<E> implements Position<E> {
		private E element;
		private Node<E> parent;
		private Node<E> left;
		private Node<E> right; 
		
		public Node(E e, Node<E> above, Node<E> leftChild, Node<E> rightChild) {
			element = e;
			parent = above;
			left = leftChild;
			right = rightChild;
		}
		
		public E getElement() {
			return element;
		}
		
		public Node<E> getParent() {
			return parent;
		}
		
		public Node<E> getLeft() {
			return left;
		}
		
		public Node<E> getRight() {
			return right;
		}
		
		public void setElement(E e) {
			element = e;
		}
		
		public void setParent(Node<E> parentNode) {
			parent = parentNode;
		}
		
		public void setLeft(Node<E> leftChild) {
			left = leftChild;
		}
		
		public void setRight(Node<E> rightChild) {
			right = rightChild;
		}
	}
	
	protected Node<E> createNode(E e, Node<E> parent, Node<E> left, Node<E> right) {
		return new Node<E>(e, parent, left, right);
	}
	
	protected Node<E> root = null;
	private int size = 0;
	
	public LinkedBinaryTree() {
		
	}
	
	protected Node<E> validate(Position<E> p) throws IllegalArgumentException {
		if (!(p instanceof Node)) throw new IllegalArgumentException("Not valid position type");
		Node<E> node = (Node<E>) p;
		if (node.getParent() == node) throw new IllegalArgumentException("p is no longer in the tree");
		return node;
	}
	
	public int size() {
		return size;
	}
	
	public Position<E> root() {
		return root;
	}
	
	public Position<E> parent(Position<E> p) throws IllegalArgumentException {
		Node<E> node = validate(p);
		return node.getParent();
	}
	
	public Position<E> left(Position<E> p) throws IllegalArgumentException {
		Node<E> node = validate(p);
		return node.getLeft();
	}
	
	public Position<E> right(Position<E> p) throws IllegalArgumentException {
		Node<E> node = validate(p);
		return node.getRight();
	}
	
	public Position<E> addRoot(E e) throws IllegalStateException {
		if (!isEmpty()) throw new IllegalStateException("Tree is not empty");
		root = createNode(e, null, null, null);
		size = 1;
		return root;
	}
	
	public Position<E> addLeft(Position<E> p, E e) throws IllegalArgumentException {
		Node<E> parent = validate(p);
		if (parent.getLeft() != null) throw new IllegalArgumentException("p already has a left child");
		Node<E> child = createNode(e, parent, null, null);
		parent.setLeft(child);
		size++;
		return child;
	}
	
	public Position<E> addRight(Position<E> p, E e) throws IllegalArgumentException {
		Node<E> parent = validate(p);
		if (parent.getRight() != null) throw new IllegalArgumentException("p already has a right child");
		Node<E> child = createNode(e, parent, null, null);
		parent.setRight(child);
		size++;
		return child;
	}
	
	public E set(Position<E> p, E e) throws IllegalArgumentException {
		Node<E> node = validate(p);
		E temp = node.getElement();
		node.setElement(e);
		return temp;
	}
	
	public void attach(Position<E> p, LinkedBinaryTree<E> t1, LinkedBinaryTree<E> t2) throws IllegalArgumentException {
		Node<E> node = validate(p);
		if (isInternal(p)) throw new IllegalArgumentException("p must be a leaf");
		size += t1.size() + t2.size();
		if (!t1.isEmpty()) {
			t1.root.setParent(node);
			node.setLeft(t1.root);
			t1.root = null;
			t1.size = 0;
		}
		if (!t2.isEmpty()) {
			t2.root.setParent(node);
			node.setRight(t2.root);
			t2.root = null;
			t2.size = 0;
		}
	}
	
	public E remove(Position<E> p) throws IllegalArgumentException {
		Node<E> node = validate(p);
		if (numChildren(p) == 2) throw new IllegalArgumentException("p has two children");
		Node<E> child = (node.getLeft() != null ? node.getLeft() : node.getRight());
		if (child != null) child.setParent(node.getParent());
		if (node == root) root = child;
		else {
			Node<E> parent = node.getParent();
			if (node == parent.getLeft()) parent.setLeft(child);
			else parent.setRight(child);
		}
		size--;
		E temp = node.getElement();
		node.setElement(null);
		node.setLeft(null);
		node.setRight(null);
		node.setParent(node);
		return temp;
	}
	
	private static String spaces(int d) {
		String str = "";
		for (int i = 0; i < d; i++) str +=" ";
		return str;
	}
	
	public static <E> void printPreorderIndent(Tree<E> T, Position<E> p, int d) {
		System.out.println(spaces(2 * d) + p.getElement( ));
		for (Position<E> c : T.children(p)) printPreorderIndent(T, c, d + 1);
	}
	
	public static <E> void printPreorderLabeled(Tree<E> T, Position<E> p, ArrayList<Integer> path) {
		int d = path.size();
		System.out.print(spaces(2 * d));
		for (int j = 0; j < d; j++) System.out.print(path.get(j) + (j == d - 1 ? " " : "."));
		System.out.println(p.getElement());
		path.add(1);
		for (Position<E> c : T.children(p)) {
			printPreorderLabeled(T, c, path);
			path.set(d, 1 + path.get(d));
		}
		path.remove(d);
	}
	
	public static int diskSpace(Tree<Integer> T, Position<Integer> p) {
		int subtotal = p.getElement( );
		for (Position<Integer> c : T.children(p)) subtotal += diskSpace(T, c);
		return subtotal;
	}
	
	public static <E> void parenthesize(Tree<E> T, Position<E> p) {
		System.out.print(p.getElement());
		if (T.isInternal(p)) {
			boolean firstTime = true;
			for (Position<E> c : T.children(p)) {
				System.out.print((firstTime ? " (" : ", ")); 
				firstTime = false;
				parenthesize(T, c);
			}
			System.out.print(")");
		}
	}
	
	public static void main(String[] args) {
		LinkedBinaryTree<String> lbs = new LinkedBinaryTree<>();
		Position a = lbs.addRoot("A");
		Position b = lbs.addLeft(a, "B");
		lbs.addLeft(b, "Bbl");
		lbs.addRight(b, "Bbr");
		lbs.addRight(a, "C");
		LinkedBinaryTree.printPreorderIndent(lbs, a, 0);
		LinkedBinaryTree.printPreorderLabeled(lbs, a, new ArrayList<>());
		
		LinkedBinaryTree<Integer> lbi = new LinkedBinaryTree<>();
		a = lbi.addRoot(1);
		b = lbi.addLeft(a, 2);
		lbi.addLeft(b, 3);
		lbi.addRight(b, 4);
		lbi.addRight(a, 5);
		System.out.println(LinkedBinaryTree.diskSpace(lbi, a));
		
		LinkedBinaryTree.parenthesize(lbs, lbs.root);
	}
}
