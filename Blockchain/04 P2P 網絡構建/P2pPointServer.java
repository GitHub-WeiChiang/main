/**
 * 
 * @author ChiangWei
 * @date 2020/5/13
 *
 */

// This class implements an IP Socket Address (IP address + port number) It can also be a pair (hostname + port number), in which case an attempt will be made to resolve the hostname. If resolution fails then the address is said to be unresolved but can still be used on some circumstances like connecting through a proxy.
import java.net.InetSocketAddress;
import java.util.ArrayList;
import java.util.List;

// The PostConstruct annotation is used on a method that needs to be executed after dependency injection is done to perform any initialization.
import javax.annotation.PostConstruct;

// Interface WebSocket
import org.java_websocket.WebSocket;
// Interface ClientHandshake
import org.java_websocket.handshake.ClientHandshake;
// WebSocketServer is an abstract class that only takes care of the HTTP handshake portion of WebSockets. It's up to a subclass to add functionality/purpose to the server.
import org.java_websocket.server.WebSocketServer;

// The org.slf4j.Logger interface is the main user entry point of SLF4J API. It is expected that logging takes place through concrete implementations of this interface.
import org.slf4j.Logger;
// The LoggerFactory is a utility class producing Loggers for various logging APIs, most notably for log4j, logback and JDK 1.4 logging.
import org.slf4j.LoggerFactory;

// @Order defines the sort order for an annotated component.
import org.springframework.core.annotation.Order;
// Indicates that an annotated class is a "component".
import org.springframework.stereotype.Component;

//Testing framework for Java
import org.testng.util.Strings;

// ��� Spring Boot �� WebSocket �A�Ⱥ�
@Component
public class P2pPointServer {
	
	// ��x����
	private Logger logger = LoggerFactory.getLogger(P2pPointServer.class);
	
	// ���� Server �� WebSocket �ݤf
	// �h�����ծɥi�H���ܸӭ�
	private int port = 7001;
	
	// �Ҧ��s����A�Ⱥݪ� WebSocket �w�s��
	private List<WebSocket> localSockets = new ArrayList<>();
	
	public List<WebSocket> getLocalSockets() {
		return localSockets;
	}
	
	public void setLocalSockets(List<WebSocket> localSockets) {
		this.localSockets = localSockets;
	}
	
	/**
	 * ��l�� P2P Server ��
	 * 
	 * @param Server �ݪ��ݤf�� port
	 */
	// ���O�� initServer() �b�A�ȱҰʮɴN��[���A�� @PostConstruct �аO�Ϩ�b�A�Ⱦ��[�� bean ���ɭԹB��A�åB�u�|�Q�A�Ⱦ�����@���C
	@PostConstruct
	// ���O�ҪA�Ⱥݥ���Ȥ�ݥ[���A�� @Order(1) �Х� initServer()
	@Order(1)
	public void initServer() {
		/**
		 * ��l�� WebSocket ���A�Ⱥݩw�q��������H socketServer, ���� WebSocketServer
		 * InetSocketAddress(port) �O WebSocketServer �c�y�����ѼơAInetSocketAddress �O(IP �a�} + �ݤf��)�����A�Y�ݤf�a�}�����C
		 */
		final WebSocketServer socketServer = new WebSocketServer(new InetSocketAddress(port)) {
			/**
			 * ���g 5 �Өƥ��k�A�ƥ�o�ͮ�Ĳ�o��������k
			 */
			
			@Override
			// �_�}�s���ɭ�Ĳ�o
			public void onClose(WebSocket webSocket, int i, String s, boolean b) {
				logger.info(webSocket.getRemoteSocketAddress() + "�Ȥ�ݻP�A�Ⱦ��_�}�s��!");
				
				// ��Ȥ���_�}�s���ɡAWebSocket �s�����R���ӳs��
				localSockets.remove(webSocket);
			}

			@Override
			// �s���o�Ϳ��~�ɽեΡA�򱵵�Ĳ�o onClose ��k
			public void onError(WebSocket webSocket, Exception e) {
				logger.info(webSocket.getRemoteSocketAddress() + "�Ȥ���챵���~!");
				localSockets.remove(webSocket);
			}

			@Override
			// ����Ȥ�ݵo�Ӫ�������Ĳ�o
			public void onMessage(WebSocket webSocket, String msg) {
				logger.info("�_�ʪA�Ⱥݱ�����Ȥ�ݮ���: " + msg);
				sendMessage(webSocket, "�������");
			}

			@Override
			// �Ыسs�����\��Ĳ�o
			public void onOpen(WebSocket webSocket, ClientHandshake clientHandshake) {
				sendMessage(webSocket, "�_�ʪA�Ⱥݦ��\�s��");
				
				// ���\�Ыؤ@�� WebSocket �s���ɡA�N�ӳs���[�J�s����
				localSockets.add(webSocket);
			}

			@Override
			// �A�Ⱥݱҥήɽե�
			public void onStart() {
				logger.info("�_�ʪ� WebSocket Server �ݱҰ�...");
			}
			
		};
		
		socketServer.onStart();
		logger.info("�_�ʪA�Ⱥݺ�ť socketServer �ݤf: " + port);
	}
	
	/**
	 * �V�s���쥻�����Y�ӫȤ�ݵo�e����
	 * 
	 * @param ws
	 * @param message
	 */
	public void sendMessage(WebSocket ws, String message) {
		logger.info("�o�e��" + ws.getRemoteSocketAddress().getPort() + "�� p2p �����O: " + message);
		ws.send(message);
	}
	
	/**
	 * �V�Ҧ��s���쥻�����Ȥ�ݼs������
	 * 
	 * @param message: �ݼs�����e
	 */
	public void broadcast(String message) {
		if (localSockets.size() == 0 || Strings.isNullOrEmpty(message)) {
			return;
		}
		
		logger.info("Glad to say broadcast to clients being startted!");
		for (WebSocket socket : localSockets) {
			this.sendMessage(socket, message);
		}
		logger.info("Glad to say broadcast to clients has overred!");
	}
	
}
