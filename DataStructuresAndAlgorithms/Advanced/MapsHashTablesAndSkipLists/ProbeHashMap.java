
/**
 * 
 * @author ChiangWei
 * @date 2020/4/5
 *
 */

import java.util.ArrayList;

public class ProbeHashMap<K, V> extends AbstractHashMap<K, V> {
	public static void main(String[] args) {
		ProbeHashMap<Integer, Integer> phm = new ProbeHashMap<>();
		phm.put(3, 3);
		phm.put(0, 0);
		phm.put(2, 2);
		phm.put(4, 4);
		phm.put(1, 1);
		for(Entry<Integer, Integer> i : phm.entrySet()) {
			System.out.println(i.getKey() + " - " + i.getValue());
		}
	}
	
	private MapEntry<K, V>[] table;
	private MapEntry<K, V> DEFUNCT = new MapEntry<>(null, null);

	public ProbeHashMap() {
		super();
	}

	public ProbeHashMap(int cap) {
		super(cap);
	}

	public ProbeHashMap(int cap, int p) {
		super(cap, p);
	}

	protected void createTable() {
		table = (MapEntry<K, V>[]) new MapEntry[capacity];
	}

	private boolean isAvailable(int j) {
		return (table[j] == null || table[j] == DEFUNCT);
	}

	private int findSlot(int h, K k) {
		int avail = -1;
		int j = h;
		do {
			if (isAvailable(j)) {
				if (avail == -1) {
					avail = j;
				}
				if (table[j] == null) {
					break;
				}
			} else if (table[j].getKey().equals(k)) {
				return j;
			}
			j = (j + 1) % capacity;
		} while (j != h);
		return -(avail + 1);
	}

	protected V bucketGet(int h, K k) {
		int j = findSlot(h, k);
		if (j < 0) {
			return null;
		}
		return table[j].getValue();
	}

	protected V bucketPut(int h, K k, V v) {
		int j = findSlot(h, k);
		if (j >= 0) {
			return table[j].setValue(v);
		}
		table[-(j + 1)] = new MapEntry<>(k, v);
		n++;
		return null;
	}

	protected V bucketRemove(int h, K k) {
		int j = findSlot(h, k);
		if (j < 0) {
			return null;
		}
		V answer = table[j].getValue();
		table[j] = DEFUNCT;
		n--;
		return answer;
	}

	public Iterable<Entry<K, V>> entrySet() {
		ArrayList<Entry<K, V>> buffer = new ArrayList<>();
		for (int h = 0; h < capacity; h++) {
			if (!isAvailable(h)) {
				buffer.add(table[h]);
			}
		}
		return buffer;
	}
}
