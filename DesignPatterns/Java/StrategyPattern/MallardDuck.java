/**
 * 
 * @author ChiangWei
 * @date 2020/01/11
 *
 */

public class MallardDuck extends Duck {
	public MallardDuck() {
		quackBehavior = new Quack();
		flyBehavior = new FlyWithWings();
	}
	
	@Override
	public void display() {
		System.out.println("I'm a real Mallard duck");
	}
}
