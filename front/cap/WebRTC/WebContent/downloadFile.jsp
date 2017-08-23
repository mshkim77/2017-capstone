<%@page import="java.io.FileWriter"%>
<%@page import="java.io.BufferedWriter"%>
<%@page import="java.net.URLEncoder"%>
<%@page import="java.util.Enumeration"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page import="java.io.File, java.io.IOException"
	import="com.oreilly.servlet.MultipartRequest"
	import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>페이지 이름</title>
</head>

<body>
	<%
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("utf-8");
		response.setContentType("text/html; charset=UTF-8");

		//파일 저장될 위치 저장
		//String savePath = "/Users/Sooduck/Documents/JSPWorkspace/Test/JSPproject/WebContent/upload";
		//"/Users/Sooduck/Documents/JSPWorkspace/Test/AndroidProject/WebContent/ImageData"; // 저장할 디렉토리 (절대경로)
		//String savePath = "/Applications/MAMP/apache-tomcat-7.0.57/webapps/JSPproject/upload";
		String savePath = "/Users/sooduck/Develop/JSPWorkspace/cap/WebRTC/WebContent/upload";

		//파일 제한크기
		int sizeLimit = 100 * 1024 * 1024;
		String fileName;
		String originalFileName;
		String bName, bTitle, bContent, bImg, bpassword;
		File fff;

		try {
			MultipartRequest multi = new MultipartRequest(request,
					savePath, sizeLimit, "UTF-8",
					new DefaultFileRenamePolicy());

			bTitle = multi.getParameter("fname");
			bImg = multi.getParameter("data");
			fff = multi.getFile("data");
			originalFileName = multi.getOriginalFileName("data");
			
			
			
			/* bName = multi.getParameter("bName");
			bTitle = multi.getParameter("bTitle");
			bContent = multi.getParameter("bContent");
			bpassword = multi.getParameter("bPassword"); */

		/* 	//파일 이름 얻음
			fileName = multi.getFilesystemName("bImg");
			//이름 중복시 원래이름 얻기
			originalFileName = multi.getOriginalFileName("bImg");
 */
			/* if (fileName == null) { //업로드 안될때 */
	%>
	<!-- <h2>파일 업로드 실패</h2>
	<br>
	<a href="javacript:history.back()"> 재업로드 </a> -->
	<%
		/* } else { //업로드 될때
				File file1 = multi.getFile("bImg");
				String division = multi.getParameter("division");
				String contents = multi.getParameter("contents"); */
	%>
	<%-- <h2>파일 업로드 완료</h2>
	저장된 파일이름:
	<%=fileName%><br> 변경전 파일이름:
	<%=originalFileName%><br> 종류:
	<%=division%><br> 설명:
	<%=contents%><br> 사이즈:
	<%=file1.length()%>byte
	<br> contentType:
	<%=multi.getContentType("bImg")%><br> --%>

	<%
		/* System.out.println(bName + ", " + bTitle + ", " + bContent
						+ ", " + /* originalFileName */ /* bpassword); */

				/* String sendUrl = new String("News1BoardWrite.do?bName=" + bName
						+ "&bTitle=" + bTitle + "&bContent=" + bContent
						+ "&bImg=" + originalFileName + "&bPassword="
						+ bpassword); */

				/* String sendUrl = new String("index.html"); */
						
				/* String sendutf = URLEncoder.encode(sendUrl, "UTF-8"); */
				/* response.sendRedirect(sendUrl); */
				
				out.println("Suss");
				
				Enumeration eenum = multi.getFileNames();
				
				while(eenum.hasMoreElements()) {
					
					out.println("name : " + eenum.nextElement());
				
				}
				
				out.println(bTitle);
				out.println(originalFileName);
				out.println("file size : " + (int)fff.length());

			/* } */
		} catch (Exception e) {
			out.println("IOException 발생<br><pre>" + e.getMessage()
					+ "</pre>");
		} 
	%>
</body>
</html>