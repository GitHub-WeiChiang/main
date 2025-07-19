/**
 * 
 * @author ChiangWei
 * @date 2020/01/11
 *
 */

public class ModelDuck extends Duck {
	public ModelDuck() {
		flyBehavior = new FlyNoWay();
		quackBehavior = new Quack();
	}
	
	@Override
	public void display() {
		System.out.println("I'm a model duck");
	}
}
