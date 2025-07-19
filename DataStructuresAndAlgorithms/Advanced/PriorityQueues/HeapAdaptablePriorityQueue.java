
/**
 * 
 * @author ChiangWei
 * @date 2020/4/2
 *
 */

import java.util.Comparator;

public class HeapAdaptablePriorityQueue<K, V> extends HeapPriorityQueue<K, V> implements AdaptablePriorityQueue<K, V> {
	public static void main(String[] args) {
		HeapAdaptablePriorityQueue<Integer, Integer> hapq = new HeapAdaptablePriorityQueue<>();
		Entry<Integer, Integer> temp;
		hapq.insert(0, 0);
		hapq.insert(2, 2);
		temp = hapq.insert(4, 4);
		hapq.insert(3, 3);
		hapq.insert(1, 1);
		
		hapq.replaceKey(temp, -1);
		hapq.replaceValue(temp, -1);
		
		System.out.println(hapq.removeMin().getValue());
		System.out.println(hapq.removeMin().getValue());
		System.out.println(hapq.removeMin().getValue());
		System.out.println(hapq.removeMin().getValue());
		System.out.println(hapq.removeMin().getValue());
		System.out.println(hapq.removeMin());
	}
	
	protected static class AdaptablePQEntry<K, V> extends PQEntry<K, V> {
		private int index;

		public AdaptablePQEntry(K key, V value, int j) {
			super(key, value);
			index = j;
		}

		public int getIndex() {
			return index;
		}

		public void setIndex(int j) {
			index = j;
		}
	}

	public HeapAdaptablePriorityQueue() {
		super();
	}

	public HeapAdaptablePriorityQueue(Comparator<K> comp) {
		super(comp);
	}

	protected AdaptablePQEntry<K, V> validate(Entry<K, V> entry) throws IllegalArgumentException {
		if (!(entry instanceof AdaptablePQEntry))
			throw new IllegalArgumentException("Invalid entry");
		AdaptablePQEntry<K, V> locator = (AdaptablePQEntry<K, V>) entry;
		int j = locator.getIndex();
		if (j >= heap.size() || heap.get(j) != locator)
			throw new IllegalArgumentException("Invalid entry");
		return locator;
	}

	protected void swap(int i, int j) {
		super.swap(i, j);
		((AdaptablePQEntry<K, V>) heap.get(i)).setIndex(i);
		((AdaptablePQEntry<K, V>) heap.get(j)).setIndex(j);
	}

	protected void bubble(int j) {
		if (j > 0 && compare(heap.get(j), heap.get(parent(j))) < 0)
			upheap(j);
		else
			downheap(j);
	}

	public Entry<K, V> insert(K key, V value) throws IllegalArgumentException {
		checkKey(key);
		Entry<K, V> newest = new AdaptablePQEntry<>(key, value, heap.size());
		heap.add(newest);
		upheap(heap.size() - 1);
		return newest;
	}

	public void remove(Entry<K, V> entry) throws IllegalArgumentException {
		AdaptablePQEntry<K, V> locator = validate(entry);
		int j = locator.getIndex();
		if (j == heap.size() - 1)
			heap.remove(heap.size() - 1);
		else {
			swap(j, heap.size() - 1);
			heap.remove(heap.size() - 1);
			bubble(j);
		}
	}

	public void replaceKey(Entry<K, V> entry, K key) throws IllegalArgumentException {
		AdaptablePQEntry<K, V> locator = validate(entry);
		checkKey(key);
		locator.setKey(key);
		bubble(locator.getIndex());
	}

	public void replaceValue(Entry<K, V> entry, V value) throws IllegalArgumentException {
		AdaptablePQEntry<K, V> locator = validate(entry);
		locator.setValue(value);
	}
}
