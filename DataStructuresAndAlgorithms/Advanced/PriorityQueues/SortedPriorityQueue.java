/**
 * 
 * @author ChiangWei
 * @date 2020/3/30
 *
 */

import java.util.Comparator;

public class SortedPriorityQueue<K, V> extends AbstractPriorityQueue<K, V> {
	public static void main(String[] args) {
		SortedPriorityQueue<Integer, Integer> upq = new SortedPriorityQueue<>();
		upq.insert(1, 1);
		upq.insert(5, 5);
		upq.insert(2, 2);
		upq.insert(4, 4);
		upq.insert(3, 3);
		System.out.println(upq.min().getKey());
		upq.removeMin();
		System.out.println(upq.min().getKey());
		upq.removeMin();
		System.out.println(upq.min().getKey());
		upq.removeMin();
		System.out.println(upq.min().getKey());
		upq.removeMin();
		System.out.println(upq.min().getKey());
		upq.removeMin();
	}
	
	private PositionalList<Entry<K, V>> list = new LinkedPositionalList<>();
	
	public SortedPriorityQueue() {
		super();
	}
	
	public SortedPriorityQueue(Comparator<K> comp) {
		super(comp);
	}
	
	public Entry<K, V> insert(K key, V value) throws IllegalArgumentException {
		checkKey(key);
		Entry<K, V> newest = new PQEntry<>(key, value);
		Position<Entry<K, V>> walk = list.last();
		while (walk != null && compare(newest, walk.getElement()) < 0) {
			walk = list.before(walk);
		}
		if (walk == null) list.addFirst(newest);
		else list.addAfter(walk, newest);
		return newest;
	}
	
	public Entry<K, V> min() {
		if (list.isEmpty()) return null;
		return list.first().getElement();
	}
	
	public Entry<K,V> removeMin() {
		if (list.isEmpty()) return null;
		return list.remove(list.first());
	}
	
	public int size() {
		return list.size();
	}
}
