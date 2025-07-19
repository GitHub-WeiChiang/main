/**
 * 
 * @author ChiangWei
 * @date 2020/5/19
 *
 */

// Represents a Uniform Resource Identifier (URI) reference.
import java.net.URI;
// Checked exception thrown to indicate that a string could not be parsed as a URI reference.
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;

// The PostConstruct annotation is used on a method that needs to be executed after dependency injection is done to perform any initialization.
import javax.annotation.PostConstruct;

// Interface WebSocket
import org.java_websocket.WebSocket;
// A subclass must implement at least onOpen, onClose, and onMessage to be useful.
import org.java_websocket.client.WebSocketClient;
// Interface ServerHandshake
import org.java_websocket.handshake.ServerHandshake;

//The org.slf4j.Logger interface is the main user entry point of SLF4J API. It is expected that logging takes place through concrete implementations of this interface.
import org.slf4j.Logger;
//The LoggerFactory is a utility class producing Loggers for various logging APIs, most notably for log4j, logback and JDK 1.4 logging.
import org.slf4j.LoggerFactory;

//@Order defines the sort order for an annotated component.
import org.springframework.core.annotation.Order;
//Indicates that an annotated class is a "component".
import org.springframework.stereotype.Component;

//Testing framework for Java
import org.testng.util.Strings;

// ��� Spring Boot 2.0 �� WebSocket �Ȥ��
@Component
public class P2pPointClient {
	
	// ��x����
	private Logger logger = LoggerFactory.getLogger(P2pPointClient.class);
	
	// P2P ���������`�I�J�O�A�ȺݡA�S�O�Ȥ�ݡC�@���A�ȺݹB��b 7001 �ݤf(P2pPointServer �� port �r�q)�A�P�ɧ@���Ȥ�q�L ws://localhost:7001 �s����A�Ⱥ�
	private String wsUrl = "ws://localhost:7001/";
	
	// �Ҧ��Ȥ�� WebSocket ���s�����w�s
	private List<WebSocket> localSockets = new ArrayList<>();
	
	public List<WebSocket> getLocalSockets() {
		return localSockets;
	}
	
	public void setLocalSockets(List<WebSocket> localSockets) {
		this.localSockets = localSockets;
	}
	
	/**
	 * �s����A�Ⱥ�
	 */
	@PostConstruct
	@Order(2)
	public void connectPeer() {
		try {
			// �Ы� WebSocket ���Ȥ��
			final WebSocketClient socketClient = new WebSocketClient(new URI(wsUrl)) {

				@Override
				public void onClose(int arg0, String arg1, boolean arg2) {
					logger.info("�_�ʫȤ������");
					localSockets.remove(this);
				}

				@Override
				public void onError(Exception arg0) {
					logger.info("�_�ʫȤ�ݳ���");
					localSockets.remove(this);
				}

				@Override
				public void onMessage(String msg) {
					logger.info("�_�ʫȤ�ݦ���_�ʪA�Ⱥݵo�e������: " + msg);
				}

				@Override
				public void onOpen(ServerHandshake serverHandshake) {
					sendMessage(this, "�_�ʫȤ�ݦ��\�ЫثȤ��");
					
					localSockets.add(this);
				}
				
			};
			
			// �Ȥ�ݶ}�l�s���A�Ⱦ�
			socketClient.connect();
		} catch (URISyntaxException e) {
			logger.info("�_�ʳs�����~: " + e.getMessage());
		}
	}
	
	/**
	 * �V�A�Ⱥݵo�e�����A��e WebSocket �����{ Socket �a�}�N�O�A�Ⱥ�
	 * 
	 * @param ws
	 * @param message
	 */
	public void sendMessage(WebSocket ws, String message) {
		logger.info("�o�e��" + ws.getRemoteSocketAddress().getPort() + "�� p2p ����: " + message);
		ws.send(message);
	}
	
	/**
	 * �V�Ҧ��s���L���A�Ⱥݼs������
	 * 
	 * @param message: �ݼs��������
	 */
	public void broadcast(String message) {
		if (localSockets.size() == 0 || Strings.isNullOrEmpty(message)) {
			return;
		}
		logger.info("Glad to say broadcast to servers being startted!");
		for (WebSocket socket : localSockets) {
			this.sendMessage(socket, message);
		}
		logger.info("Glad to say broadcast to servers has overred!");
	}
	
}
