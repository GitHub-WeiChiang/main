package course.c04;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet(name = "SessionTest2", urlPatterns = { "/SessionTest2" })
public class SessionTest2 extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession();
		String msg1 = (String) session.getAttribute("msg1");

		session.setAttribute("msg2", msg1 + "Hi, this is msg2 saved in SessionTest2 </br>");

		RequestDispatcher rd = request.getRequestDispatcher("/course/c04/sessionTestView.jsp");
		rd.forward(request, response);
	}
}
