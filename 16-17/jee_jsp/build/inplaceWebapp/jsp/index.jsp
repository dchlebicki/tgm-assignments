<%--
  Created by IntelliJ IDEA.
  User: Dominik
  Date: 29.05.2017
  Time: 14:50
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Java EE Servlets</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  </head>
  <body>
    <div class="jumbotron text-center">
      <h1>Willkommen!</h1>
      <p>von Dominik Chlebicki</p>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-sm-4 text-left">
          <h3>Heute ist der <%= main.java.servlet.Servlet.getDate() %></h3>
        </div>
        <div class="col-sm-4 text-center">
          <h3>Es ist <%= main.java.servlet.Servlet.getTime() %> Uhr</h3>
        </div>
        <div class="col-sm-4 text-right">
          <h3><%= main.java.servlet.Servlet.getMessage() %></h3>
        </div>
      </div>
    </div>
  </body>
</html>
